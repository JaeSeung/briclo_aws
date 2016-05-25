from django.conf.urls import url, include
from home import views

urlpatterns = [
    url(r'^$', views.team_introduce, name="team_introduce"),
]