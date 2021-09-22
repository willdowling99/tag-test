from django.db import models
from wagtail.core.models import Page
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TagBase, ItemBase
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel


class TopicTag(TagBase):
    free_tagging = False
    class Meta:
        verbose_name = "Topic tag"
        verbose_name_plural = "Topic tag"

class SecondaryTag(TagBase):
    class Meta:
        verbose_name = "Secondary tag"

class TypeTag(TagBase):
    free_tagging = False
    class Meta:
        verbose_name = "Type tag"

class SponsorTag(TagBase):
    free_tagging = False
    class Meta:
        verbose_name = "Sponsor tag"


class TopicTaggedBlog(ItemBase):
    tag = models.ForeignKey(
        TopicTag, related_name="tagged_blogs", on_delete=models.CASCADE
    )
    content_object = ParentalKey(
        to='blog.BlogPage',
        on_delete=models.CASCADE,
        related_name='topic_tagged_items'
    )

class SecondTaggedBlog(ItemBase):
    tag = models.ForeignKey(
        SecondaryTag, related_name="tagged_blogs", on_delete=models.CASCADE
    )
    content_object = ParentalKey(
        to='blog.BlogPage',
        on_delete=models.CASCADE,
        related_name='second_tagged_items'
    )

class TypeTaggedBlog(ItemBase):
    tag = models.ForeignKey(
        TypeTag, related_name="tagged_blogs", on_delete=models.CASCADE
    )
    content_object = ParentalKey(
        to='blog.BlogPage',
        on_delete=models.CASCADE,
        related_name='type_tagged_items'
    )

class SponsorTaggedBlog(ItemBase):
    tag = models.ForeignKey(
        SponsorTag, related_name="tagged_blogs", on_delete=models.CASCADE
    )
    content_object = ParentalKey(
        to='blog.BlogPage',
        on_delete=models.CASCADE,
        related_name='sponsor_tagged_items'
    )

class BlogPage(Page):
    topic_tags = ClusterTaggableManager(through='blog.TopicTaggedBlog', blank=True, verbose_name = "Topic tag")
    second_tags = ClusterTaggableManager(through='blog.SecondTaggedBlog', blank=True, verbose_name = "Secondary tag")
    type_tags = ClusterTaggableManager(through='blog.TypeTaggedBlog', blank=True, verbose_name = "Type tag")
    sponsor_tags = ClusterTaggableManager(through='blog.SponsorTaggedBlog', blank=True, verbose_name = "Sponsor tag")
    content_panels = [
        FieldPanel('title'),
        MultiFieldPanel([
          FieldPanel('topic_tags'),
          FieldPanel('second_tags'),
          FieldPanel('type_tags'),
          FieldPanel('sponsor_tags'),
        ],
        heading='Tags')
    ]