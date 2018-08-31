from django.conf.urls import url
from Service.views import server, vue_demo, AjaxServer,ServerAjax
urlpatterns = [
	url(r"^$", server),
	url(r'^(?P<page>\d+)/$', server),
	url(r'^vue_demo/$', vue_demo),
	url(r'^server_aj/$', ServerAjax),
	url(r'^ajax_server/$', AjaxServer),
	url(r'^ajax_server/(?P<page>\d+)/$', AjaxServer),
]