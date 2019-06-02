from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from interest.models import Link
from machinetag.models import MachineTag
from rss.models import Feed
import re
# Create your views here.

def dashboard(request):
    tags = MachineTag.objects.order_by('label').all()
    context = {
        'machinetags': tags
    }
    return render(request, "dashboard.html", context)

def link_index(request):
    links = Link.objects.all()
    context = {
        'links': links
    }
    return render(request, 'link_index.html', context)


def link_detail(request, pk):
    link = Link.objects.get(pk=pk)
    context = {
        'link': link
    }
    return render(request, 'link_detail.html', context)


def interest_view(request):
    links = Link.objects.all()
    tags = MachineTag.objects.order_by(
        'label').all().prefetch_related('tagged')
    feeds = Feed.objects.all()
    context = {
        'tags': tags,
        'links': links,
        'feeds': feeds
    }
    if request.method == "POST":
        submitted_tags = request.POST.getlist("tag")
        submitted_links = request.POST.getlist("link")
        submitted_feeds = request.POST.getlist("feed")
        for tag in submitted_tags:
            selected_tag = MachineTag.objects.get(pk=tag)
            for link in submitted_links:
                selected_link = links.get(pk=link)
                selected_tag.tagged.add(selected_link)
            for feed in submitted_feeds:
                selected_feed = feeds.get(pk=feed)
                selected_tag.tagged.add(selected_feed)
    return render(request, "interests_index.html", context)


def interest_delete(request):
    if request.method == "POST":
        submitted_tag = request.POST.get("delete_tag")
        submitted_link = request.POST.get("delete_link")
        submitted_feed = request.POST.get("delete_feed")
        mtag = MachineTag.objects.get(id=submitted_tag)
        if submitted_link:
            link = Link.objects.get(id=submitted_link)
            mtag.tagged.remove(link)
        if submitted_feed:
            feed = Feed.objects.get(id=submitted_feed)
            mtag.tagged.remove(feed)
    return HttpResponseRedirect(reverse('interests'))

def tags_index(request):
    tags = MachineTag.objects.order_by('label').all()
    context = {
        'machinetags': tags
    }
    return render(request, "dashboard.html", context)


def tag_detail(request, label):
    fragments = re.split(':|=', label)
    print(fragments)
    tag = MachineTag.objects.get(label=label)
    context = {
        'machinetag': tag
    }
    return render(request, "tag_detail.html", context)
