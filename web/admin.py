from django.contrib import admin

# Register your models here.

from .models import BlogPost ,boxform
from .models import Contact,gallery_photo,FormMessage,EmailMessage,Subscribe
from .models import Comment,Tag,ReceptPost,Category



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

# @admin.register(BlogPost)
# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'pub_date')
#     filter_horizontal = ('tags',)

# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# admin.site.register(BlogPost)
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'pub_date',)
    list_filter = ('name',)
    search_fields = ('title', 'content',)
admin.site.register(Contact)


admin.site.register(gallery_photo)
admin.site.register(FormMessage)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'created_at')
    search_fields = ('author', 'email', 'comment')

admin.site.register(boxform)
admin.site.register(EmailMessage)

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    pass

admin.site.register(ReceptPost)