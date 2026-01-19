from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logs/',views.logs_view,name='logs'),
    path("account/", views.account_view, name="account"),
]