from django.db import models
from django import forms

# Create your models here.
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

class JobsIndexPage(Page):
    max_count = 1
    intro = RichTextField(blank=True)
    # add the get_context method:
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        jobpages = self.get_children().live().order_by('-first_published_at')
        context['jobpages'] = jobpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    subpage_types = ['jobs.JobPage']

class JobPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'JobPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class JobPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    advisors = ParentalManyToManyField('jobs.Advisor', blank=True)

    tags = ClusterTaggableManager(through=JobPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('advisors', widget=forms.CheckboxSelectMultiple),
            FieldPanel('tags'),
        ], heading="Job information"),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    parent_page_types = ['jobs.JobsIndexPage']

class JobPageGalleryImage(Orderable):
    page = ParentalKey(JobPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

@register_snippet
class Advisor(models.Model):
    name = models.CharField(max_length=255)
    advisor_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    email = models.CharField(max_length=255, null=True, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('advisor_image'),
        FieldPanel('email'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Advisors'

class JobTagIndexPage(Page):
    max_count = 1
    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        jobpages = JobPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['jobpages'] = jobpages
        return context