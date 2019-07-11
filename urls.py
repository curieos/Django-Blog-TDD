from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
<<<<<<< HEAD
	path("", views.IndexView.as_view(), name="index"),
	path("<int:year>/<int:month>/<slug:slug>", views.PostDetail.as_view(), name="post"),
	path("<slug:slug>", views.TagDetail.as_view(), name="tag")
=======
    path("", views.IndexView.as_view(), name="index"),
>>>>>>> 9004bf328deb9a9a4f46a19a888042c1dfcd492d
]
