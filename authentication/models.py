from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def deposit(self, amount):
        self.balance += amount
        self.save()
    
    def deduct_balance(self,amount):
        self.balance -= amount
        self.save()
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class BorrowHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(default=now)
    return_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('borrowed', 'Borrowed'), ('returned', 'Returned')], default='available')
    
    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"


class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review of {self.book.title}"
    
