from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shared_lists')

    def get_absolute_url(self):
        return reverse('lists:view_list', args=[self.id])

    @staticmethod
    def create_new(first_item_text, owner=None):
        list_ = List.objects.create(owner=owner)
        Item.objects.create(text=first_item_text, list=list_)
        return list_

    @property
    def name(self):
        return self.item_set.first().text

    # @property
    # def shared_with_all(self):
    #     return self.shared_with.all()


class Item(models.Model):
    text = models.TextField(default="")
    list = models.ForeignKey(List, default=None)

    def __str__(self):
        return self.text

    class Meta:
        unique_together = ('list', 'text')
        ordering = ('id',)