import json,io
#convertimos el json a python

#"_entityId" "slug"



#C:\Users\BorjaLocal\Desktop\PYTHON\Eljercicios 3.7\DOCS\ejemplo_API.txt



#f = open('ejemplo_API.txt') #,encoding='utf-8' valido en py3

f = io.open('api.json',mode='r',encoding='utf-8')
#f = io.open('ejemplo.json',mode='r',encoding='utf-8')
txtjson=f.read()
#print (txtjson)
jsonObj=json.loads(txtjson)
#los items de la etiqueta items están metidos en una lista

for i in range (0,24):
   print(jsonObj['items'][i]['_entityId'])
   
    
    
    
    
    



b
