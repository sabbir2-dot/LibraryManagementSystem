from django.shortcuts import render, redirect
from django.views.generic import TemplateView,DetailView, FormView
from authentication.models import Book, BorrowHistory
from django.contrib.auth.decorators import login_required
from authentication.forms import DepositForm
from django.utils.timezone import now
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context

class BookDetails(DetailView):
    model = Book
    template_name = 'book_details.html'

@login_required
def borrow_book(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    user = request.user
    user_profile = user.profile

    if request.method == 'POST':
        if book.available and user_profile.deduct_balance(book.cost):
            BorrowHistory.objects.create(user=user, book=book, status='borrowed')
            book.available = False
            book.save()
            return redirect('book-detail', pk=book_pk)  # Pass pk as argument to redirect
        else:
            message = 'Insufficient balance' if user_profile.deduct_balance(book.cost) == False else 'Book is not available for borrowing'
            return render(request, 'book_details.html', {'book': book, 'message': message})
    else:
        return redirect('book-detail', pk=book_pk)
    
def display_borrowed_books(request):
    user = request.user
    borrowed_books = BorrowHistory.objects.filter(user=user, status='borrowed')
    return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books})

class DepositView(FormView):
    template_name = 'deposit.html'
    form_class = DepositForm

    def form_valid(self,form):
        amount = form.cleaned_data['amount']
        user_profile = self.request.user.profile
        user_profile.deposit(amount)
        return redirect('home')
    
@login_required
def return_book(request, borrow_history_pk):
    borrow_history = BorrowHistory.objects.get(pk=borrow_history_pk)
    user_profile = borrow_history.user.profile
    book = borrow_history.book

    if request.method == 'POST':
        # Update the return status and set the return date
        borrow_history.status = 'returned'
        borrow_history.return_date = now()
        borrow_history.save()

        # Mark the book as available
        book.available = True
        book.save()

        # Refund the book cost to the user's balance
        user_profile.deposit(book.cost)

        # Redirect to the borrowed books page
        return redirect('display-borrowed-books')
    else:
        return render(request, 'borrowed_books.html', {'borrowed_books': [borrow_history]}) 
    
def report_view(request):
    borrow_history = BorrowHistory.objects.filter(user = request.user)
    return render(request, 'report.html', {'borrow_history': borrow_history})