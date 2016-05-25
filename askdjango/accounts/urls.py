from django.conf.urls import url
from . import views
from .forms import LoginForm
from django.contrib.auth.views import login, logout

urlpatterns= [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login', kwargs={'authentication_form': LoginForm, },
    	),
     url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={
    	'template_name':'accounts/login_form.html', 'next_page': '/'
    	}),

   #url(r'^login/$, 'login', name='login', kwargs={'template_name:'accounts/login_form.html',}),
    url(r'^profile/$', views.profile, name='profile'),]