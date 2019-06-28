from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:year>/<int:month>/<slug:slug>", views.PostDetail.as_view(), name="post"),
]
