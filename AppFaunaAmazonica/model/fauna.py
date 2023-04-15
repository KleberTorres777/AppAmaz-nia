import mongoengine
from pymongo import MongoClient
from model.especie import Especie

class Animal(mongoengine.Document):
    _id = mongoengine.SequenceField(required=True, primary_key=True)
nome_popular = mongoengine.StringField(default="")
classe = mongoengine.StringField(default="")
especies = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Especie), default=[Especie(nome="test", habitat="test habitat", alimentacao="test alimentacao")])
genero = mongoengine.StringField(default="")
ordem = mongoengine.StringField(default="")
familia = mongoengine.StringField(default="")

mongoengine.connect('animal_db')