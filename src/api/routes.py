"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User,Favoritos,Planetas,Personajes
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
import json

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

@api.route('/people', methods=['GET'])
def getpeople():
    personajes=Personajes.query.all()
    if personajes==[]:
        return jsonify({"msg":"no existen personajes"})
    results=list(map(lambda item:item.serialize(),personajes))
    return jsonify(results),200

@api.route('/planetas', methods=['GET'])
def getplanetas():
    planetas=Planetas.query.all()
    if planetas==[]:
        return jsonify({"msg":"no existen planetas"})
    results=list(map(lambda item:item.serialize(),planetas))
    return jsonify(results),200

@api.route('/user', methods=['GET','POST'])
def getusuario():
    if request.method=='GET':
        usuario=User.query.all()
        if usuario==[]:
            return jsonify({"msg":"no existen usuarios"})
        results=list(map(lambda item:item.serialize(),usuario))
        return jsonify(results),200
    if request.method=='POST':
        body=json.loads(request.data)
        usuario=User.query.filter_by(email=body["email"]).first()
        if usuario is None:
            nuevo_usuario=User(
                email=body["email"],
                password=body["password"]
            )
            db.session.add(nuevo_usuario)
            db.session.commit()
            return jsonify({"msg":"usuario creado"})
        return jsonify({"msg":"ya existe usuario"})
        




@api.route('/planetas/<int:id>', methods=['GET'])
def getplanet_by_id(id):
    planetas=Planetas.query.filter_by(id=id).first()
    if planetas is None:
        return jsonify({"msg":"no existen planetas"})
    return jsonify(planetas.serialize()),200

@api.route('/people/<int:id>', methods=['GET'])
def getpersonaje_by_id(id):
    personajes=Personajes.query.filter_by(id=id).first()
    if personajes is None:
        return jsonify({"msg":"no existen personajes"})
    return jsonify(personajes.serialize()),200

@api.route('/user/<int:id>', methods=['GET'])
def getusuario_by_id(id):
    usuario=User.query.filter_by(id=id).first()
    if usuario is None:
        return jsonify({"msg":"no existen usuarios"})
    return jsonify(usuario.serialize()),200

@api.route('/favoritos/planetas/<int:id>', methods=['POST','DELETE'])
def postplanet_by_id(id):
    body=json.loads(request.data)

    planetas=Planetas.query.filter_by(id=id).first()
    if planetas is None:
        return jsonify({"msg":"no existen planetas"})
    
    usuario=User.query.filter_by(id=body["user_id"]).first()
    if usuario is None:
        return jsonify({"msg":"no existen usuarios"})
    
    if request.method=='POST':
        nuevo_favorito=Favoritos(
            planetas_id=id,
            user_id=body["user_id"]
        )
        db.session.add(nuevo_favorito)
        db.session.commit()
        return jsonify({"msg":"favorito creado"})
    
    if request.method=='DELETE':
        db.session.delete(planetas)
        db.session.commit()
        return jsonify({"msg":"favorito borrado"})

@api.route('/favoritos/people/<int:id>', methods=['POST','DELETE'])
def postpersonajes_by_id(id):
    body=json.loads(request.data)

    personajes=Personajes.query.filter_by(id=id).first()
    if personajes is None:
        return jsonify({"msg":"no existen personajes"})
    
    usuario=User.query.filter_by(id=body["user_id"]).first()
    if usuario is None:
        return jsonify({"msg":"no existen usuarios"})
    
    if request.method=='POST':
        nuevo_favorito=Favoritos(
            personajes_id=id,
            user_id=body["user_id"]
        )
        db.session.add(nuevo_favorito)
        db.session.commit()
        return jsonify({"msg":"favorito creado"})
    
    if request.method=='DELETE':
        db.session.delete(personajes)
        db.session.commit()
        return jsonify({"msg":"favorito borrado"})

@api.route('/favoritos/user/<int:id_usuario>', methods=['GET'])
def get_favoritos(id_usuario):
    favoritos=Favoritos.query.filter_by(user_id=id_usuario).all()
    if favoritos==[]:
        return jsonify({"msg":"no existen favoritos"})
    results=list(map(lambda item:item.serialize(),favoritos))
    return jsonify(results),200



    



    

