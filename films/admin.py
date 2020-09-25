from django.contrib import admin
from .models import FilmReview, ReviewComment

# Register your models here.

class CommentInLine(admin.StackedInline):
    model = ReviewComment

class ReviewAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

admin.site.register(FilmReview, ReviewAdmin)
admin.site.register(ReviewComment)