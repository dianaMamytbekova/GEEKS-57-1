from django.contrib import admin
from .models import Genre, Tag, Movie, Rating, Comment

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'avg_rating')
    list_filter = ('genre', 'tags')
    search_fields = ('title', 'description')
    filter_horizontal = ('tags',)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'score', 'created_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'created_at', 'active')
    list_filter = ('active',)

