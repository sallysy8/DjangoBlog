from django.contrib import admin

# Register your models here.
# a new import
from blogging.models import Post, Category


class CategoryInline(admin.StackedInline):
    model = Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
