from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from users import views as users_views
from home import views as home_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    # path('', include('django.contrib.auth.urls')),
    path('register', users_views.register, name='register'),
    path('register2', users_views.user_append, name='append_user'),
    path('cabinet', users_views.cabinet, name='cabinet'),
    path('login_select', users_views.login_select, name='login_select'),
    path('login/<login_method>', users_views.login, name='login'),
    path('logout', users_views.logout, name='logout'),
    path('delete_user', users_views.delete_user, name='delete_user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
