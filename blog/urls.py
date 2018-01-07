from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^users/$',views.UserList.as_view(),name="users"),
	url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view(),name="users-detail"),
	url(r'^blogs/$',views.BlogList.as_view()),
	url(r'^blogs/(?P<pk>[0-9]+)/$',views.BlogDetail.as_view(),name="blogs-detail"),
	url(r'^api/login/$',views.LoginView.as_view()),
]