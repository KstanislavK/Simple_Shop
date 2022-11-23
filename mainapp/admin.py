from django.contrib import admin

from .models import CompanyList, PhoneNumList, ArticleList, FeedbackList


class PhoneNumInline(admin.TabularInline):
    model = PhoneNumList
    list_display = ('pk', 'phone_num')


@admin.register(CompanyList)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'email')
    list_display_links = ('title', 'address', 'email')
    inlines = (PhoneNumInline,)


@admin.register(ArticleList)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_display_links = ('pk', 'title')


@admin.register(FeedbackList)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email')
    list_display_links = ('pk', 'name', 'email')


