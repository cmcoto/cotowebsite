from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    PublishingPanel,
    PageChooserPanel,
)

from wagtail.fields import RichTextField

from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)

from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)

from wagtail.snippets.models import register_snippet

@register_setting
class NavigationSettings(BaseGenericSetting):
    social_text = models.CharField(max_length=255, blank=False, null=True, verbose_name="Social Media Phrase", help_text="Write the Follow us here...")
    twitter_url = models.URLField(verbose_name="Twitter URL", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    facebook_url = models.URLField(verbose_name="Facebook URL", blank=True)
    linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True)
    instagram_url = models.URLField(verbose_name="Instagram URL", blank=True)
    
    #FOR HEADER
    header_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    header_cta = models.CharField(
        blank=True,
        null=True,
        verbose_name="Header CTA",
        max_length=255,
        help_text="Text to display on Call to Action on Header",
    )

    #FOR LOCAL CONTACTS
    contact_phrase = RichTextField(
        blank=True,
        features=['h2', 'h3', 'bold', 'italic'],
        null=True, help_text="Write What you would like to say as Contact..on the FOOTER. Example: Contact Us, Contact, etc.",
       
    )

    contact_url = RichTextField(blank=True, null=True, features=["link"], help_text="Pick Link using / on the area. The url link will show on the Footer, on top of Address, below Contact_Phrase...")

    address = RichTextField(
        blank=True,
        null=True, help_text="Write your Address here...",
        max_length=255,
    )
    phone = RichTextField(
        blank=True,
        null=True,
        verbose_name="Your Phone Number",
        max_length=255,
        help_text="Write your phone number here. Before, choose / and Link, then email_link...",
    )
    email = RichTextField(max_length=255, blank=True, null=True, help_text="Write your email here. Before, choose / and Link, then phone_link...")

   
    privacy_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
 
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("header_image"),
                FieldPanel("header_cta"),
            ],
            "Header settings",
        ),
        MultiFieldPanel(
            [
                FieldPanel("social_text"),
                FieldPanel("twitter_url"),
                FieldPanel("github_url"),
                FieldPanel("facebook_url"),
                FieldPanel("linkedin_url"),
                FieldPanel("instagram_url"),
            ],
            "Social settings",
        ),
        MultiFieldPanel(
            [
                FieldPanel("contact_phrase"),
                FieldPanel("contact_url"),
                FieldPanel("address"),
                FieldPanel("phone"),
                FieldPanel("email"),
                PageChooserPanel('privacy_cta'),
                
            ],
            "Your Contact settings",
        )
    ]

#FOR THE FOOTER TEXT...
    
@register_snippet
class FooterText(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):

    body = RichTextField(blank=True, null=True)

    panels = [
        FieldPanel("body"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Footer text"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_text": [self.body ]}

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Footer Text"
  