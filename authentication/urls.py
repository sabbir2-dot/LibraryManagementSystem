from django.urls import path, include
from .views import RegistrationView, UserLoginView
from core.views import BookDetails
urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('book/<int:pk>/', BookDetails.as_view(), name='book-detail'),

]