from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from cineboard import views as cb_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tvShow.urls')),
    path('', include('book.urls')),
    path('', include('students.urls')),
    path('basket/', include('basket.urls')),
    path('clothes/', include('clothes.urls')),
    path('cineboard/', include('cineboard.urls', namespace='cineboard')),
    path('register/', cb_views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='cineboard:movie_list'), name='logout'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

