from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path("",views.index,name='index'),
    path("progress/",views.progress,name='progress'),
    path('categories/',views.categories,name="categories"),
    path('categories/category/',include('category.urls'),name='category'),
    path('sign-up/',views.signup_view,name="sign-up"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_request,name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='core/password_reset.html'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'),name='password_reset_complete'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html'),name='password_reset_confirm')
]