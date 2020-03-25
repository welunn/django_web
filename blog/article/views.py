from django.shortcuts import render, redirect, reverse ,get_object_or_404
from django.views import View
from .models import *
from comments.forms import CommentForm
from comments.models import Comment
from django.core.paginator import Paginator
import markdown
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from blog import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


# Create your views here.
class IndexView(View):
    def get(self, request):
        articles = Article.objects.all()
        # print(articles)
        # 对结果列表进行分页，每页2条数据
        # paginator = Paginator(articles, 2)
        # # 统计总共有多少条记录
        # print(paginator.count)
        # # 获取分页对象中的数据列表
        # print(paginator.object_list)
        # # 获取总页数
        # print(paginator.num_pages)
        # # 获取总页数从1 到 3
        # print(paginator.page_range)
        # # 获取第一页的文章
        # page = paginator.get_page(2)
        # print(page.object_list)
        # # 通过page 对象获取分页对象
        # print(paginator is page.paginator)
        # print(page.number)
        paginator = Paginator(articles, 2)
        pagenum = request.GET.get("pagenum")
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        return render(request, "article/index.html", {"page": page})


class SingeView(View):
    def get(self, request, id):
        articles = Article.objects.all()[:5]
        article = get_object_or_404(Article, pk=id)
        print(article.comment_set.count())
        cf = CommentForm()
        # 处理点击阅读次数
        article.views += 1
        article.save()
        # 实例化markdown对象
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ])
        # 使用markdown渲染制定的字段
        article.body = md.convert(article.body)
        article.toc = md.toc

        return render(request, "article/single.html", locals())


    def post(self, request, id):
        name = request.POST.get("name")
        email = request.POST.get("email")
        url = request.POST.get("url")
        content = request.POST.get("content")
        comment = Comment()
        comment.name = name
        comment.email = email
        comment.url = url
        comment.content = content
        comment.article = get_object_or_404(Article, pk=id)
        comment.save()
        return redirect(reverse("article:single", args=(id,)))


class ArticleView(View):
    def get(self, request, year, month):
        articles = Article.objects.all().filter(create_time__year=year, create_time__month=month)
        paginator = Paginator(articles, 2)
        pagenum = request.GET.get("pagenum")
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        return render(request, "article/index.html", {"page": page})


class CategoryView(View):
    def get(self, request, id):
        category = get_object_or_404(Category, pk=id)
        articles = category.article_set.all()
        paginator = Paginator(articles, 2)
        pagenum = request.GET.get("pagenum")
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        return render(request, "article/index.html", {"page": page})


class TagView(View):
    def get(self, request, id):
        tag = get_object_or_404(Tags, pk=id)
        articles = tag.article_set.all()
        paginator = Paginator(articles, 2)
        pagenum = request.GET.get("pagenum")
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        return render(request, "article/index.html", {"page": page})


class ContactView(View):
    def get(self, request):
        return render(request, "article/contact.html", locals())


    def post(self, request):
        info = MessageInfo()
        info.username = request.POST["username"]
        info.email = request.POST["email"]
        info.subject = request.POST["subject"]
        info.message = request.POST["message"]
        info.save()
        msg = "提交成功！"
        return render(request, "article/contact.html", locals())


class SendMailView(View):
    def get(self, request):
        # send_mail("邮件测试", "邮件正文", settings.DEFAULT_FROM_EMAIL, ["welun521@163.com","36077155@qq.com"])

        return render(request, "article/mail.html")


    def post(self, request):
        """
        获取页面上传输的邮件信息
        :param request:
        :return:
        """
        try:
            toAddr = request.POST["toEmail"]
            subject = request.POST["subject"]
            content = request.POST["content"]

            # 创建邮件发送对象
            # send_mail(subject, content, settings.EMAIL_FROM, [toAddr])

            userid = 1
            # 发送邮件给用户用于激活账户
            print(userid)
            print(settings.SECRET_KEY)
            # 创建加密工具
            util = Serializer(secret_key=settings.SECRET_KEY, )
            userid = util.dumps({"userid": userid}).decode("utf-8")
            body = "<a href='http://127.0.0.1:8000/article/active/%s/'>点击激活账号</a>" % (userid,)
            mail = EmailMultiAlternatives(subject, body, settings.DEFAULT_FROM_EMAIL, [toAddr])
            mail.content_subtype = "html"
            mail.send()


            # mail = EmailMultiAlternatives(subject, content, settings.DEFAULT_FROM_EMAIL, [toAddr])
            # mail.content_subtype = "html"
            # mail.send()
            msg = "发送成功！"
            return render(request, "article/mail.html", locals())
        except:
            msg = "发送失败！"
            return render(request, "article/mail.html", locals())


class ActiveView(View):
    def get(self, request, id):
        util = Serializer(secret_key=settings.SECRET_KEY,)
        obj = util.loads(id)
        userid = obj["userid"]
        print(userid)
        msg = "激活成功！被激活的id是：%s"%(userid,)
        return render(request, "article/mail.html", locals())