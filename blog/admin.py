from django.contrib import admin
from .models import Post
from django import forms


class PostModelForm( forms.ModelForm ):
    post_text = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Post
        fields = ['post_title', 'author', 'pub_date', 'post_text', 'published']

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	form = PostModelForm
	list_filter = ['pub_date']
	search_fields = ['post_title', 'post_text', 'author']
	list_display = ('post_title', 'author', 'pub_date', 'published')

admin.site.register(Post, PostAdmin)