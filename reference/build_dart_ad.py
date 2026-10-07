"""Extend the frozen core24 AD procedure to the 89 DART assays."""
import pathlib,json,sys,gzip,hashlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import predict_24 as p
p.RDLogger.DisableLog('rdApp.*')
root=p.ROOT;models=json.loads((root/'dart_model_manifest.json').read_text());lineage=json.load(open(root/'ad_build_inputs/lineage.json'));smap=json.load(open(root/'ad_build_inputs/structure_map.json'))
# Freeze structure preprocessing once; retain duplicate rows as in core24.
needed={x for v in lineage.values() for x in v['dtxsids']};std={}
for id in sorted(needed):
 s,m,e=p.standardize_smiles(smap.get(id,''))
 if m is not None:std[id]=(s,p.AD_GENERATOR.GetFingerprint(m))
with gzip.open(root/'ad_reference_smiles.json.gz','rt') as f: refs=json.load(f)
audit={'method':json.loads((root/'method_audit.json').read_text())['method'],'lineage':{'hitcall_git_blob_sha':'8e707bed768d2444488ebe57423bf9ca352dfd92','reference_rows_before_exclusion':8984,'fingerprint_rows':8968,'split':'train_test_split(test_size=0.2,shuffle=True,random_state=42), no stratification; same reconstructed lineage as core24','structure_mapping':'Local DSSTox exports; structures recovered by DTXSID with CAS source preference','structure_source_files':json.load(open(root/'ad_build_inputs/structure_sources.json'))},'endpoints':{}}
density_cache={}
for spec in models:
 code=spec['endpoint_code'];lin=lineage[code];ids=lin['dtxsids'];selected=[std[id] for id in ids if id in std];bits=[x[1] for x in selected];assert len(bits)>5,(code,len(bits))
 key=tuple(x[0] for x in selected)
 if key in density_cache: density=density_cache[key]
 else:
  density=np.empty(len(bits))
  for i,b in enumerate(bits):
   sim=np.asarray(p.DataStructs.BulkTanimotoSimilarity(b,bits));sim[i]=-np.inf;density[i]=np.partition(sim,len(bits)-5)[-5:].mean()
  density_cache[key]=density
 threshold=float(np.percentile(density,5));refs[code]=[x[0] for x in selected]
 spec.update(tier='General DART mechanism',artifact_kind='sklearn_estimator',ad_reference_n=len(bits),ad_threshold=threshold,ad_method='Morgan radius 2, 2048-bit query Tmax; threshold is 5th percentile of mean top-5 training-neighbor Tanimoto',ad_status='Assessed with unified core24 AD procedure',ad_reference_basis='Reconstructed model-fit reference using frozen core24 ToxCast lineage')
 audit['endpoints'][code]={'assay':spec['endpoint'],'labeled_rows':lin['labeled_n'],'reconstructed_fit_rows':len(ids),'AD_reference_fingerprints':len(bits),'missing_or_rejected_structures':len(ids)-len(bits),'unique_preprocessed_structures':len(set(refs[code])),'threshold':threshold,'density_median':float(np.median(density))}
 print(code,len(bits),threshold,flush=True)
(root/'dart_model_manifest.json').write_text(json.dumps(models,ensure_ascii=False,indent=2));core=json.loads((root/'model_manifest.json').read_text());(root/'model_manifest_113.json').write_text(json.dumps(core+models,ensure_ascii=False,indent=2))
with gzip.open(root/'ad_reference_smiles_113.json.gz','wt',encoding='utf-8') as f:json.dump(refs,f,ensure_ascii=False)
(root/'dart_ad_method_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2));print('Built AD for all 113 models',flush=True)
