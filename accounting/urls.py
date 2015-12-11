from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'accounting.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="base.html"), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^p2p_accounting/', include('p2p.urls')),
]
