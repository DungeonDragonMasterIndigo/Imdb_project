
from flask_cors import CORS
from flask import Flask, jsonify, request
# from .entities.entity import Session, engine, Base
# from .entities.graph import Graph, GraphSchema
import json
from elasticsearch import Elasticsearch
import requests
from flask_restful import Resource, Api


#Creating a Flask application
app = Flask(__name__)
api = Api(app)
CORS(app)


# Elastic search implementation

base = 'http://localhost:9200/workers/worker'

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])



r = requests.get('http://localhost:9200')


class MoviesList(Resource):

    def get(self):

        doc = {
            'size': 10000,
            'query': {
                'match_all': {}
            }
        }
        res = es.search(index='workers', doc_type='worker', body=doc, scroll='1m')
        list=[]
        for doc in res['hits']['hits']:

            list.append(doc['_source'])

        #movies = es.search(index='workers', filter_path=['hits.hits._id', 'hits.hits._type'])

        return (list)

api.add_resource(MoviesList, '/movies')



# Postgres implementaion

# i = 1
# for i in range(5):
#     r = requests.get('http://www.omdbapi.com/?i=tt000000'+str(i)+'&apikey=7e6ea2a7')
#
#     es.index(index='movies', doc_type='movie', id=i, body=json.loads(r.content.decode('utf-8')))
#     i = i + 1
#
#     #print(r.content.decode('utf-8'))
#
#
#
# print (es.get(index='movies', doc_type='movie', id=1))




# generate database schema
# Base.metadata.create_all(engine)


# @app.route("/graphs")
#
#
# def get_graphs():
#     # get from database
#     session = Session()
#     graph_objects = session.query(Graph).all()
#
#
#     #Transform it so that it can be serialised as a JSON onject
#     schema = GraphSchema(many=True)
#     graphs = schema.dump(graph_objects)
#
#     #Serializing as JSON
#     session.close()
#     return jsonify(graphs.data)
#
#
# @app.route('/graphs', methods=['POST'])
#
#
# def add_graph():
#     #add a graph object
#
#     posted_graph = GraphSchema(only=('title', 'description'))\
#         .load(request.get_json())
#     graph = Graph(**posted_graph.data, created_by="HTTP post request")
#
#
#     # persist graph
#     session = Session()
#     session.add(graph)
#     session.commit()
#
#
#     #return created graph data
#
#     new_graph = GraphSchema().dump(graph).data
#     session.close()
#     return jsonify(new_graph), 201


# start session
# check for existing data
# if len(graphs) == 0:
#     # create and persist dummy graph stuff
#     python_graph = Graph("01", "The best Graph", "It is the best of all graphs")
#     session.add(python_graph)
#
#
#
#     # reload exams
#     exams = session.query(Graph).all()
#
# # show existing exams
# print('Basic stuff:')
# for graph in graphs:
#     print(graph.id, graph.title, graph.description, )
#     session.delete(graph)
#
# session.commit()
# session.close()

#docker run --name online-graph-db \
#    -e POSTGRES_PASSWORD=bozhka \
#    -e POSTGRES_USER=hassan \
#    -e POSTGRES_DB=online-graph \
#    -p 5432:5432 \
#    -d postgres
