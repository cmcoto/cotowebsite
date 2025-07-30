""" Here live all the blocks used for almost everything"""
from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    ListBlock,
    TextBlock,
    PageChooserBlock,
    URLBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "base/blocks/image_block.html"


class HeadingBlock(StructBlock):
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a heading size"),
            ("h1", "H1"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "base/blocks/heading_block.html"

class CardBlock(StructBlock):
    """Cards with Image, Text and Button"""

    title = CharBlock(required=True, help_text="Add your title.")

    cards = ListBlock(

        StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", CharBlock(required=True, max_length=40)),
                ("text", TextBlock(required=True, max_length=200)),
                ("button_page", PageChooserBlock(required=False)),
                ("button_url", URLBlock(required=False, help_text="If the button_page is selected, that will be used first.")),

            ]
        )
    )
    class Meta: 
        icon="grip"
        template = "base/blocks/card_block.html"

class BaseStreamBlock(StreamBlock):
    cards = CardBlock()
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(icon="pilcrow")
    image_block = ImageBlock()
    embed_block = EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )
    

