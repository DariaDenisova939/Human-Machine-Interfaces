from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path

from Lab3 import settings
from . import views
urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('', views.index, name='home'),
    path('output/<int:idx>', views.output, name='output'),
    path('output_course/', views.output_course, name='output_course'),
    path('course/<int:pk>', views.course, name='course'),
    path('complaint/<int:pk>', views.complaint, name='complaint'),
    path('create_favorite_course/<int:pk>', views.create_favorite_course, name='create_favorite_course'),
    path('output_favorite_course/', views.output_favorite_course, name='output_favorite_course'),
    path('output_author_course/', views.output_author_course, name='output_author_course'),
    path('authorship/<str:flag>/<int:pk>', views.authorship, name='authorship'),
    path('delete_check/<int:pk>/<int:idx>', views.delete_check, name='delete_check'),
    path('create/<int:idx>/<int:pk>', views.create, name='create'),
    path('delete/<int:pk>/<int:idx>', views.delete, name='delete'),
    path('update/<int:idx>/<int:pk>', views.update, name='update'),
    path('timetable/', views.timetable, name='timetable'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('logout', views.logout_user, name='logout'),
]
