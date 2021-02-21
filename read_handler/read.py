from flask import Flask, request
import os
from flask import jsonify
from read_handler.read_event import *
app = Flask(__name__)

@app.route("/")
def hello():
    print('Hello World')
    return "Hello World!"


@app.route("/events",methods=['GET'])
def getEvents():
    print("GETEVENTS")
    print(a)
    #validate_Function()
    reObj = read_sql()
    query = reObj.prepare_query("",request.args['sDateTime'],request.args['eDateTime'])
    db_result = reObj.get_data(query)
    ret_obj = {'db_result':db_result}
    return jsonify(ret_obj)


