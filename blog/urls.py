# standard to get url funcitonality from django
from django.conf.urls import url
# will get you all your views
from . import views

urlpatterns = [
	# starts at ^ and ends at $
	# created new view post_list and gave it a name to appear (can be different)
	url(r'^$', views.post_list, name='post_list'),
]