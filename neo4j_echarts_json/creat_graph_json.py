from py2neo import Graph, Node, Relationship,NodeMatcher
from neo4j_db.config import graph
import os

os.chdir('C://Users/倾顾/PycharmProjects/KGQA_LAW-master')  # 改变编译器默认的当前工作目录，改成文件所在的位置

def creat_knowledges():
    with open('raw_data/knowledges.csv', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            rela_array=line.strip("\n").split(",")
            #print(rela_array)
            graph.run("merge (f1:law_exam{cate:'law_exam',name:'%s'})\
            merge (f2:sort_exam{cate:'sort_exam',name:'%s'})\
            merge (f3:classification{cate:'classification',name:'%s'})\
            merge (f4:knowledge_points{cate:'knowledge_points',name:'%s'})\
            merge (f1)-[r1:sort{relation:'sort',name:'%s'}]->(f2)\
            merge (f2)-[r2:chapter{relation:'chapter',name:'%s'}]->(f3)\
            merge (f3)-[r3:sort_knowledge{relation:'sort_knowledge',name:'%s'}]->(f4)\
            return count(*)"% (rela_array[0],rela_array[2],rela_array[4],rela_array[6],
                           rela_array[1],rela_array[3],rela_array[5]))
    print("用于生成json文件的法考知识图谱构建已完成")
    with open('raw_data/knowledges_question.csv', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            rela_array=line.strip("\n").split(",")
            #print(rela_array)
            graph.run("merge (f1:knowledge_points{cate:'knowledge_points',name:'%s'})\
            merge (f2:题目{cate:'题目',name:'%s'})\
            merge (f1)-[r1:question{relation:'题库',name:'%s'}]->(f2)\
            return count(*)"% (rela_array[0],rela_array[2],rela_array[1]))
    print("法考知识图谱构建已完成")
def creat_jurisdiction():
    with open('raw_data/Jurisdiction.csv', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            rela_array=line.strip("\n").split(",")
            #print(rela_array)
            graph.run("merge (f1:Theme{cate:'Theme',name:'%s'})\
            merge (f2:Form{cate:'Form',name:'%s'})\
            merge (f3:Resolution_Jurisdiction{cate:'Resolution_Jurisdiction',name:'%s'})\
            merge (f4:Case{cate:'Case',name:'%s'})\
            merge (f5:Details{cate:'Details',name:'%s'})\
            merge (f6:Court_Answer{cate:'Court_Answer',name:'%s'})\
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
            graph.run("merge (f1:Theme{cate:'Theme',name:'%s'})\
            merge (f2:Form{cate:'Form',name:'%s'})\
            merge (f3:Resolution_Jurisdiction{cate:'Resolution_Jurisdiction',name:'%s'})\
            merge (f1)-[r1:Form_Type{relation:'Form_Type',name:'%s'}]->(f2)\
            merge (f2)-[r2:Resolution_Type{relation:'Resolution_Type',name:'%s'}]->(f3)\
            return count(*)"% (rela_array[0],rela_array[2],rela_array[4],
                           rela_array[1],rela_array[3]))
    with open('raw_data/usual.csv', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            rela_array=line.strip("\n").split(",")
            #print(rela_array)
            graph.run("merge (f1:Court_Answer{cate:'Court_Answer',name:'%s'})\
            merge (f2:Answer{cate:'Answer',name:'%s'})\
            merge (f1)-[r1:Lead{relation:'Lead',name:'%s'}]->(f2)\
            return count(*)"% (rela_array[0],rela_array[2],
                           rela_array[1]))
    print("用于生成json文件的民诉法知识图谱构建已完成")
if __name__ == '__main__':
  # creat_knowledges()
   creat_jurisdiction()
   import os
   print(os.getcwd())  # 目前Python搜索的路径
   #print(os.getcwd())