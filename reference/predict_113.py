"""Run unchanged core24 and the 89 pinned raw DART assay models."""
import argparse,json,pathlib,subprocess,sys,warnings
import joblib,numpy as np,pandas as pd
import predict_24 as p
ROOT=pathlib.Path(__file__).resolve().parent

def main():
 a=argparse.ArgumentParser();a.add_argument('input',type=pathlib.Path);a.add_argument('-o','--output',type=pathlib.Path,default=pathlib.Path('predictions_113.xlsx'));args=a.parse_args()
 subprocess.run([sys.executable,str(ROOT/'predict_24.py'),str(args.input),'-o',str(args.output)],check=True)
 p.install_sklearn_compatibility_shim();warnings.filterwarnings('ignore')
 raw=p.load_input(args.input,None,'SMILES','ID'); specs=json.loads((ROOT/'dart_model_manifest.json').read_text());records=[];mols=[];valid=[]
 for i,r in raw.iterrows():
  mol=p.Chem.MolFromSmiles(str(r['SMILES']));valid.append(mol is not None)
  if mol is not None:mols.append(mol)
 cache={}
 for s in specs:
  model=joblib.load(ROOT/s['artifact_path']);key=(s['native_fingerprint'],s['model_features'])
  if key not in cache:cache[key]=p.native_feature_matrix(mols,*key)
  prob=p.positive_probability(model,cache[key]);j=0
  for i,r in raw.iterrows():
   if not valid[i]:continue
   pr=float(prob[j]);j+=1
   records.append(dict(query_id=str(r['ID']),input_smiles=str(r['SMILES']),endpoint_code=s['endpoint_code'],aeid=s['aeid'],assay=s['endpoint'],positive_probability=pr,prediction=int(pr>=s['decision_threshold']),ad_flag='Not assessed',evidence_status='Raw prediction; AD unavailable'))
 detail=pd.DataFrame(records)
 with pd.ExcelWriter(args.output,engine='openpyxl',mode='a',if_sheet_exists='replace') as writer:
  detail.to_excel(writer,sheet_name='DART Detail',index=False)
  for col,sheet in [('prediction','DART Prediction'),('positive_probability','DART Probability')]:
   piv=detail.pivot(index='query_id',columns='endpoint_code',values=col).reindex(columns=[s['endpoint_code'] for s in specs]).reset_index();piv.to_excel(writer,sheet_name=sheet,index=False)
  pd.DataFrame(specs).to_excel(writer,sheet_name='DART manifest',index=False)
 print(f'Completed 24 core + {len(specs)} raw DART models: {args.output}')
if __name__=='__main__':main()
