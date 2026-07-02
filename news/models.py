from django.db import models
from django.contrib.auth.models import User
from .ml import predict_category

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class News(models.Model):

    STATUS = (
        ("Draft", "Draft"),
        ("Published", "Published"),
    )

    title = models.CharField(max_length=300)

    content = models.TextField()

    image = models.ImageField(
        upload_to="news_images/",
        blank=True,
        null=True
    )

    # AI Prediction
    auto_category = models.CharField(
        max_length=50,
        blank=True
    )

    # Final Category
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Draft"
    )

    views = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        text = self.title + " " + self.content
        predicted_category = predict_category(text)
        self.auto_category = predicted_category.title()
        if not self.category:
            category = Category.objects.filter(name__iexact=predicted_category).first()
            if category:
                self.category = category

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title