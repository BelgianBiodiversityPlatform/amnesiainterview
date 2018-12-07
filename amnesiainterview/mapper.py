# -*- coding: utf-8 -*-

from sqlalchemy import orm

from amnesia.modules.content import Content
from amnesia.modules.content_type import ContentType
from amnesia.modules.file import File
from amnesia.modules.content_type.utils import get_type_id

from .model import Interview


def includeme(config):
    tables = config.registry['metadata'].tables

    config.include('amnesia.modules.content.mapper')
    config.include('amnesia.modules.content_type.mapper')

    orm.mapper(
        Interview, tables['amnesiainterview.interview'], inherits=Content,
        polymorphic_identity=get_type_id(config, 'interview'),
        properties={
            'picture': orm.relationship(
                File, lazy='joined', innerjoin=True, uselist=False,
                foreign_keys=[
                    tables['amnesiainterview.interview'].c.picture_id
                ]
            )
        }
    )

