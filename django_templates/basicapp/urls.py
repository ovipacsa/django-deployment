from django.conf.urls import url
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    url(r'^url_templates/$',views.url_templates,name='url_templates'),
    url(r'^other/$',views.other,name='other'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$', views.user_login, name="user_login"),

]
