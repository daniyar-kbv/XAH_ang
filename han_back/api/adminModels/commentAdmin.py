from django.contrib import admin


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'date_published', 'created_by', 'article')
    list_display_links = ('id', 'body', 'date_published', 'created_by', 'article')