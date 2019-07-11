from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
<<<<<<< HEAD

from .models import Post, Tag

class IndexView(generic.ListView):
	template_name = "blog/index.html"
	context_object_name = "post_list"

	def get_queryset(self):
		return Post.objects.order_by("-date_created")[:6]

class PostDetail(generic.DetailView):
	model = Post
	template_name = "blog/post.html"
	context_object_name = "post"


class TagDetail(generic.DetailView):
	model = Tag
	template_name = "blog/tag.html"
	context_object_name = "tag"

=======

from .models import Post

class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "post_list"

    def get_queryset(self):
        return Post.objects.order_by("-date_created")[:6]
>>>>>>> 9004bf328deb9a9a4f46a19a888042c1dfcd492d
