from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'create_at')
    inlines = [RecipeInline]


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'serves', 'prep_time', 'cook_time')


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
