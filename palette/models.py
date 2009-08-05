from django.db import models

from django_extensions.db.models import TitleSlugDescriptionModel

class Palette(TitleSlugDescriptionModel):
    # All the fields we need are being defined by our base class.
    def __unicode__(self):
        return self.title


class Colour(models.Model):
    palette = models.ForeignKey(Palette)
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=6, help_text="Colour code in the format #ff00ff")

    def __unicode__(self):
        return self.title

