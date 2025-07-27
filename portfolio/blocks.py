""" Here lives the blocks used for Portfolio...they use also blocks from Streams"""
from wagtail.blocks import (
    CharBlock,
    ListBlock,
    PageChooserBlock,
    RichTextBlock,
    StructBlock,
    EmailBlock,
)

# import ImageChooserBlock:
from wagtail.images.blocks import ImageChooserBlock

from streams.blocks import BaseStreamBlock

class CardBlock(StructBlock):
    heading = CharBlock()
    text = RichTextBlock(features=["bold", "italic", "link"])
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = "form"
        template = "portfolio/blocks/card_block.html"

class FeaturedPostsBlock(StructBlock):
    heading = CharBlock()
    text = RichTextBlock(features=["bold", "italic", "link"], required=False)
    posts = ListBlock(PageChooserBlock(page_type=["blog.BlogPage", "jobs.JobPage"]))

    class Meta:
        icon = "folder-open-inverse"
        template = "portfolio/blocks/featured_posts_block.html"


class TeamMemberBlock(StructBlock):
    image = ImageChooserBlock(required=False)
    name = RichTextBlock(features=["H3","H4"], required=True)
    text = RichTextBlock(required=False)
    telephone = RichTextBlock(features=["bold", "italic","link"], help_text="Choose Phone number link type--", required=False)
    email = RichTextBlock(features=["bold", "italic", "link"], help_text="Choose email link type--",required=False)

    class Meta:
        icon = "user"
        template = "portfolio/blocks/team_member_block.html"

class TeamBlock(StructBlock):
    """TEAM MEMBER Cards with Image, Text and Button for TEAM MEMBERS"""

    title = CharBlock(required=False, help_text="Add your title.")

    cards = ListBlock(

        StructBlock(
            [
              ("team_member", TeamMemberBlock()),
                
            ]
        )
    )
    class Meta: 
        icon="grip"
        template = "portfolio/blocks/team_block.html"



class PortfolioStreamBlock(BaseStreamBlock):
    

    card = CardBlock(group="Sections")
    featured_posts = FeaturedPostsBlock(group="Sections")
    team_member = TeamMemberBlock(group="Sections")
    member = TeamBlock(group="Sections")