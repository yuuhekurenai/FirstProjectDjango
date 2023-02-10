from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
]
# É necessario adicionar o caminho das imagens que seram enviadas pelos usuários
# ao UrlPatterns para que possam ser lidas.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# É como utilizamos o collectstatic para criar uma nova pasta com todos os arquivos estáticos
# agora é necessário também informar o caminho dos arquivos em produção aqui na Urls para que sejam
# visualizados, caso contrário não será possível ve-los no site.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)