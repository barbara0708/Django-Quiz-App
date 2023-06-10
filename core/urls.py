from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path("",views.index,name='index'),
    path('categories/',views.categories,name="categories"),
    path('categories/category/',include('category.urls'),name='category'),
    path('sign-up/',views.signup_view,name="sign-up"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_request,name='logout'),
    path('reset/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset/done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/complete',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('reset/<uidb64>/<token>/confirm',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm')
]