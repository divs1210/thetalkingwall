from django.contrib import admin
from posts.models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['author', 'post_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]
    list_display = ('author', 'pub_date', 'post_text')
    list_filter = ['author', 'pub_date']
    search_fields = ['post_text', 'author']

admin.site.register(Post, PostAdmin)
