from django.contrib import admin

from .models import UserProfile, Book, BorrowHistory, BookReview
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(BorrowHistory)
admin.site.register(BookReview)