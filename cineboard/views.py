from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Q
from .models import Movie, Genre, Tag, Rating
from .forms import MovieForm, CommentForm, RatingForm
from .forms import RegisterForm


class MovieListView(ListView):
    model = Movie
    template_name = 'cineboard/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 6  

    def get_queryset(self):
        qs = Movie.objects.all().order_by('-avg_rating', '-created_at')
        q = self.request.GET.get('q')
        genre_slug = self.kwargs.get('genre_slug')
        tag_slug = self.kwargs.get('tag_slug')
        if q:
            qs = qs.filter(title__icontains=q)
        if genre_slug:
            qs = qs.filter(genre__slug=genre_slug)
        if tag_slug:
            qs = qs.filter(tags__slug=tag_slug)
        return qs.distinct()

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'cineboard/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['rating_form'] = RatingForm()
        context['comments'] = self.object.comments.filter(active=True).order_by('-created_at')
        return context

class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'cineboard/movie_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        return response

class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'cineboard/movie_form.html'

    def test_func(self):
        obj = self.get_object()
        return obj.created_by == self.request.user or self.request.user.is_staff

class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    template_name = 'cineboard/movie_confirm_delete.html'
    success_url = reverse_lazy('cineboard:movie_list')

    def test_func(self):
        obj = self.get_object()
        return obj.created_by == self.request.user or self.request.user.is_staff


from django.views import View
from .models import Comment

class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
        return redirect(movie.get_absolute_url())

class AddRatingView(LoginRequiredMixin, View):
    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        form = RatingForm(request.POST)
        if form.is_valid():
            rating_obj, created = Rating.objects.update_or_create(
                movie=movie, user=request.user,
                defaults={'score': form.cleaned_data['score']}
            )
            movie.update_avg_rating()
        return redirect(movie.get_absolute_url())
    

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')    
