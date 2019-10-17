# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:11:24 2019

@author: BorjaLocal
"""

import json, requests

req=requests.get('https://dapi.olympicchannel.com/v2/content/en-us/epg/')
#req en este caso es un objeto
#text es un atributo no un método ( no lleva paréntesis)
# req.text='aaaaaaa'  => No podemos cambiar su valor, el atributo en este caso es como una contante
txtjson=req.text
#print (txtjson)
jsonObj=json.loads(txtjson)
#print(jsonObj['items'][0]['fields'])

for i in range (0,24):
    #%d digitos entero  %S strings       %f para datos decimales
    print("Item %d %s : " % (i,jsonObj['items'][i]['fields']["VideoUrl"]))
    # {} las llaves es poscional respecto al parentesis 
    #print("Item {} {} : ".format(i,jsonObj['items'][i]['fields']["VideoUrl"]))
    #print("Item % : "+(jsonObj['items'][i]['fields']["StartTime"])
    
#los items de la etiqueta items están metidos en una lista
##print(json)
##con w+ el archivo se hace delctura y escritura 
#f=open('html5.htm','r')
##f es un objeto con el metodo leer
#html=f.read()
#f.close()
#f=open('entities.htm','w')
#for i in range (0,24):
#    linea="<span class='strong'>Item "+ str(i+1)+ ":</span>\nEntity_ID = " + jsonObj['items'][i]['_entityId']
#    print(linea)
#    #acumulamos html + el valor de la variable
#    html+='<p>'+linea+'</p>\n'
#
#html+='</body></html>'
#f.write(html)
#f.close()
