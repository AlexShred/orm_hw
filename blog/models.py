from django.db import models


class AbstractUser(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=30, unique=True)

    class Meta:
        abstract = True


class Author(AbstractUser):
    username = models.CharField(max_length=30)
    date_register = models.DateField()

    def __str__(self):
        return self.username


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, through='Publication', related_name='articles')

    def __str__(self):
        return self.title


class Publication(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_published = models.DateField()

    def __str__(self):
        return f'{self.author} - {self.article}'
