from django.conf import settings
from django.conf.urls.static import static
from django.urls import path



from . import views

urlpatterns = [
    path('',views.mapa,name='mapa'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout' ),
    path('registro_normal/',views.registro_normal,name='registro_normal' ),
    # path('',views.lista_carritos,name='lista_carritos'),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)