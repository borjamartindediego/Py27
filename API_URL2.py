# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 21:11:52 2019

@author: BorjaLocal
"""
import json, requests
'''
#f = io.open('api.json',mode='r',encoding='utf-8')
#f = io.open('ejemplo.json',mode='r',encoding='utf-8')
#txtjson=f.read()
'''
#print (txtjson)

req=requests.get('https://dapi.olympicchannel.com/v2/content/en-us/epg/')
#req en este caso es un objeto
#text es un atributo no un método ( no lleva paréntesis)
# req.text='aaaaaaa'  => No podemos cambiar su valor, el atributo en este caso es como una contante
txtjson=req.text
#print (txtjson)
jsonObj=json.loads(txtjson)
#los items de la etiqueta items están metidos en una lista
#print(json)
#con w+ el archivo se hace delctura y escritura 
f=open('html5.htm','r')
#f es un objeto con el metodo leer
html=f.read()
f.close()
f=open('entities.htm','w')
#Elarray asociativo o diccionario funciona con claves en vez de indices
for i in range (0,6):
    linea="<span class='strong'>Item "+ str(i+1)+ ":</span><br>slug = " + jsonObj['items'][i]['slug']
    linea+="<span class='strong'></span><br>title = " + jsonObj['items'][i]['title']
    linea+="<span class='strong'></span><br>selfUrl = " + jsonObj['items'][i]['selfUrl'] +"</a>"
    linea+="<span class='strong'></span><br>Wonfeed = " + jsonObj['items'][i]['fields']['WonFeed'] +"</a>"
    linea+="<span class='strong'></span><br>VideoUrl = " + jsonObj['items'][i]['fields']['VideoUrl'] +"</a>"
    linea+="<span class='strong'></span><br>VideoUrl = " + jsonObj['items'][i]['tags'][3]['extraData']["EntityId"]+"</a>"
    
#    linea+="<span class='strong'></span><br>selfUrl = " + jsonObj['items'][i]['selfUrl'] +"</a>"
#    linea+="<span class='strong'></span><br>selfUrl = " + jsonObj['items'][i]['selfUrl'] +"</a>"
#    linea+="<span class='strong'></span><br>selfUrl = " + jsonObj['items'][i]['selfUrl'] +"</a>"
#    linea+="<span class='strong'></span><br>selfUrl = " + jsonObj['items'][i]['selfUrl'] +"</a>"
#    linea+="<span class='strong'></span><br>selfUrl = " + jsonObj['items'][i]['selfUrl'] +"</a>"
    print(linea)
    #acumulamos html + el valor de la variable
    html+='<p>'+linea+'</p>\n'

html+='</body></html>'
f.write(html)
f.close()
