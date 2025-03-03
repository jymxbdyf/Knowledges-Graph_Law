# KGQA_LAW
小型法律知识图谱构建与应用

文件树:<br>
1)  app.py是整个系统的主入口<br>
2)  templates文件夹是HTML的页面<br>
     |-index.html 欢迎界面<br> 
     |-search.html 民诉法知识图谱-逻辑关系检索页面<br>
     |-jurisdiction_relation.html 民诉法知识图谱概览页面<br>
     |-query_path.html 民诉法知识图谱-具体路径查询页面<br>
     |-knowledges_relation.html 法考知识图谱概览页面<br>
     |-question.html 法考知识图谱-知识点与题目检索页面<br>
     |-add.html 节点生成器-增加节点与关系页面<br>
     |-add_search.html 节点生成器-新节点检索页面<br>
3)  static文件夹存放css，js和用于预加载的静态json文件，其中css和js是页面的样式和效果的文件<br>
4)  raw_data文件夹是获取到的数据处理后的csv文件<br>
5)  neo4j_db文件夹是知识图谱查询模块<br>
     |-config.py 配置参数<br>
     |-creat_graph_query.py 创建用于查询的图数据库<br>
     |-query_graph.py 知识图谱的查询<br>
6)  neo4j_echarts_json文件夹是知识图谱构建模块<br>
     |-creat_graph_json.py 创建用于生成json文件的图数据库<br>
     |-creat_jurisdiction_json.py 创建民诉法知识图谱json文件<br>
     |-creat_knowledges_json.py 创建法考知识图谱json文件<br>
7)  law_crawler文件夹是爬虫模块<br>
     |- ruler.py 是之前爬取觉晓法考网数据的代码，已经产生好csv 可以不用再执行<br>

<hr>

部署步骤：<br>
* 0.安装所需的库 执行pip install -r requirement.txt<br>
* 1.先下载好neo4j图数据库，并配好环境（注意neo4j需要jdk8）。修改neo4j_db目录下的配置文件config.py,设置图数据库的账号和密码。<br>
* 2.切换到neo4j_echarts_json目录下，执行python  creat_graph_json.py 分别建立民诉法和法考知识图谱（需要切换图数据库）<br>
* 3.逐一执行python  creat_jurisdiction_json.py和python  creat_knowledges_json.py创建前端组件echarts所需的json文件<br>
* 4.切换到neo4j_db目录下，执行creat_graph_query.py创建用于查询的图数据库<br>
* 5.运行python app.py,浏览器打开localhost:5000即可查看<br>

项目试用地址：http://121.36.99.152:5000/

系统整体流程图：

![img.png](img.png)

网站示例:<br>
欢迎界面

![img_1.png](img_1.png)

民诉法知识图谱-逻辑关系检索

![img_4.png](img_4.png)

民诉法知识图谱概览

![img_2.png](img_2.png)

民诉法知识图谱-具体路径检索

![img_3.png](img_3.png)

法考知识图谱概览

![img_5.png](img_5.png)

法考知识图谱知识点与题目检索

![img_6.png](img_6.png)

节点生成器-节点与关系增加页面

![img_7.png](img_7.png)

节点生成器-新节点检索页面

![img_8.png](img_8.png)



<hr>
