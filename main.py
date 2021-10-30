from flask import Flask, request, jsonify
from flask_cors import CORS
from Usuario import Usuario
import json

app = Flask(__name__)
Usuarios = []
CORS(app)

@app.route("/usuarios", methods=['GET'])
def obtenerUsuarios():
    global Usuarios
    envios =[]
    for usuario in Usuarios:
        unEnvio = {
            "nombre": usuario.getNombre(),
            "edad": usuario.getEdad(),
            "username":usuario.getUsername(),
            "password":usuario.getPassword()
        }
        envios.append(unEnvio)
    respuesta = jsonify(envios) 
    return respuesta

@app.route("/usuario", methods=['GET'])
def obtenerUnUsuario():
    global Usuarios
    envios =[]
    for usuario in Usuarios:
        if (usuario.getUsername() == request.json['username'] and usuario.getPassword() == request.json['password']):
            unEnvio = {
                "nombre": usuario.getNombre(),
                "edad": usuario.getEdad(),
                "username":usuario.getUsername(),
                "password":usuario.getPassword()
            }
            envios.append(unEnvio)
    respuesta = jsonify(envios) 
    return respuesta


@app.route("/usuarios", methods=['POST'])
def crearUsuario():
    global Usuarios
    nuevoUsuario = Usuario(request.json['nombre'],int(request.json['edad']), request.json['username'],request.json['password'])
    Usuarios.append(nuevoUsuario)
    respuesta = jsonify({"error":False, "mensaje": "Todo bien"})
    return (respuesta)

@app.route("/usuario/<string:username>/<string:password>", methods=['DELETE'])
def eliminarUsuario(username, password):
    global Usuarios
    envios =[]
    for posicion in range(len(Usuarios)):
        if (Usuarios[posicion].getUsername() == username and Usuarios[posicion].getPassword() == password):
            unEnvio = {
                "mensaje": "Se elimino el usuario",
            }
            del Usuarios[posicion]
            envios.append(unEnvio)
            break            
    respuesta = jsonify(envios) 
    return respuesta

@app.route("/usuario/<string:username>", methods=['PUT'])
def actualizarUsuario(username):
    global Usuarios
    envios =[]
    for posicion in range(len(Usuarios)):
        if (Usuarios[posicion].getUsername() == username):
            Usuarios[posicion].setNombre(request.json['nombre'])
            Usuarios[posicion].setEdad(request.json['edad'])
            Usuarios[posicion].setPassword(request.json['password'])
            unEnvio = {
                "mensaje": "Se actualizo el usuario",
            }
            envios.append(unEnvio)
            break            
    respuesta = jsonify(envios) 
    return respuesta

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)