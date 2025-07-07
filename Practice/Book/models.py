from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Course(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)
    marks = models.IntegerField()