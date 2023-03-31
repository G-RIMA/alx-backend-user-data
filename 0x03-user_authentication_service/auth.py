#!/usr/bin/env python3
''' Hashed Module '''

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    ''' def hash password '''
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

