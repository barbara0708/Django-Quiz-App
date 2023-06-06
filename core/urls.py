from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path("",views.index,name='index'),
    path('categories/',views.categories,name="categories"),
    path('categories/category/',include('category.urls')),
    path('sign-up/',views.signup_view,name="sign-up"),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='core/logout.html'),name='logout')
]