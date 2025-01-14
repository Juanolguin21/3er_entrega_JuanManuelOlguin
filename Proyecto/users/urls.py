
from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('login/', views.login_request, name="Login" ),
    path('register/', views.register, name="Register" ),
    path('logout/', LogoutView.as_view(template_name='Neoprenos/inicio.html'), name='Logout'),
    path('update-profile/', views.update_user, name='update_user')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
