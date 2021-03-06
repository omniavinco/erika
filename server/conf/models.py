#-*- coding: utf-8 -*-

from common import db
import datetime
from settings import DB_PREFIX as prefix

class ConfigFile(db.Model):
    __tablename__ = prefix + 'configfile'

    id = db.Column(db.Integer, primary_key=True)
    filetype = db.Column(db.String(63))

    user_id = db.Column(db.Integer, db.ForeignKey(prefix + 'user.id'))
    user = db.relationship('User', foreign_keys=[user_id])

    parent_id = db.Column(db.Integer, db.ForeignKey(prefix + 'user.id'))
    parent = db.relationship('User', foreign_keys=[parent_id])
    
    content = db.Column(db.String)
    desc = db.Column(db.String)

    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, filetype='', user=None, content='', desc=''):
        self.filetype = filetype
        self.user = user
        self.content = content
        self.desc = desc


class ConfigArchive(db.Model):
    __tablename__ = prefix + 'configarchive'

    id = db.Column(db.Integer, primary_key=True)
    filetype = db.Column(db.String(63))

    user_id = db.Column(db.Integer, db.ForeignKey(prefix + 'user.id'))
    user = db.relationship('User')

    content = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, filetype='', user=None, content=''):
        self.filetype = filetype
        self.user = user
        self.content = content

    
