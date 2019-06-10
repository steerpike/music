from django.db import models

# Create your models here.

class Person(models.Model):
    twitter_username = models.CharField(max_length=200)
    twitter_id = models.IntegerField(null=True)
    objects = models.Manager()

    def __str__(self):
        return self.twitter_username

class HashTag(models.Model):
    hashtag = models.CharField(max_length=200)
    person = models.ManyToManyField(Person, through='Trusted')


class Trusted(models.Model):
    expert = models.ForeignKey(
        Person, related_name="expert", on_delete=models.DO_NOTHING)
    twittertag = models.ForeignKey(HashTag, on_delete=models.DO_NOTHING)


class Link(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=2000)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        return self.title

    def get_classname(self):
        return 'Link'
