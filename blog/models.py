from django.db import models
from django.db.models.functions import Lower
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def clean(self):
        categories = Category.objects.annotate(name_lower=Lower("name"))

        errors = {}

        for category in categories:
            if self.name.lower() == category.name_lower:
                errors["name"] = ValidationError(
                    f'Category "{category.name_lower}" already exist. '
                    "Try something new..."
                )
        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:category", args=[str(self.id)])


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    header_image = models.ImageField(
        blank=True, null=True, default="", upload_to="images/"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True, default="")
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("blog:article-detail", args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.post.title, self.name)
