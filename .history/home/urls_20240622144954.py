from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [ 

    path('', views.login, name='login'),
    path('redirecionar_para_login/', views.redirecionar_para_login, name='redirecionar_para_login'),
    ###########################
    ###########################
    path('webhook/', views.webhook_handler, name='webhook_handler'),
    ###########################
    ###########################
    path('sele_pais/', views.sele_pais, name='sele_pais'),
    path('pais/', views.pais, name='pais'),
    path('redirecionar_para_pais/', views.redirecionar_para_pais, name='redirecionar_para_pais'),
    ###########################
    ###########################
    path('indice/', views.indice, name='indice'),
    path('redirecionar_para_indice/', views.redirecionar_para_indice, name='redirecionar_para_indice'),
    ###########################
    ###########################
    path('sele_nicho/', views.sele_nicho, name='sele_nicho'),
    path('nicho/', views.nicho, name='nicho'),
    path('redirecionar_para_nicho/', views.redirecionar_para_nicho, name='redirecionar_para_nicho'),
    ###########################
    ###########################
    path('acessos/', views.acessos, name='acessos'),
    path('redirecionar_para_acessos/', views.redirecionar_para_acessos, name='redirecionar_para_acessos'),
    ###########################
    ###########################
    path('validacao/', views.validacao, name='validacao'),
    path('redirecionar_para_validacao/', views.redirecionar_para_validacao, name='redirecionar_para_validacao'),
    ###########################
    ###########################
    path('verificando/', views.verificando, name='verificando'),
    path('redirecionar_para_verificando/', views.redirecionar_para_verificando, name='redirecionar_para_verificando'),
    ###########################
    ###########################
    path('ver_conta/', views.ver_conta, name='ver_conta'),
    ###########################
    ###########################
    path('prefer/', views.prefer, name='prefer'),
    path('redirecionar_para_prefer/', views.redirecionar_para_prefer, name='redirecionar_para_prefer'),
    ###########################
    ###########################
    path('aguarde/', views.aguarde, name='aguarde'),
    path('redirecionar_para_aguarde/', views.redirecionar_para_aguarde, name='redirecionar_para_aguarde'),
    path('tema/', views.tema, name='tema'),
    ###########################
    ###########################
    path('dsers/', views.dsers, name='dsers'),
    path('redirecionar_para_dsers/', views.redirecionar_para_dsers, name='redirecionar_para_dsers'),
    ###########################
    ###########################
    path('produzir/', views.produzir, name='produzir'),
    path('redirecionar_para_produzir/', views.redirecionar_para_produzir, name='redirecionar_para_produzir'),
    ###########################
    ###########################
    path('lojapronta/', views.lojapronta, name='lojapronta'),
    path('redirecionar_para_lojapronta/', views.redirecionar_para_lojapronta, name='redirecionar_para_lojapronta'),
    ###########################
    ############################
    path('modal/', views.modal, name='modal'),
    path('redirecionar_para_modal/', views.redirecionar_para_modal, name='redirecionar_para_modal'),
    path('modal2/', views.modal2, name='modal2'),
    path('modal3/', views.modal3, name='modal3'),
    path('modal4/', views.modal4, name='modal4'),
     path('modal5/', views.modal4, name='modal5'),
    path('redirecionar_para_modal4/', views.redirecionar_para_modal4, name='redirecionar_para_modal4'),
    ###########################
    ###########################
    path('pagina_erro/', views.pagina_erro, name='pagina_erro'),
    path('redirecionar_para_pagina_erro/', views.redirecionar_para_pagina_erro, name='redirecionar_para_pagina_erro'),
    path('teste/', views.teste, name='teste'),
    path('teste3/', views.teste3, name='teste3'),
    path('retor/', views.retor, name='retor'),
    path('redirecionar_para_retor/', views.redirecionar_para_retor, name='redirecionar_para_retor'),

    ###########################
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)