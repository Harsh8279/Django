from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success-page/',views.success_page, name = "success_page"),
    path('contact-us/',views.contact_us, name="Contact-us"),
    path('about-us/',views.about_us, name="About-us"),

]