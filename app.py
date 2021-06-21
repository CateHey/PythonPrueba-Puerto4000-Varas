
import json
from flask import Flask, jsonify
import re
#app es la aplicacion de servidor
app = Flask (__name__)
#abrimos el archivo json generado con el txt
f = open ('listacompleta.json',"r")
c= f.read()
#retorna un json como diccionario
#cerramos el archivo json  
f.close()
data = json.loads(c)

@app.route('/datos/<string:query>', methods=['GET'])
def datos(query):
    resultado= []
    for i in range(0, 99):
        if (re.search(query, data["datos"][i]['nombre'])):
            resultado.append(data["datos"][i])
    return jsonify(resultado)

#si se ejecuta como main o archivo principal
if __name__ == '__main__':
#ejecutamos como debug
    app.run(debug=True, port=4000)