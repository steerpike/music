
from django.db import models
from django.utils.text import slugify
from gm2m import GM2MField
from interest.models import Link
from rss.models import Feed

class MachineTag(models.Model):
    namespace = models.CharField(max_length=100, blank=True, default='')
    namespace_slug = models.SlugField(max_length=100, editable=False, default='')
    predicate = models.CharField(max_length=100, blank=True, default='')
    predicate_slug = models.SlugField(max_length=100, editable=False, default='')
    value = models.CharField(max_length=300, blank=True, default='')
    value_slug = models.SlugField(max_length=100, editable=False,  default='')
    label = models.CharField(
        max_length=600, editable=False, blank=True, default='')
    tagged = GM2MField(Link, Feed)
    objects = models.Manager()
    class Meta:
        verbose_name = 'Machine tag'
        verbose_name_plural = 'Machine tags'
        unique_together = (
            ('namespace', 'predicate', 'value')
        )
    def __str__(self):
        return '{0.namespace}:{0.predicate}={0.value}'.format(self)

    def save(self, *args, **kwargs):
        if not self.namespace_slug:
            self.namespace_slug = slugify(self.namespace)
        if not self.predicate_slug:
            self.predicate_slug = slugify(self.predicate)
        if not self.value_slug:
            self.value_slug = slugify(self.value)
        if not self.label:
            self.label = '{0.namespace_slug}:{0.predicate_slug}={0.value_slug}'.format(
                self)
        return super().save(*args, **kwargs)
