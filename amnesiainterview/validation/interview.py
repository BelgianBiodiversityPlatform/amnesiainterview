# -*- coding: utf-8 -*-


from marshmallow.fields import Integer
from marshmallow.fields import String
from marshmallow.fields import Url
from marshmallow.validate import Length

from amnesia.modules.content.validation import ContentSchema


class InterviewSchema(ContentSchema):
    ''' Schema for the Document model '''

    content_id = Integer(dump_only=True)
    picture_id = Integer(required=True)
    last_name = String(required=True, validate=[Length(min=1)])
    first_name = String(required=True, validate=[Length(min=1)])
    position = String(missing=None)
    affiliation = String(missing=None)
    body = String(required=True)
    twitter = Url(missing=None)
    linkedin = Url(missing=None)
    facebook = Url(missing=None)
    instagram = Url(missing=None)
    researchgate = Url(missing=None)
