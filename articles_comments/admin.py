from django.contrib import admin
from articles_comments.models import ArticleComment

class ArticleCommentAdmin:
    list_display = ('id', 'author')
    list_display_links = ('id', )
    search_fields = ('id', 'author')

admin.site.register(ArticleComment)
