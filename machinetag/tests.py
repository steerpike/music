from django.test import TestCase
from interest.models import Link, Person
from machinetag.models import MachineTag

# Create your tests here.

class TagTestCase(TestCase):
    def setUp(self):
        Link.objects.create(
            title='Test title', 
            description='A long test description', url='http://www.google.com', code='200')
        Person.objects.create(
            twitter_username='brightcarvings', twitter_id='267856')
        mt1 = MachineTag.objects.create(
            namespace='education', predicate='tutorial', value= 'writing')
        mt2 = MachineTag.objects.create(
            namespace='development', predicate='tutorial', value='laravel')
        mt3 = MachineTag.objects.create(
            namespace='development', predicate='processes', value='agile')
        mt4 = MachineTag.objects.create(
            namespace='development', predicate='languages', value='php')
        link1 = Link.objects.create(
            title='Link1 title',
            description='Link1 long test description', url='http://www.google.com', code='200')
        link2 = Link.objects.create(
            title='Link2 title',
            description='Link2 long test description', url='http://www.google.com', code='200')
        link3 = Link.objects.create(
            title='Link3 title',
            description='Link3 long test description', url='http://www.google.com', code='200')
        mt1.tagged.add(link1)
        mt2.tagged.add(link2)
        mt3.tagged.add(link3)
        mt4.tagged.add(link2)
        
    def test_machine_tag_can_attach(self):
        link = Link.objects.get(title='Test title')
        tag = MachineTag.objects.get(
            namespace='education',
            predicate='tutorial',
            value='writing'
        )
        tag.tagged.add(link)
        self.assertEqual(len(list(tag.tagged.all())), 2)
