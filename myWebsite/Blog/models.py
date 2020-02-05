from django.db import models
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):

    title = models.CharField(max_length=50,help_text="Title of the post")
    content = models.TextField(max_length=20000,help_text="post content goes here")
    Author = models.CharField(max_length=20,help_text="name of the author")
    date = models.DateTimeField(help_text="Date, the post was written")

    def __str__(self):

        return  self.title


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'