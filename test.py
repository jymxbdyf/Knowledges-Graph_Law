from flask import Flask, render_template, request, jsonify
from neo4j_db.query_graph import query, user_creat_query
from gevent import pywsgi
import sys
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

@app.route('/index', methods=['GET', 'POST'])
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/add', methods=['GET', 'POST'])
def add():
    return render_template("add_test.html")

@app.route("/add/user", methods=["GET", "POST"])
def add_user():
    start = request.args.get('start')
    relation = request.args.get('relation')
    end = request.args.get('end')
    #print(start)
    #print(relation)
    #print(end)
    json_data=user_creat_query(str(start),str(relation), str(end))
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True,port=5000)

