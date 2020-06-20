from django.urls import path
from jobs import views
urlpatterns = [
    path('<slug>/', views.JobDetailView.as_view(), name="job_detail"),    
]
