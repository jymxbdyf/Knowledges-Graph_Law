from py2neo import Graph, Node, Relationship,NodeMatcher
from config import graph
import os
# print(os.getcwd())  # 目前Python搜索的路径
os.chdir('C://Users/倾顾/PycharmProjects/KGQA_LAW-master')  # 改变编译器默认的当前工作目录，改成文件所在的位置

def creat_jurisdiction_query():
    with open('raw_data/Jurisdiction.csv', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            rela_array=line.strip("\n").split(",")
            #print(rela_array)
            graph.run("merge (f1:Entity{cate:'Theme',name:'%s'})\
            merge (f2:Entity{cate:'Form',name:'%s'})\
            merge (f3:Entity{cate:'Resolution_Jurisdiction',name:'%s'})\
            merge (f4:Entity{cate:'Case',name:'%s'})\
            merge (f5:Entity{cate:'Details',name:'%s'})\
            merge (f6:Entity{cate:'Court_Answer',name:'%s'})\
            merge (f1)-[r1:Form_Type{relation:'Form_Type',name:'%s'}]->(f2)\
            merge (f2)-[r2:Resolution_Type{relation:'Resolution_Type',name:'%s'}]->(f3)\
            merge (f3)-[r3:Case_Type{relation:'Case_Type',name:'%s'}]->(f4)\
            merge (f4)-[r4:Details_Type{relation:'Details_Type',name:'%s'}]->(f5)\
            merge (f5)-[r5:Lead_to_answer{relation:'Lead_to_answer',name:'%s'}]->(f6)\
            return count(*)"% (rela_array[0],rela_array[2],rela_array[4],rela_array[6],rela_array[8],rela_array[10],
                           rela_array[1],rela_array[3],rela_array[5],rela_array[7],rela_array[9]))
    with open('raw_data/Jurisdiction1.csv', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            rela_array=line.strip("\n").split(",")
            #print(rela_array)
            graph.run("merge (f1:Entity{cate:'Theme',name:'%s'})\
            merge (f2:Entity{cate:'Form',name:'%s'})\
            merge (f3:Entity{cate:'Resolution_Jurisdiction',name:'%s'})\
            merge (f1)-[r1:Form_Type{relation:'Form_Type',name:'%s'}]->(f2)\
            merge (f2)-[r2:Resolution_Type{relation:'Resolution_Type',name:'%s'}]->(f3)\
            return count(*)"% (rela_array[0],rela_array[2],rela_array[4],
                           rela_array[1],rela_array[3]))
    with open('raw_data/usual.csv', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            rela_array=line.strip("\n").split(",")
            #print(rela_array)
            graph.run("merge (f1:Entity{cate:'Court_Answer',name:'%s'})\
            merge (f2:Entity{cate:'Answer',name:'%s'})\
            merge (f1)-[r1:Lead{relation:'Lead',name:'%s'}]->(f2)\
            return count(*)"% (rela_array[0],rela_array[2],
                           rela_array[1]))
    print("民诉法知识图谱构建已完成")

def creat_knowledges_query():
    with open('raw_data/knowledges.csv', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            rela_array=line.strip("\n").split(",")
            #print(rela_array)
            graph.run("merge (f1:Entity{cate:'law_exam',name:'%s'})\
            merge (f2:Entity{cate:'sort_exam',name:'%s'})\
            merge (f3:Entity{cate:'classification',name:'%s'})\
            merge (f4:Entity{cate:'knowledge_points',name:'%s'})\
            merge (f1)-[r1:sort{relation:'sort',name:'%s'}]->(f2)\
            merge (f2)-[r2:classify{relation:'classify',name:'%s'}]->(f3)\
            merge (f3)-[r3:sort_knowledge{relation:'sort_knowledge',name:'%s'}]->(f4)\
            return count(*)"% (rela_array[0],rela_array[2],rela_array[4],rela_array[6],
                           rela_array[1],rela_array[3],rela_array[5]))
    print("法考知识图谱构建已完成")
def creat_knowledges():
    graph.run("load csv with headers from 'file:///knowledges_question.csv'\
    as row\
    merge (f1:Entity{cate:'knowledge_points',name:row.f1})\
    merge (f2:Entity{cate:'题目',name:row.f2})\
    merge (f1)-[r1:question{relation:'题库',name:row.r1}]->(f2)\
    return count(*)")
    print("法考知识图谱-题库构建已完成")
if __name__ == '__main__':
    creat_knowledges()
    #creat_jurisdiction_query()
    #creat_knowledges_query()
    #print(os.getcwd())