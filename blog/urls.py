


from unicodedata import name
from django.urls import path
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(),name = "post-detail-page") #/posts/my-first-blog
]
