from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, PageChooserPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet

from streams.blocks import BaseStreamBlock
from portfolio.blocks import PortfolioStreamBlock

class HomePage(Page):
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_subtitle = RichTextField(blank=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

  

    button_text = models.CharField(max_length=50, blank=True, null=True)

    # add the Hero section of HomePage:
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    hero_text = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )
    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )

    body = RichTextField(blank=True)

    extra = StreamField(
        PortfolioStreamBlock(),
        BaseStreamBlock(),
        blank=True,
        help_text="Use this section to make the website better!.", 
    
    )


    content_panels = Page.content_panels + [
        MultiFieldPanel (
            [
                FieldPanel('banner_title'),
                FieldPanel('banner_subtitle'),
                FieldPanel('banner_image'),
                PageChooserPanel('banner_cta'),
                
                FieldPanel('button_text')
            ],
            heading="Banner Section",
        ),
        MultiFieldPanel (   
            [
                FieldPanel('hero_image'),
                FieldPanel('hero_text'),
                FieldPanel('hero_cta'),
                FieldPanel('hero_cta_link'),
            ],
            heading="Hero Section",
        ),
        FieldPanel('body'),
        FieldPanel('extra'),
    ]


    
