from django.contrib import admin

# Register your models here.
from .models import SignUp
from .forms import SignUpForm

from .models import Article

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm

admin.site.register(SignUp, SignUpAdmin)


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'create_date' , 'updated']
    ordering = ['title']
    actions = [make_published]

admin.site.register(Article, ArticleAdmin)
