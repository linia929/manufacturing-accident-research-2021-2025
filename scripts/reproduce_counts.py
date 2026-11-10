"""Reproduce accident-summary counts; no third-party dependencies or network."""
from pathlib import Path
import csv, json, collections, hashlib
ROOT=Path(__file__).resolve().parents[1]
def read(name):
    with (ROOT/'data'/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
cases=read('cases_103.csv');axis=read('international_axis_103.csv');ev=read('evidence_index_49.csv');book=read('esaw_codebook_used.csv')
ids={r['case_id'] for r in cases};valid={r['code'] for r in book}
assert len(cases)==len(ids)==103
assert len(axis)==len({r['case_id'] for r in axis})==103
assert {r['case_id'] for r in axis}==ids
assert all(r['ESAW2013_contact_code'] in valid for r in axis)
assert all(r['evidence_based_reason'] and r['evidence_locator'] and r['official_url'] for r in axis)
assert all(r['alternative_codes'] for r in axis if r['ESAW2013_contact_code']=='00')
count=collections.Counter(r['ESAW2013_contact_code'] for r in axis)
assert count['00']==13 and sum(count.values())==103
precision=collections.Counter(r['decision_resolution'] for r in axis)
assert precision=={'specific':85,'group_only':5,'not_unique':13}
assert len(ev)==len({r['case_id'] for r in ev})==49 and all(r['case_id'] in ids for r in ev)
domains={k:sum(int(r[k+'_recorded']) for r in ev) for k in 'HMEG'}
assert domains==dict(H=49,M=23,E=11,G=48)
for r in read('esaw_counts.csv'):
    assert int(r['n_accident_summaries'])==count[r['contact_code']]
    assert abs(float(r['share_all_103'])-count[r['contact_code']]/103)<1e-6
    if r['contact_code']!='00':assert abs(float(r['share_among_90_assignable'])-count[r['contact_code']]/90)<1e-6
manifest=ROOT/'MANIFEST.sha256'
if manifest.exists():
    for line in manifest.read_text(encoding='utf-8').splitlines():
        digest,path=line.split('  ',1)
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
print(json.dumps({'n_accidents':len(cases),'n_contact_decisions':len(axis),'coding_unit':'accident_summary_not_complete_victim_ESAW','precision':dict(precision),'contact_counts':dict(sorted(count.items())),'sector':dict(collections.Counter(r['research_sector'] for r in cases)),'year':dict(sorted(collections.Counter(r['year'] for r in cases).items())),'four_domain_positive_records_49_cases':domains,'all_checks_passed':True},ensure_ascii=False,indent=2))
