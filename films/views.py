from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView

from .models import FilmReview, ReviewComment

from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class FilmListView(LoginRequiredMixin,ListView):
    model = FilmReview 
    template_name = 'film_list.html'
    context_object_name = 'film_list'
    login_url = 'login'

class FilmUpdateView(LoginRequiredMixin, UpdateView):
    model = FilmReview
    template_name = 'film_edit.html'
    fields = ('film_name', 'body', 'actors')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class FilmDeleteView(LoginRequiredMixin, DeleteView):
    model = FilmReview
    template_name = "film_delete.html"
    success_url = reverse_lazy('film_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class FilmDetailView(LoginRequiredMixin, DetailView):
    model = FilmReview
    template_name = 'film_detail.html'
    context_object_name = 'film'
    login_url = 'login'

class FilmCreateView(LoginRequiredMixin, CreateView):
    model = FilmReview
    template_name = 'film_new.html'
    fields = ('film_name', 'body', 'actors')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = ReviewComment
    template_name = 'comment_new.html'
    fields = ('review_comment')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = ReviewComment
    template_name = 'comment_edit.html'
    fields = ('review_comment')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = ReviewComment
    template_name = "comment_delete.html"
    success_url = reverse_lazy('film_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
