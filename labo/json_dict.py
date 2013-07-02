import json

st = '{"bln":true,"intg":20,"mixed":{"str":"hoge"}}'

dic = json.loads(st)

print dic['mixed']

jsn_str = json.dumps(dic['mixed'])

print jsn_str
