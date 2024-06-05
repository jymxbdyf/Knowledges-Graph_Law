from py2neo import Graph
graph = Graph(
    "http://localhost:7474",
    auth=("neo4j", "123456neo4j")
)
import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 这里保险的就是直接先把绝对路径加入到搜索路径
sys.path.insert(0, os.path.join(BASE_DIR))
sys.path.insert(0, os.path.join(BASE_DIR, 'data'))  # 把data所在的绝对路径加入到了搜索路径，这样也可以直接访问dataset.csv文件了

# 这句代码进行切换目录
os.chdir(BASE_DIR)   # 把目录切换到当前项目，这句话是关键

