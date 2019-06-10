from django.db import models


class Feed(models.Model):
        url = models.URLField(max_length=255, unique=True)
        about = models.TextField(null=True)
        description = models.TextField(null=True)
        class Meta:
            verbose_name = 'Feed'
            verbose_name_plural = 'Feeds'
        def __repr__(self):
            return "<Feed '{}'>".format(self.url)
        def __str__(self):
            return self.url

        def get_classname(self):
            return 'Feed'
