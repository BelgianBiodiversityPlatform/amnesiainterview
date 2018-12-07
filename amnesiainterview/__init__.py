# -*- coding: utf-8 -*-

from .model import Interview

from .resources import InterviewEntity
from .resources import InterviewResource


def includeme(config):
    config.include('.mapper')
    config.include('.views')
