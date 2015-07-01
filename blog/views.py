from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

# Create your views here.
def index(request):
	latest_post_list = Post.objects.filter(published=True).order_by('-pub_date')
	paginator = Paginator(latest_post_list, 5)

	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results
		posts = paginator.page(paginator.num_pages)

	context = {'posts': posts}
	return render(request, 'blog/index.html', context)

def detail(request, post_id):
	post = get_object_or_404(Post.objects.filter(published=True), pk=post_id)
	return render(request, 'blog/detail.html', {'post': post})