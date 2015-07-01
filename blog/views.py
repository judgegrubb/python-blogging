from django.shortcuts import get_object_or_404, render

from .models import Post

# Create your views here.
def index(request):
	latest_post_list = Post.objects.filter(published=True).order_by('-pub_date')[:5]
	context = {'latest_post_list': latest_post_list}
	return render(request, 'blog/index.html', context)

def detail(request, post_id):
	post = get_object_or_404(Post.objects.filter(published=True), pk=post_id)
	return render(request, 'blog/detail.html', {'post': post})