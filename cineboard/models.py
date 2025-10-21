from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='movies')
    release_date = models.DateField(null=True, blank=True)
    avg_rating = models.FloatField(default=0)
    tags = models.ManyToManyField(Tag, blank=True, related_name='movies')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='movies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cineboard:movie_detail', kwargs={'pk': self.pk})

    def update_avg_rating(self):
        agg = self.ratings.aggregate(models.Avg('score'))
        self.avg_rating = agg['score__avg'] or 0
        self.save(update_fields=['avg_rating'])

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    score = models.PositiveSmallIntegerField()  # 1..5
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('movie', 'user')

    def __str__(self):
        return f"{self.movie.title} — {self.score}"

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.movie}"
