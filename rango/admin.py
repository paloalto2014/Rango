from django.contrib import admin
from rango.models import Category, Page


class PageInline(admin.TabularInline):
    model = Page
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','views','likes']
    list_filter = ['views','likes']
    search_fields = ['name']
    inlines = [PageInline]




class PageAdmin(admin.ModelAdmin):
    list_display = ['title','category','url','views']
    list_filter = ['views']
    search_fields = ['title','url']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)