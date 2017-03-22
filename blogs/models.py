from django.db import models
from django.conf import settings
from django import forms

from modelcluster.fields import ParentalManyToManyField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
from django.utils.safestring import mark_safe

COMMENTS_APP = getattr(settings, 'COMMENTS_APP', None)

@register_snippet
class Category(models.Model):
    name = models.CharField(max_length=25)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class CodeBlock(blocks.StructBlock):

    # short names from http://pygments.org/docs/lexers/
    languages = [
        ('python', 'Python'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('js', 'JavaScript'),
        ('json', 'JSON'),
        ('bash', 'BASH'),
    ]

    language = blocks.ChoiceBlock(languages)
    code = blocks.TextBlock()

    class Meta:
        icon = 'code'

    def render(self, inp, context=None):
        lexer = get_lexer_by_name(inp['language'])
        src = inp['code']
        formatter = get_formatter_by_name(
            'html',
            style='default',
            cssclass='codehilite',
        )

        return mark_safe(highlight(src, lexer, formatter))

class BlogIndex(Page):
    # An introduction to the type of blogs
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

class BlogPost(Page):

    # to appear on the index page
    intro = RichTextField(blank=True)

    # subheading to go under main title
    subheading = models.CharField(max_length=50, blank=True)

    categories = ParentalManyToManyField('blogs.Category', blank=True)

    # author is currently being obtained from page.owner

    body = StreamField([
        ('section_heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('code', CodeBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('subheading'),
        FieldPanel('intro'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        StreamFieldPanel('body'),
    ]

    def get_absolute_url(self):
        return self.url

    def get_context(self, request, *args, **kwargs):
        context = super(BlogPost, self).get_context(request, *args, **kwargs)
        context['COMMENTS_APP'] = COMMENTS_APP
        return context