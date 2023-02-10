#!/usr/bin/env python3
"""
API authentication
"""

from flask import request
from typing import TypeVar, List

class Auth:
    """ 
    Authentication class 
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ 
        require authentication 
        """
        return False

    
    def authorization_header(self, request=None) -> str:
        """ 
        Authorisation Header
        """
        return None

    
    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user method """
        return None