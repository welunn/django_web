from django.db import models


# Create your models here.
class BookInfo(models.Model):
    # 定义书名
    title = models.CharField(max_length=50)
    # 定义作者 数据库可以为空， 后台管理校验可以为空
    author = models.CharField(max_length=50, null=True, blank=True)
    # 发布时间
    pub_date = models.DateTimeField()


    def __str__(self):
        return self.title


class HeroInfo(models.Model):
    # 英雄名称
    hname = models.CharField(max_length=50)
    # 性别 只有男女，可以通过choice属性设置选项
    hgender = models.CharField(max_length=1, choices=(("1", "男"), ("0", "女")))
    # 英雄简介 成名绝技
    hcontent = models.CharField(max_length=100, null=True, blank=True)
    # 英雄所属小说(书) 乔峰=>天龙八部
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)


    def __str__(self):
        return self.hname


# 实现一对一的关系
class Person(models.Model):
    username = models.CharField(max_length=20)
    gender = models.CharField(max_length=2, choices=(('1', '男'), ('0', '女')))


# 每个人的身份证号都是唯一的
class Card(models.Model):
    id_card = models.CharField(max_length=18)
    per = models.OneToOneField(Person, on_delete=models.CASCADE)


# 多对多关系 主机
class Host(models.Model):
    hostname = models.CharField(max_length=50)


# app应用
class Application(models.Model):
    appname = models.CharField(max_length=50)
    host = models.ManyToManyField(Host)


# 自定义管理类 集成Manager类
class TempManager(models.Manager):


    def findbyname(self, _name):
        return Temp.myobjects.all().first()


# 测试类
class Temp(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    addr = models.CharField(max_length=50, db_column="address", default="郑州", verbose_name="地址")

    myobjects = models.Manager()
    myObjects1 = TempManager()


# 创建区域类 省->市->区/县
class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

