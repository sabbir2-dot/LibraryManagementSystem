from django.urls import path, include
from .views import RegistrationView, UserLoginView, user_logout
from core.views import BookDetails, borrow_book, display_borrowed_books, DepositView, report_view,return_book
urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('book/<int:pk>/', BookDetails.as_view(), name='book-detail'),
    path('book/<int:book_pk>/borrow/', borrow_book, name='borrow-book'),
    path('book/<int:borrow_history_pk>/return/', return_book, name='return-book'),
    path('borrowed_books/', display_borrowed_books, name = 'display-borrowed-books'),
    path('deposit/', DepositView.as_view(), name = 'deposit'),
    path('report/', report_view, name = 'report'),
    path('logout/', user_logout, name='logout'),

]