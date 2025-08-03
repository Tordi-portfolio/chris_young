# store/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Forgot password (Step 1: request reset email)
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='app4/password_reset.html'), name='reset_password'),

    # Step 2: email sent confirmation
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name='app4/password_reset_sent.html'), name='password_reset_done'),

    # Step 3: link from email
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app4/password_reset_confirm.html'), name='password_reset_confirm'),

    # Step 4: password successfully changed
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app4/password_reset_complete.html'), name='password_reset_complete'),
]