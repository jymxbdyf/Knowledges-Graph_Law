# KGQA_LAW
小型法律知识图谱构建与应用

文件树:<br>
1)  app.py是整个系统的主入口<br>
2)  templates文件夹是HTML的页面<br>
     |-index.html 欢迎界面<br> 
     |-search.html 搜索民诉法逻辑关系或法考知识点页面<br>
     |-jurisdiction_relation.html 民诉法知识图谱页面<br>
     |-knowledges_relation.html 法考知识图谱页面<br>
     |-question.html 法考客观题知识点检索页面<br>
     |-add.html 增加节点与关系页面<br>
     |-query_path.html 民诉法知识图谱具体路径查询页面<br>
3)  static文件夹存放css，js和用于预加载的静态json文件，其中css和js是页面的样式和效果的文件<br>
4)  raw_data文件夹是获取到的数据处理后的csv文件<br>
5)  neo4j_db文件夹是知识图谱查询模块<br>
     |-config.py 配置参数<br>
     |-creat_graph_query.py 创建用于查询的图数据库<br>
     |-query_graph.py 知识图谱的查询<br>
6)  neo4j_echarts_json文件夹是知识图谱构建模块<br>
     |-creat_graph_json.py 创建用于生成json文件的图数据库<br>
     |-creat_jurisdiction_json.py 创建民诉法知识图谱<br>
     |-creat_knowledges_json.py 创建法考知识图谱<br>
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

系统整体流程图：

图片1.png

网站示例:<br>
欢迎界面

放一页index页面图

主界面

可以放五张系统展示图
<hr>

项目试用地址：http://121.36.99.152:5000/