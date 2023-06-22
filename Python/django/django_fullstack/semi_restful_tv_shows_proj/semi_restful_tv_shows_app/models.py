from django.db import models
from datetime import datetime
# Create your models here.


class Tv_showsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # Validate title
        title = postData.get('title')
        title1 = postData.get('title1')
        if not title1:
            if not title:
                errors['title'] = "Title is required gasioaspo."
            elif len(title) < 2:
                errors["title"] = "Tv Show Title should be at least 2 characters"
            else:
                # Check if a TV show with the same title already exists
                existing_tv_show = Tv_shows.objects.filter(
                    title__iexact=title).first()
                if existing_tv_show:
                    errors['title'] = "A TV show with this title already exists."
        # Validate title for update
        id = postData.get('id')
        if not title:
            if not title1:
                errors['title1'] = "Title is required."
            elif len(title1) < 2:
                errors["title1"] = "Tv Show Title should be at least 2 characters"
            else:
                existing_tv_show1 = Tv_shows.objects.get(
                    id=id)
                # Check if a TV show with the same title already exists
                existing_tv_show = Tv_shows.objects.filter(
                    title__iexact=title1).first()
                if existing_tv_show:
                    if existing_tv_show1.id != existing_tv_show.id:
                        errors['title'] = "A TV show with this title already exists."
        # Validate network
        network = postData.get('network')
        if not network:
            errors['network'] = "Network is required."
        elif len(network) < 3:
            errors["network"] = (
                "Tv Show Network should be at least 3 characters")

        # Validate release date
        release_date = postData.get('release_date')
        if not release_date:
            errors['release_date'] = "Release date is required."
        elif release_date > str(datetime.now()):
            errors['release_date'] = "Release date should be in the past."

        # Validate description (optional)
        desc = postData.get('desc')
        if desc and len(desc) < 10:
            errors['desc'] = (
                "Description should be at least 10 characters if it is exist.")

        return errors


class Tv_shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Tv_showsManager()
