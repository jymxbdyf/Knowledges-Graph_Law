from flask import Flask, render_template, request, jsonify
from neo4j_db.query_graph import query, user_creat_query, query_path_neo
from gevent import pywsgi
import sys
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 获取当前文件的绝对路径
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')   # 从当前文件所在目录构建到templates的相对路径sys.path.insert(0, os.path.join(BASE_DIR))
sys.path.insert(0, os.path.join(BASE_DIR, 'data'))  # 把data所在的绝对路径加入到搜索路径
# 进行切换目录
os.chdir(BASE_DIR)  # 把目录切换到当前项目
#print(os.getcwd())  # 目前Python搜索路径



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    name = request.args.get('name')
    json_data = query(str(name))
    #return(json_data)
    return jsonify(json_data)

@app.route('/jurisdiction', methods=['GET', 'POST'])
def jurisdiction():
    return render_template('jurisdiction_relation.html')

@app.route('/knowledges', methods=['GET', 'POST'])
def knowledges():
    return render_template('knowledges_relation.html')

@app.route("/question", methods=["GET", "POST"])
def question():
        return render_template('question.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    return render_template("add.html")

@app.route("/add/user", methods=["GET", "POST"])
def add_user():
    start = request.args.get('start')
    relation = request.args.get('relation')
    end = request.args.get('end')
    json_data=user_creat_query(str(start),str(relation), str(end))
    return jsonify(json_data)

@app.route("/add_search", methods=["GET", "POST"])
def add_search():
    return render_template("add_search.html")

@app.route("/query_p", methods=["GET", "POST"])
def query_p():
        return render_template('query_path.html')

@app.route("/query_path", methods=["GET", "POST"])
def query_path():
    one = request.args.get('one')
    two= request.args.get('two')
    three = request.args.get('three')
    four = request.args.get('four')
    five = request.args.get('five')
    six =request.args.get("six")
    json_data=query_path_neo(str(one),str(two), str(three),str(four),str(five),str(six))
    return jsonify(json_data)


if __name__ == '__main__':
    app.debug=True
    app.run()
'''
if __name__ == '__main__':
    app.debug = True
   # print("Running on http://127.0.0.1:5000")
    server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
    server.serve_forever()
'''