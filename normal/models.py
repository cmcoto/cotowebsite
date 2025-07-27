from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField 
from wagtail.admin.panels import FieldPanel, PageChooserPanel

from streams.blocks import BaseStreamBlock


class NormalPage(Page):
    

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

    body = RichTextField(blank=True)

    extra = StreamField(
        BaseStreamBlock(),
        blank=True,
        help_text="Use this section to make the website better!.", 
        
    
    )
    

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),
        FieldPanel('banner_image'),
        PageChooserPanel('banner_cta'),
        FieldPanel('body'),
        FieldPanel('extra'),
       
       
    ]

