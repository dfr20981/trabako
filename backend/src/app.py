from re import S
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/trabajo'
mongo = PyMongo(app)

db =mongo.db.trabajo
#################################################################################insertar productos 
@app.route('/pro', methods=['POST'])
def neoProductos():
  print(request.json)
  id = db.insert({
    'productos': request.json['producto'],
    'item': request.json['cantidad'],
    
  })
  return jsonify(str(ObjectId(id)))
  ###############################################################################ver productos 
@app.route('/pro', methods=['GET'])
def veoProductos():
    trabajo = []
    for doc in db.find():
        trabajo.append({
            '_id': str(ObjectId(doc['_id'])),
            'productos': doc['productos'],
            'item': doc['item']
        })
    return jsonify(trabajo)
################################################################################ optere solo un resultado 
@app.route('/user', methods=['POST'])
def crearClaseCliente():
  print(request.json)
  id = db.insert({
    'nombre': request.json['nom'],
    'edad': request.json['cantidad'],
    'carrito_de_compras': request.json[''],
    'direcciones': request.json['direcciones']
  })
  return jsonify(str(ObjectId(id)))
################################################################################
if __name__ == "__main__":
    app.run(debug=True)