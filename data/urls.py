from django.urls import include, path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add/resume.html', views.resume1, name='student_changelist'),
    path('data/', views.StudentLiView.as_view(), name='resume1'),
    path('add/', views.StudentCreView.as_view(), name='student_add'),
    path('<int:pk>/', views.StudentUpView.as_view(), name='student_change'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),
    path('', views.index, name='index'),
    path('registered/', views.resume, name='resume'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)