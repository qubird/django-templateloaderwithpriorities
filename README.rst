===================================
Django TemplateLoaderWithPriorities
===================================

A django template loader that allows you to control the order which the template dirs (filesystem directories or apps' template directories) are resolved in.

Useful when you want to override third party apps templates.

====================
Installation and use
====================

Get ``templateloaderwithpriorities`` from pypy or github::

    $ pip install django-templateloaderwithpriorities

or::

    $ pip install -e git+git://github.com/qubird/django-templateloaderwithpriorities#egg=templateloaderwithpriorities

Once installed, put the loader on top of ``settings.TEMPLATE_LOADERS``::

    TEMPLATE_LOADERS = ('templateloaderwithpriorities.Loader', ) + TEMPLATE_LOADERS

Be sure that it's the first item of ``TEMPLATE_LOADERS``, else your priorities will be ignored.

Then add ``TEMPLATE_LOADER_PRIORITIES`` to your settings.py::

    TEMPLATE_LOADER_PRIORITIES = [
        'my.app',
        '/path/to/my/custom/templates'
    ]

The loader searches for templates in the given order, looking for the ``templates`` directory if the item is an app, or the directory itself if the item is an absolute path.

First come, first served.
