import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone

# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

'''
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
'''


class Authors(models.Model):
    name = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)


class Stories(models.Model):
    key = models.AutoField(auto_created=True, primary_key=True)
    headline = models.CharField(max_length=64)

    POLITICS = 'POL'
    ART = 'ART'
    TECHNOLOGY = 'TECH'
    TRIVIAL = 'TRIVIA'
    CATEGORY_CHOICES = (
        (POLITICS, 'Politics News'),
        (ART, 'Art News'),
        (TECHNOLOGY, 'Technology News'),
        (TRIVIAL, 'Trivial News'),
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
    )

    UK = 'UK'
    EUROPEAN = 'EU'
    WORLD = 'W'
    REGION_CHOICES = (
        (UK, 'UK News'),
        (EUROPEAN, 'European News'),
        (WORLD, 'World News'),
    )
    region = models.CharField(
        max_length=20,
        choices=REGION_CHOICES,
        default=None
    )

    author = models.ForeignKey('Authors', to_field='username', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=512)

    def switchJson(self):
        json = {
            'key': self.key,
            'headline': self.headline,
            'story_cat': self.category,
            'story_region': self.region,
            'author': self.author.username,
            'story_date': datetime.strftime(self.date, "%Y-%m-%d %H:%M:%S"),
            'story_details': self.details,
        }
        return json



