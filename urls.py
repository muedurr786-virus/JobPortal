from django.urls import path
from django.conf import settings  # <-- Added this import
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # Authentication URLs
    path('register/', registerpage, name='register'),
    path('', loginpage, name='login'),
    path('logout/', logoutpage, name='logout'),
    
    # Dashboard & Profile URLs
    path('dashboard/', dashboardpage, name='dashboard'),
    path('recruiter/', recuiterpage, name='recuiter'),  # Matches your typo redirect/template names
    path('job-seeker/', JobSeekerpage, name='jobseeker'),
    
    # Job Posting & Application Management URLs
    path('job-post/', Jobpostpage, name='jobpost'),
    path('applications/', applicationpage, name='applicationlist'),
    path('my-applications/', myapplicationpage, name='myapplication'),
    
    # Skills & Matching URLs
    path('skill-matching/', skillmachingpage, name='skillmatching'),
    path('add_skill/', skillPage, name='add_skill'),
    
    # Application Status Actions (Passing the ID)
    path('application/shortlist/<int:id>/', shortlistpage, name='shortlist'),
    path('application/reject/<int:id>/', rejectpage, name='reject'),
    path('application/pending/<int:id>/', pendingpage, name='pending'),
]

# Fixed the syntax error by moving this to its own line
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
