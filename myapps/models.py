from django.db import models


class Books(models.Model):
    book_name=models.CharField(max_length=200)
    author_name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    pages=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.book_name
    