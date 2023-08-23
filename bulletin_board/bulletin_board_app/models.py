from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    # TANKS = 'TA'
    # HEALTH = 'HP'
    # DD = 'DD'
    # MERCHANTS = 'ME'
    # GILDMASTERS = 'GM'
    # QUESTGIVERS = 'QG'
    # BLACKSMITHS = 'BS'
    # LEATHERWORKERS = 'LW'
    # POTIONS = 'PO'
    # SPELLMASTERS = 'SM'
    TANKS = 'Танки'
    HEALTH = 'Хилы'
    DD = 'ДД'
    MERCHANTS = 'Торговцы'
    GILDMASTERS = 'Гилдмастеры'
    QUESTGIVERS = 'Квестгиверы'
    BLACKSMITHS = 'Кузнецы'
    LEATHERWORKERS = 'Кожевники'
    POTIONS = 'Зельевары'
    SPELLMASTERS = 'Мастера заклинаний'
    CATEGORY_CHOICES = (
        (TANKS, 'Танки'),
        (HEALTH, 'Хилы'),
        (DD, 'ДД'),
        (MERCHANTS, 'Торговцы'),
        (GILDMASTERS, 'Гилдмастеры'),
        (QUESTGIVERS, 'Квестгиверы'),
        (BLACKSMITHS, 'Кузнецы'),
        (LEATHERWORKERS, 'Кожевники'),
        (POTIONS, 'Зельевары'),
        (SPELLMASTERS, 'Мастера заклинаний'),
    )
    # categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=MERCHANTS)
    categoryType = models.TextField(choices=CATEGORY_CHOICES, default=MERCHANTS)

    def __str__(self):
        return f"{self.categoryType}"

class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = models.TextField()
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
    image = models.ImageField(blank=True)
    file = models.FileField(blank=True)
    adCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return f'/ads/ad/{self.id}'

# class AdCategory(models.Model):
#     adThrough = models.ForeignKey(Ad, on_delete=models.CASCADE)
#     categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    commentAuthor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.commentAuthor}"

