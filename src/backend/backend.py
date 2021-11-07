from flask import Flask,request,render_template,jsonify,flash
from flask_restful import Api,Resource,fields,marshal_with
from flask_cors import CORS
from pprint import pprint
import json
import os

app = Flask(__name__)
CORS(app)
api=Api(app)
@app.route('/')
def index():
    return str(0)
@app.route('/monster',methods=["GET"])
def monster():
    with open("src/backend/monsterdata.json","r",encoding="utf-8")as data:
        monster=json.load(data)
    return monster
@app.route('/monster',methods=["POST"])
def addmonster():
    data=request.get_json()
    name=data['param']['name']
    hp=data['param']['hp']
    bp=data['param']['bp']
    ability=data['param']['ability']
    monster=data['param']['data']
    print(type(monster))
    add={name:{"hp":hp,"bp":bp,"ability":ability}}
    monster.update(add)
    print(monster)
    with open("src/backend/monsterdata.json","w")as j_w:
        json.dump(monster,j_w)
    return str(0)
if __name__=="__main__":
    app.run()
