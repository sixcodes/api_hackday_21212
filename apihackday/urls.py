from django.conf.urls import patterns, include, url
from tastypie.api import Api
from bolao.api import ApostadorResource, BolaoResource, ApostaResource

from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(ApostadorResource())
v1_api.register(BolaoResource())
v1_api.register(ApostaResource())

urlpatterns = patterns('',
    url(r'^$', 'bolao.views.home', name='home'),
    url(r'^bolao$', 'bolao.views.listarBolao', name='listarbolao'),
    url(r'^bolao/add', 'bolao.views.criarBolao', name='criarbolao'),
    url(r'^bolao/(?P<bolao>[\d]+)$', 'bolao.views.exibeBolao', name='exibebolao'),
    # url(r'^apihackday/', include('apihackday.foo.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^api/', include(v1_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
