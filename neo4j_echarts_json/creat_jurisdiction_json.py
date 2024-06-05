import codecs
import json
from py2neo import *
import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath("C://Users/倾顾/PycharmProjects/KGQA_LAW-master/raw_data"))  # 把绝对路径加入到搜索路径
sys.path.insert(0, os.path.join(BASE_DIR))
sys.path.insert(0, os.path.join(BASE_DIR, 'data'))  # 把data所在的绝对路径加入到搜索路径
# 进行切换目录
os.chdir(BASE_DIR)   # 把目录切换到当前项目

graph = Graph('http://localhost:7474/', auth=('neo4j', '123456neo4j'))  # 连接数据库

def search_all_category():
    data = []  # 定义data数组，存放节点信息
    links = []  # 定义关系数组，存放节点间的关系
    # 节点分类
    node_Theme = graph.run('MATCH (n:Theme) RETURN n').data()
    node_Form = graph.run('MATCH (n:Form) RETURN n').data()
    node_Resolution_Jurisdiction = graph.run('MATCH (n:Resolution_Jurisdiction) RETURN n').data()
    node_Case = graph.run('MATCH (n:Case) RETURN n').data()
    node_Details = graph.run('MATCH (n:Details) RETURN n').data()
    node_Court_Answer = graph.run('MATCH (n:Court_Answer) RETURN n').data()
    i=0
    '''
    cql = "match (c:主管与管辖) where c.con_id='%s' return c "
    for r in graph.run(cql).data():
        node_ = r['c']  # 返回的是node
        node_id = node_.identity
        print(node_id)
    '''
    for n in node_Theme:
        nodesStr = json.dumps(n, ensure_ascii=False)  # 将节点信息转化为json格式，否则中文会不显示
        node_name = json.loads(nodesStr)
        node_name = node_name['n']['name']  # 取出节点的name
        #node_id=node_name['n']['identity']
       # print(node_id)
        dict = {
            # 'id':str(n), # 防止重复节点
            'name': node_name,
            'symbolSize': 50,
            'category': 'Theme',
            'index':i
        }
        data.append(dict)  # 将单个节点信息存放在data数组中
        i+=1
    for n in node_Form:
        nodesStr = json.dumps(n, ensure_ascii=False)  # 将节点信息转化为json格式，否则中文会不显示
        node_name = json.loads(nodesStr)
        node_name = node_name['n']['name']  # 取出节点的name
        #print(node_name)
        dict = {
            # 'id':str(n), # 防止重复节点
            'name': node_name,
            'symbolSize': 50,
            'category': 'Form',
            'index': i
        }
        data.append(dict)  # 将单个节点信息存放在data数组中
        i+=1
    for n in node_Resolution_Jurisdiction:
        nodesStr = json.dumps(n, ensure_ascii=False)  # 将节点信息转化为json格式，否则中文会不显示
        node_name = json.loads(nodesStr)
        node_name = node_name['n']['name']  # 取出节点的name
        #print(node_name)
        dict = {
            # 'id':str(n), # 防止重复节点
            'name': node_name,
            'symbolSize': 50,
            'category': 'Resolution_Jurisdiction',
            'index': i

        }
        data.append(dict)  # 将单个节点信息存放在data数组中
        i+=1
    for n in node_Case:
        nodesStr = json.dumps(n, ensure_ascii=False)  # 将节点信息转化为json格式，否则中文会不显示
        node_name = json.loads(nodesStr)
        node_name = node_name['n']['name']  # 取出节点的name
        #print(node_name)
        dict = {
            # 'id':str(n), # 防止重复节点
            'name': node_name,
            'symbolSize': 50,
            'category': 'Case',
            'index':i
        }
        data.append(dict)  # 将单个节点信息存放在data数组中
        i+=1
    for n in node_Details:
        nodesStr = json.dumps(n, ensure_ascii=False)  # 将节点信息转化为json格式，否则中文会不显示
        node_name = json.loads(nodesStr)
        node_name = node_name['n']['name']  # 取出节点的name
        #print(node_name)
        dict = {
            # 'id':str(n), # 防止重复节点
            'name': node_name,
            'symbolSize': 50,
            'category': 'Details',
            'index': i
        }
        data.append(dict)  # 将单个节点信息存放在data数组中
        i+=1
    for n in node_Court_Answer:
        nodesStr = json.dumps(n, ensure_ascii=False)  # 将节点信息转化为json格式，否则中文会不显示
        node_name = json.loads(nodesStr)
        node_name = node_name['n']['name']  # 取出节点的name
        #print(node_name)
        dict = {
            # 'id':str(n), # 防止重复节点
            'name': node_name,
            'symbolSize': 50,
            'category': 'Court_Answer',
            'index': i

        }
        data.append(dict)  # 将单个节点信息存放在data数组中
        i+=1
    # 查询所有关系，并将所有的关系信息存放在links数组中
    rps = graph.relationships
    #print(rps)
    for r in rps:
       # print(rps[r])
        source = str(rps[r].start_node['name'])# 取出开始节点的name
        for i in data:  # 需要使用ID
            if source == i['name']:
                source = i['index']

        target = str(rps[r].end_node['name'])
        for j in data:  # 需要使用ID
            if target == j['name']:
                target = j['index']

       # name = str(type(rps[r]).__name__)  # 取出开始节点的结束节点之间的关系
        name=str(rps[r].get('name'))
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
     # dbms.default_database=neo4j
     # 主管与管辖，用于图数据库的构建
     f = codecs.open('./static/jurisdiction.json', 'w', 'utf-8')
     f.write(neo4j_data)
     print("echarts所需的民诉法知识图谱json文件已生成")
