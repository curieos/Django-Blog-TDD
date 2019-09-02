from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Post, Tag

class IndexView(generic.ListView):
	template_name = "blog/index.html"
	context_object_name = "post_list"

	def get_queryset(self):
		return Post.objects.order_by("-date_created")

class PostDetail(generic.DetailView):
	model = Post
	template_name = "blog/post.html"
	context_object_name = "post"


class TagDetail(generic.DetailView):
	model = Tag
	template_name = "blog/tag.html"
	context_object_name = "tag"

