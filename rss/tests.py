from django.test import TestCase

from django.urls import reverse
import json
from rss.models import Feed


class RssIndexViewTests(TestCase):
    def test_no_feed(self):
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["feed"], None)


class RssFeedModelTests(TestCase):
        def setUp(self):
                Feed.objects.create(
                    url="https://www.djangoproject.com/rss/weblog/"
                )

        def test_model_has_url(self):
                django_feed = Feed.objects.get(
                    url="https://www.djangoproject.com/rss/weblog/"
                )

                self.assertEqual(
                    django_feed.url,
                    "https://www.djangoproject.com/rss/weblog/"
                )


class RssRestFeedsViewTests(TestCase):

        def test_create_feed(self):
                url = "https://www.djangoproject.com/rss/weblog/"
                json_data = json.dumps({"url": url})

                response = self.client.post(
                    reverse("rest-feeds"),
                    json_data,
                    content_type="application/json"
                )

                feeds = Feed.objects.all()

                self.assertEqual(response.status_code, 201)
                self.assertQuerysetEqual(
                    feeds,
                    ["<Feed '{}'>".format(url)]
                )

        def test_get_feeds(self):
                url = "https://www.djangoproject.com/rss/weblog/"

                Feed.objects.create(
                    url=url
                )

                response = self.client.get(reverse('rest-feeds'))
                feed = response.json()[0]

                self.assertEqual(response.status_code, 200)
                self.assertEqual(feed["url"], url)
                
class RssRestItemsViewTests(TestCase):

        def test_get_items(self):
                Feed.objects.create(
                    url="https://www.djangoproject.com/rss/weblog/"
                )

                response = self.client.get(reverse("rest-items"))

                self.assertEqual(response.status_code, 200)
