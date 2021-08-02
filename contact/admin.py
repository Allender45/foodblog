from django.contrib import admin

from .models import ContactModel, ContactLink, About, Social, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at', )
    list_display_links = ('name', )


@admin.register(About)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'mini_text', )
    list_display_links = ('id', 'text', 'mini_text', )
    inlines = [ImageInline]


admin.site.register(ContactLink)
admin.site.register(Social)
admin.site.register(Image)