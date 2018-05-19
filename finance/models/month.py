# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Month(models.Model):
    class Meta:
        verbose_name = "month"
        verbose_name_plural = "months"

    name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name="Month Name"
    )

    def __unicode__(self):
        return u"Бюджет за %s" % (self.name)