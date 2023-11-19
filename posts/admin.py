from django.contrib import admin
from .models import Post
import django.apps
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    login_template = 'admin/login.html'
    list_display = ('title', 'create_at', 'update_at', 'author')
    # fields = ('title', 'body')
    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'body',)
        }),
        ('Author Information', {
            'fields': ('author',)
        })
    )


class PostAdminSite(admin.AdminSite):
    site_header = "MY: Admin Panel"


post_site = PostAdminSite(name='PostAdmin')
post_site.register(Post, PostAdmin)

models = django.apps.apps.get_models()
for model in models:
    try:
        post_site.register(model)
    except admin.sites.AlreadyRegistered:
        pass