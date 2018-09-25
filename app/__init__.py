# -*- coding: utf-8 -*-
"""
Python bare project.

:copyright: (c) 2018 by 0xGeist
"""
import logging
from logging import NullHandler
from .app import BareClass

logging.getLogger(__name__).addHandler(NullHandler())
