"""
    views.py 主要是用来存放视图函数的，views.py名字不是固定的
    但是推荐大家使用 views.py

"""
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from . import db

def index(request):
    """
    系统首页
    :param request:
    :return:
    """

    return render(request, "index.html")


def epidemic(request):
    sql = """
           select r.name , ifnull(t.addCon, 0) addCon, ifnull(t.addDon, 0) addDon ,
           ifnull((select sum(f.addCon) 
               from t_epidemic f where f.region = r.name), 0) value
           from t_epidemic t  right join t_region r 
           on r.name = t.region and  DATE_FORMAT(epidemic_time , '%Y-%m-%d')
               = DATE_FORMAT(now() , '%Y-%m-%d')
       """
    # 执行SQL语句
    data = db.query_list(sql)
    # 将查询到的数据、传到 index.html 模板中，并在模板中进行数据的展示
    print(data)
    data = """
        [{'name': '湖北', 'addCon': 1600, 'addDon': 50000, 'value': Decimal('5000')}, {'name': '广东', 'addCon': 1000, 'addDon': 5000, 'value': Decim
al('1000')}, {'name': '浙江', 'addCon': 0, 'addDon': 0, 'value': Decimal('2000')}, {'name': '河南', 'addCon': 0, 'addDon': 0, 'valu
e': Decimal('0')}, {'name': '山东', 'addCon': 0, 'addDon': 0, 'value': Decimal('0')}, {'name': '北京', 'addCon': 0, 'addDon':
 0, 'value': Decimal('0')}, {'name': '湖南', 'addCon': 0, 'addDon': 0, 'value': Decimal('0')}]
 """
    print(data)
    return JsonResponse(data, safe=False)



def add(request):
    """
    直接跳转到 疫情收集页面
    :param request:
    :return:
    """
    return render(request, "epidemic_collect.html")



def add_epidemic(request):
    """
    视图中如果是处理业务逻辑
    :param request:
    :return:
    """
    # 1、接收 页面中 提交的 数据  request.POST 返回的是一个 QueryDict 对象
    data = request.POST.dict()

    # print(data)
        # 2、将接收到的数据、存储到数据库中
    sql = "insert into t_epidemic(region, addCon, addDon, epidemic_time) values (" \
          "%(region)s, %(addCon)s, %(addDon)s, now() )"

    # 执行SQL
    db.update(sql, args=data)

    # 3、做页面跳转
    return redirect(to="/index/")


