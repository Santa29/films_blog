from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class FilmReview(models.Model):
    film_name = models.CharField(max_length=256)  # название фильма
    actors = models.TextField() # список актеров
    date = models.DateTimeField(auto_now_add=True) # время написания отзыва
    body = models.TextField() # тело отзыва
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
       
    ) # автор обзора

    def __str__(self):
        return self.film_name

    def get_absolute_url(self):
        return reverse('film_detail', args = [str(self.id)])


# Модель комментария для обзора на фильм
class ReviewComment(models.Model):
    post = models.ForeignKey(
        FilmReview, 
        on_delete=models.CASCADE, 
        related_name='reviews',
    )
    review_comment = models.CharField(max_length=250)
    author =  models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
    ) 
    date = models.DateTimeField(auto_now_add=True) # время написания коммента

    def __str__(self):
       return self.review_comment

    def get_absolute_url(self):
        return reverse('films_list')