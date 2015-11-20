from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('sapps.apps.market.views',
		url(r'^$','principal_view',name = 'vista_principal'),
		url(r'^app/(?P<id_app>.*)/$', 'aplicacion_view', name = 'vista_aplicacion'),
		url(r'^juegos/$', 'juegos_view', name = 'vista_juegos'),
		url(r'^aplicaciones/$', 'aplicaciones_view', name = 'vista_aplicaciones'),
		
		#url(r'^add/producto/$','add_product_view',name = 'vista_agregar_producto'),
		#url(r'^edit/producto/(?P<id_prod>.*)/$', 'edit_product_view', name = 'vista_editar_producto'),
		#url(r'^del/producto/(?P<id_prod>.*)/$', 'del_product_view', name = 'vista_eliminar_producto'),
		url(r'^contacto/$', 'contacto_view', name = 'vista_contacto'),
		url(r'^login/$', 'login_view', name = 'vista_login'),
		url(r'^logout/$', 'logout_view', name = 'vista_logout'),
		url(r'^register/$', 'register_view', name = 'vista_register'),
	)

		