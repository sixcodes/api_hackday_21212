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
   url(r'^$', 'bolao.views.login', name='login'),
   url(r'^logout/$', 'bolao.views.logout_then_login' , name='logout'),
)

urlpatterns += patterns('',
    url(r'^home$', 'bolao.views.home', name='home'),
    url(r'^mail/?$', 'bolao.views.mail', name='mail'),
    url(r'^finalizar/$', 'bolao.views.finalizarBolao', name='finalizarbolao'),
    url(r'^criarUsuario/$', 'bolao.views.criarUsuario', name='criarUsuario'),
    url(r'^apostar/$', 'bolao.views.apostarBolao', name='apostarbolao'),
    url(r'^convidar/$', 'bolao.views.convidarBolao', name='convidarbolao'),
    url(r'^bolao/$', 'bolao.views.listarBolao', name='listarbolao'),
    url(r'^bolao/add', 'bolao.views.criarBolao', name='criarbolao'),
    url(r'^convidar/(?P<bolao_id>[\d]+)$', 'bolao.views.convidarBolao', name='convidar'),
    url(r'^bolao/exibir/$', 'bolao.views.exibirBolao', name='exibirbolao'),
    
    url(r'^bolao/(?P<id>[\d]+)$', 'bolao.views.exibirBolao', name='exibirbolao'),

    url(r'', include('social_auth.urls')),
    url(r'^api/', include(v1_api.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
