"""
Wrapper for loading templates based on a priority list
"""

import os
import sys

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.template.base import TemplateDoesNotExist
from django.template.loader import BaseLoader
from django.utils._os import safe_join
from django.utils.importlib import import_module


def get_template_dirs():
    """
    Returns the list of directories to search ordered by priorites set on
    settings.TEMPLATE_LOADER_PRIORITIES
    """
    fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()
    template_dirs = []
    if not hasattr(settings, 'TEMPLATE_LOADER_PRIORITIES'):
        raise ImproperlyConfigured(
            "settings.TEMPLATE_LOADER_PRIORITIES must be defined "
            "to use loaderwithpriorities.Loader")
    for item in settings.TEMPLATE_LOADER_PRIORITIES:
        # find if the item is a path or a module
        try:
            mod = import_module(item)
            is_app = True
        except:
            is_app = False
        if not is_app:
            is_dir = os.path.isdir(item)
        if is_app:
            template_dir = os.path.join(os.path.dirname(mod.__file__),
                                        'templates')
            template_dirs.append(template_dir.decode(fs_encoding))
        elif is_dir:
            template_dirs.append(item)
        else:
            raise ImproperlyConfigured(
                'Error loading TEMPLATE_LOADER_PRIORITIES: '
                '%s is neither an app nor an absolute directory' % item
            )
    return template_dirs

# Cache the directories to search.
cached_template_dirs = tuple(get_template_dirs())


class Loader(BaseLoader):
    is_usable = True

    def get_template_sources(self, template_name, template_dirs=None):
        """
        Returns the absolute paths to "template_name", when appended to each
        directory in "template_dirs".
        Directories are take from cached_template_dirs if template_dirs is not
        specified.
        """
        if not template_dirs:
            template_dirs = cached_template_dirs
        for template_dir in template_dirs:
            try:
                yield safe_join(template_dir, template_name)
            except UnicodeDecodeError:
                # The template dirname was a bytestring that wasn't valid UTF-8
                raise
            except ValueError:
                # The joined path was located outside of this particular
                # template_dir (it might be inside another one, so this isn't
                # fatal).
                pass

    def load_template_source(self, template_name, template_dirs=None):
        tried = []
        filepaths = self.get_template_sources(template_name, template_dirs)
        for filepath in filepaths:
            try:
                with open(filepath) as f:
                    return (f.read().decode(settings.FILE_CHARSET), filepath)
            except IOError:
                tried.append(filepath)
        if tried:
            msg = "Tried %s" % tried
        else:
            msg = "settings.TEMPLATE_LOADER_PRIORITIES is empty"
        raise TemplateDoesNotExist(msg)

    load_template_source.is_usable = True

_loader = Loader()
