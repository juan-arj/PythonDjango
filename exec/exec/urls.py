
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('home/', include("home.urls")),
    path('contato/', include("contato.urls")),
    path('produtos/', include("produtos.urls")),
    path('carrinho/', include("carrinho.urls")),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]