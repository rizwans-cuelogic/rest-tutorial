from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^users/$',views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view()),
	url(r'^blogs/$',views.BlogList.as_view()),
	url(r'^blogs/(?P<pk>[0-9]+)/$',views.BlogDetail.as_view()),
	url(r'^api/login/$',views.LoginView.as_view()),
]