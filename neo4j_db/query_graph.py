from neo4j_db.config import graph
import codecs
import os
import json
import base64
from py2neo import *

os.chdir('C://Users/倾顾/PycharmProjects/KGQA_LAW-master')  # 改变编译器默认的当前工作目录，改成文件所在的位置
def query(name):
    data = graph.run(
    "match(p )-[r]->(n:Entity{name:'%s'}) return  p.name,r.name,n.name,p.cate,n.cate\
        Union all\
    match(p:Entity {name:'%s'}) -[r]->(n) return p.name, r.name, n.name, p.cate, n.cate" % (name,name)
    )
    data = list(data)

    return get_json_data(data)
def get_json_data(data):
    json_data={'data':[],"links":[]}
    d=[]

    for i in data:
       # print(i["p.name"], i["r.relation"], i["n.name"], i["p.cate"], i["n.cate"])
        d.append(i['p.name']+"@"+i['p.cate'])
        d.append(i['n.name']+"@"+i['n.cate'])
        d=list(set(d))
    name_dict={}
    count=0
    for j in d:
        j_array=j.split("@")#设置分隔符
        data_item={}
        name_dict[j_array[0]]=count
        count+=1
        data_item['name']=j_array[0]
        data_item['category']=j_array[1]
        json_data['data'].append(data_item)
    for i in data:
   
        link_item = {}
        link_item['source'] = name_dict[i['p.name']]
        link_item['target'] = name_dict[i['n.name']]
        link_item['value'] = i['r.name']
        json_data['links'].append(link_item)
    #print(json_data)
    f = codecs.open('./static/test.json', 'w', 'utf-8')
    f.write(json.dumps(json_data, ensure_ascii=False))
    return json_data
def user_creat_query(start, relation, end):
    if start and end and relation:
        data=graph.run("merge (p:Entity{cate:'起始节点',name:'%s'})\
                        merge (n:Entity{cate:'指向节点',name:'%s'})\
                        merge (p)-[r:relation{name:'%s'}]->(n)\
                        return  p.name,r.name,n.name,p.cate,n.cate" % (start, end, relation))
        #data = graph.run(
        #    "match(p:Entity{name:'%s'})-[r:relation{name:'%s'}]->(n:Entity{name:'%s'}) return  p.name,r.name,n.name,p.cate,n.cate" % (
        #    start, relation, end))
        data = list(data)
        return get_json_data(data)

def query_path_neo(one,two,three,four,five,six):
    node_matcher = NodeMatcher(graph)#py2neo查询节点
    relationship_matcher = RelationshipMatcher(graph)#py2neo查询节点之间的关系
    data = []  # 定义data数组，存放节点信息
    links = []  # 定义关系数组，存放节点间的关系
    node =[] # 将传入的数据拼成数组
    if one: node.append(one)
    if two: node.append(two)
    if three: node.append(three)
    if four: node.append(four)
    if five: node.append(five)
    if six :node.append(six)
    #print(node)
    i = 0
    last = None#用于跟踪for循环的前一个元素
    for n in node:
        m = graph.run("MATCH (p:Entity{name:'%s'}) RETURN p"%(n)).data()#逐一查询节点信息
        nodesStr = json.dumps(m, ensure_ascii=False)  # 将节点信息转化为json格式，否则中文会不显示
        node_name = json.loads(nodesStr)
        node_name = node_name[0] # 取出节点的信息
        node_cate = node_name['p']['cate']#取出节点的分类信息
        dict = {
            'name': n,
            'symbolSize': 50,
            'category': node_cate,
            'index': i
        }
        data.append(dict)  # 将单个节点信息存放在data数组中
        #print(data)
        if last and n :#for循环进行到第二轮才开始查询节点之间的关系
            node1 = node_matcher.match("Entity").where(name=last).first()#上一个节点
            node2 = node_matcher.match("Entity").where(name=n).first()#当前节点
            rps = list(relationship_matcher.match((node1, node2), r_type=None))
            #print(rps)
            source = i-1
            target = i
            name = str(rps[0].get('name'))
            # 构造字典存储单个关系信息
            dict = {
                'source': source,
                'target': target,
                'value': name
            }
            links.append(dict)  # 将单个关系信息存放进links数组中
           # print(links)
        last=n #跟踪for循环的上一个元素
        i += 1
    #print(node[-1])
    node3=node[-1]#取出列表中最后一个元素
    node3 = node_matcher.match("Entity").where(name=node3).first()
    rps = list(relationship_matcher.match([node3], r_type=None))#查询传入的最后一个元素的关系
    #print(rps)
    j=i-1
    for r in range(len(rps)):#循环生成最后一个节点所有关系
        target_name = str(rps[r].end_node['name'])
        target_cate = str(rps[r].end_node['cate'])
        dict = {
            'name': target_name,
            'symbolSize': 50,
            'category': target_cate,
            'index': i
        }
        data.append(dict)
        name = str(rps[r].get('name'))
        dict = {
            'source': j,
            'target': i,
            'value': name
        }
        links.append(dict)
        i+=1
    neo4j_data = {
        'data': data,
        'links': links
    }
    #neo4j_data = json.dumps(neo4j_data)
    #print(neo4j_data)
    f = codecs.open('./static/test.json', 'w', 'utf-8')
    f.write(json.dumps(neo4j_data, ensure_ascii=False))
    return neo4j_data




