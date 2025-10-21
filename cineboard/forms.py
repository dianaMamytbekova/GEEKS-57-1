from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Movie, Comment, Rating

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genre', 'release_date', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']

