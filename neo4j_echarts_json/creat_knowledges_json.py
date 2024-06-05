import codecs
import json
from py2neo import *
import neo4j_db.config
import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath("C://Users/倾顾/PycharmProjects/KGQA_LAW-master/static"))  # 把绝对路径加入到搜索路径
sys.path.insert(0, os.path.join(BASE_DIR))
sys.path.insert(0, os.path.join(BASE_DIR, 'data'))  # 把data所在的绝对路径加入到搜索路径
# 进行切换目录
os.chdir(BASE_DIR)   # 把目录切换到当前项目

graph = Graph('http://localhost:7474/', auth=('neo4j', '123456neo4j'))  # 连接数据库

def search_all_category():
    data = []  # 定义data数组，存放节点信息
    links = []  # 定义关系数组，存放节点间的关系
    # 节点分类
    node_juexiao_law = graph.run('MATCH (n:law_exam) RETURN n').data()
    node_sort_exam = graph.run('MATCH (n:sort_exam) RETURN n').data()
    node_classification = graph.run('MATCH (n:classification) RETURN n').data()
    node_knowledge_points = graph.run('MATCH (n:knowledge_points) RETURN n').data()
    '''
    node_question = graph.run('MATCH (n:question) RETURN n').data()
    node_options = graph.run('MATCH (n:options) RETURN n').data()
    node_analyze = graph.run('MATCH (n:analyze) RETURN n').data()
    '''
    i=0
    for n in node_juexiao_law:
        nodesStr = json.dumps(n, ensure_ascii=False)  # 将节点信息转化为json格式，否则中文会不显示
        node_name = json.loads(nodesStr)
        node_name = node_name['n']['name']  # 取出节点的name
        #node_id=node_name['n']['identity']
       # print(node_id)
        dict = {
            # 'id':str(n), # 防止重复节点
            'name': node_name,
            'symbolSize': 50,
            'category': 'juexiao_law',
            'index':i
        }
        data.append(dict)  # 将单个节点信息存放在data数组中
        i+=1
    for n in node_sort_exam:
        nodesStr = json.dumps(n, ensure_ascii=False)  # 将节点信息转化为json格式，否则中文会不显示
        node_name = json.loads(nodesStr)
        node_name = node_name['n']['name']  # 取出节点的name
        #print(node_name)
        dict = {
            # 'id':str(n), # 防止重复节点
            'name': node_name,
            'symbolSize': 50,
            'category': 'sort_exam',
            'index': i
        }
        data.append(dict)  # 将单个节点信息存放在data数组中
        i+=1
    for n in node_classification:
        nodesStr = json.dumps(n, ensure_ascii=False)  # 将节点信息转化为json格式，否则中文会不显示
        node_name = json.loads(nodesStr)
        node_name = node_name['n']['name']  # 取出节点的name
        #print(node_name)
        dict = {
            # 'id':str(n), # 防止重复节点
            'name': node_name,
            'symbolSize': 50,
            'category': 'classification',
            'index': i

        }
        data.append(dict)  # 将单个节点信息存放在data数组中
        i+=1
    for n in node_knowledge_points:
        nodesStr = json.dumps(n, ensure_ascii=False)  # 将节点信息转化为json格式，否则中文会不显示
        node_name = json.loads(nodesStr)
        node_name = node_name['n']['name']  # 取出节点的name
        #print(node_name)
        dict = {
            # 'id':str(n), # 防止重复节点
            'name': node_name,
            'symbolSize': 50,
            'category': 'knowledge_points',
            'index':i
        }
        data.append(dict)  # 将单个节点信息存放在data数组中
        i+=1
    # 查询所有关系，并将所有的关系信息存放在links数组中
    rps = graph.relationships
    for r in rps:
        #print(r)
        source = str(rps[r].start_node['name'])# 取出开始节点的name
        for i in data:  # 需要使用ID
            if source == i['name']:
                source = i['index']

        target = str(rps[r].end_node['name'])
        for j in data:  # 需要使用ID
            if target == j['name']:
                target = j['index']

       # name = str(type(rps[r]).__name__)  # 取出开始节点的结束节点之间的关系
        name = str(rps[r].get('name'))
        # 构造字典存储单个关系信息
        dict = {
            'source': source,
            'target': target,
            'value': name
        }
        links.append(dict)  # 将单个关系信息存放进links数组中
    neo4j_data = {
        'data': data,
        'links': links
    }
    neo4j_data = json.dumps(neo4j_data)
    return neo4j_data

if __name__ == '__main__':
     neo4j_data = search_all_category()
     #print(neo4j_data)
     # dbms.default_database=crawler.db
     # 法考知识点，用于图数据库的构建
     f = codecs.open('./static/knowledges.json', 'w', 'utf-8')
     f.write(neo4j_data)
     print("echarts所需的法考知识图谱json文件已生成")


