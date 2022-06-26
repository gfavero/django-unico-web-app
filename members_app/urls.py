from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from .forms import MySetPasswordForm
from UnicoWebApp import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register"),
    path('profile', views.profile, name="profile"),
    path('user_list', views.user_list, name="user-list"),
    path('profile_edit/<user_local>', views.profile_edit, name="profile-edit"),


    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="auth/password_reset.html"),
     name="reset_password"),

    #  path('reset_password/', views.PasswordResetView, name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="auth/password_reset_sent.html"), 
        name="password_reset_done"),

     path(
    'UnicoWebApp/reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(form_class=MySetPasswordForm,template_name="auth/password_reset_form.html"), 
    name='password_reset_confirm'),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="auth/password_reset_done.html"), 
        name="password_reset_complete"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
