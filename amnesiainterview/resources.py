# -*- coding: utf-8 -*-

import logging

from sqlalchemy.exc import DatabaseError

from amnesia.modules.content import Entity
from amnesia.modules.content import EntityManager
from amnesia.modules.state import State
from amnesia.modules.folder import Folder
from amnesia.modules.file import File

from amnesiainterview import Interview
from amnesiainterview.validation import InterviewSchema

log = logging.getLogger(__name__)  # pylint: disable=invalid-name


class InterviewEntity(Entity):
    """ Interview entity """

    def get_validation_schema(self):
        return InterviewSchema(context={'request': self.request})


class InterviewResource(EntityManager):

    __name__ = 'interview'

    def __getitem__(self, path):
        if path.isdigit():
            entity = self.dbsession.query(Interview).get(path)
            if entity:
                return InterviewEntity(self.request, entity)
        raise KeyError

    def get_validation_schema(self):
        return InterviewSchema(context={'request': self.request})

    def query(self):
        return self.dbsession.query(Interview)

    def create(self, data):
        state = self.dbsession.query(State).filter_by(name='published').one()
        container = self.dbsession.query(Folder).enable_eagerloads(False).\
            get(data['container_id'])
        picture = self.dbsession.query(File).enable_eagerloads(False).\
            get(data['picture_id'])

        new_entity = Interview(
            owner=self.request.user,
            state=state,
            container=container,
            picture=picture,
            **data
        )

        try:
            self.dbsession.add(new_entity)
            self.dbsession.flush()
            return new_entity
        except DatabaseError:
            return False
