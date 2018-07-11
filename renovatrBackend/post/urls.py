from django.urls import include, path, re_path
from post.views import(
	PostCreateView,
	PostDetailView,
	PostDeleteView,
	PostListView,
	PostUpdateView,	
)

urlpatterns = [
    re_path(r'^$', PostListView.as_view(), name="List"),
    re_path(r'^create', PostCreateView.as_view(), name="Create"),
    re_path(r'^detail/(?P<pk>[\d-]+)/$', PostDetailView.as_view(),name = "Details"),
    re_path(r'update/(?P<pk>[\d-]_)/$', PostUpdateView.as_view(), name="Update"),
    re_path(r'^delete/(?P<pk>[\d]+)/$', PostDeleteView.as_view(), name="Delete")
]