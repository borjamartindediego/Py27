mport io
import json, requests
'''
f = io.open('api.json',mode='r',encoding='utf-8')
#f = io.open('ejemplo.json',mode='r',encoding='utf-8')
txtjson=f.read()
'''
#print (txtjson)

req=requests.get('https://dapi.olympicchannel.com/v2/content/en-us/epg/')
txtjson=req.text
#print (txtjson)
jsonObj=json.loads(txtjson)
#los items de la etiqueta items están metidos en una lista
#print(json)
html='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        </style>
</head>
<body>'''
for i in range (0,24):
    linea="<span class='strong'>Item "+ str(i+1)+ ":<\span>\nEntity_ID = " + jsonObj['items'][i]['_entityId']
    print(linea)
    html+='<p>'+linea+'</p>\n'

html+='</body></html>'
f=open('entities.htm','w')
f.write(html)
f.close()
