from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from blog.models import Article
# Register your models here.

class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Article, ArticleAdmin)