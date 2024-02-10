
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name="signup"),
    path('login/',views.LoginPage,name="login"),
    path('home/',views.HomePage,name="home"),
    path('liver/',views.LiverPage,name="liver"),
    path('heart/',views.HeartPage,name="heart"),
    path('heart_result/',views.HeartResult,name="heart_result"),
    path('breast/',views.BreastPage,name="breast"),
    path('breast_result/',views.BreastResult,name="breast_result"),
    path('diabetes/',views.DiabetesPage,name="diabetes"),
    path('diabetes_result/',views.DiabetesResult,name="diabetes_result"),
    path('parkinson/',views.ParkinsonPage,name="parkinson"),
    path('parkinson_result/',views.ParkinsonResult,name="parkinson_result"),

    path('liver_result/',views.LiverResult,name="liver_result"),

    path('logout,',views.LoginPage,name='logout')
]
