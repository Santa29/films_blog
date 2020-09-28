from django.urls import path 

from .views import FilmListView, FilmUpdateView, FilmDeleteView, FilmDetailView, FilmCreateView, CommentCreateView, CommentDeleteView, CommentUpdateView

urlpatterns = [
    path('', FilmListView.as_view(), name= 'film_list'),
    path("new/", FilmCreateView.as_view(), name =  'film_new'),
    path('<int:pk>/edit', FilmUpdateView.as_view(), name = 'film_edit'),
    path('<int:pk>/new/', CommentCreateView.as_view(), name = 'comment_new'),
    path('<int:pk>/', FilmDetailView.as_view(), name= 'film_detail'),
    path('<int:pk>/delete/', FilmDeleteView.as_view(), name= 'film_delete'),
    path('<int:pk>/comment_edit/', CommentUpdateView.as_view(), name = 'comment_edit'),
    path('<int:pk>/comment_delete/', CommentDeleteView.as_view(), name = 'comment_delete'),
]