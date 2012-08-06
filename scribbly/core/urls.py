from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns('customer.views',
    url(r'^login', "login", name="login"),
    url(r'^account/login', "login"),
    url(r'^logout', "logout", name="logout"),
    url(r'^account/$', "account", name="account"),
)

urlpatterns += patterns('product.views',
    url(r'^products', "products", name="products"),
)
