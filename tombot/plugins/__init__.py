'''
Provides the plugin infrastructure and some helper functions for plugins.
'''
import os.path
import logging
import importlib
from .registry import COMMANDS, get_easy_logger


LOGGER = get_easy_logger('tombot.moduleloader')

def load_plugins():
    '''
    Import all plugins.
    '''
    root = os.path.dirname(__file__)
    LOGGER.info('Loading plugins from %s', root)
    for dummy, dummy, files in os.walk(root):
        for ffile in files:
            if ffile.endswith('_plugin.py'):
                modulename = ffile.strip('.py')
                LOGGER.info('Initializing plugin %s', modulename)
                importlib.import_module('.' + modulename, package=__name__)
