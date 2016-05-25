from django.conf.urls import url, include

from product import views

urlpatterns = [
    url(r'^$', views.product_list, name="product_list"),
    url(r'^top$', views.product_top_list, name="product_top_list"),
    url(r'^bottom$', views.product_bottom_list, name="product_bottom_list"),
    url(r'^(?P<pk>\d+)$', views.product_detail, name='product_detail'),
    url(r'^top/(?P<pk>\d+)$', views.product_top_detail, name='product_top_detail'),
    url(r'^bottom/(?P<pk>\d+)$', views.product_bottom_detail, name='product_bottom_detail'),
    #url(r'^(?P<next_pk>\d+)$', views.get_products, name='next-products'),
    url(r'^accounts/', include('accounts.urls')),
]