from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
