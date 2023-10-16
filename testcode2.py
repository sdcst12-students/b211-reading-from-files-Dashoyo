#!python3
import json

filename = 'data.txt'

file = open(filename,'r')
data = file.read()
try:
    jsondata = json.loads(data)
except Exception as e:
    print(e)

for i in jsondata:
    print(i)