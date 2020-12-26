from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class Listing(models.Model):
    CATEGORY_CHOICES = (
        ("Fashion", "Fashion"),
        ("Technology", "Technology"),
        ("Electronics", "Electronics"),
        ("Home", "Home"),
        ("Pantry", "Pantry"),
        ("Toys", "Toys")
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    starting_bid = models.DecimalField(max_digits=19, decimal_places=2)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return f"Bid on {self.listing.title} by {self.user.username}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"Comment on {self.listing.title} by {self.user.username}"