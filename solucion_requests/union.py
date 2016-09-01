import csv
import json
import io
import re
import codecs

with io.open("admin.json",'r',encoding='utf-8') as f:
	json_data0 = f.read()
with io.open("antropologia.json",'r',encoding='utf-8') as f:
	json_data1 = f.read()
with io.open("arte.json",'r',encoding='utf-8') as f:
	json_data2 = f.read()
with io.open("cpol.json",'r',encoding='utf-8') as f:
	json_data3 = f.read()
with io.open("filosofia.json",'r',encoding='utf-8') as f:
	json_data4 = f.read()
with io.open("historia.json",'r',encoding='utf-8') as f:
	json_data5 = f.read()
with io.open("lyc.json",'r',encoding='utf-8') as f:
	json_data6 = f.read()
with io.open("psicologia.json",'r',encoding='utf-8') as f:
	json_data7 = f.read()

j0 = json.loads(json_data0)
j1 = json.loads(json_data7)
j2 = json.loads(json_data4)
j3 = json.loads(json_data7)
j4 = json.loads(json_data0)
j5 = json.loads(json_data7)
j6 = json.loads(json_data4)
j7 = json.loads(json_data7)
print (len(j0+j1+j2+j3+j4+j5+j6+j7))
un = j0+j1+j2+j3+j4+j5+j6+j7

with open('eventos.json', 'w') as outfile:
	json.dump(un, outfile)
