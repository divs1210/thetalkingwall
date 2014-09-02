from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from posts.models import Post

def index(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'posts/index.html', context)

def apost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/apost.html', {'post': post})
