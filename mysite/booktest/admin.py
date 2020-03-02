from django.contrib import admin
from .models import BookInfo, HeroInfo, AreaInfo


# 定义关联插入的类
class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 1


# 定制后台管理页面
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "pub_date")
    list_filter = ("title",)
    search_fields = ("title",)
    list_per_page = 2
    # 在保存主表的时候，同时关联插入子表的内容
    inlines = [HeroInfoInline]




class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ("hname", "hgender", "hcontent", "book")
    list_filter = ["hname"]
    search_fields = ["hname"]
    list_per_page = 2


# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(AreaInfo)
