===================================
Django TemplateLoaderWithPriorities
===================================

A django template loader that allows you to control the order which the template dirs (filesystem directories or apps' template directories) are resolved in.

Useful when you want to override 

====================
Installation and use
====================

Get ``loaderwithpriorities`` from pypy or github::

    $ pip install django-templateloaderwithpriorities

or::

    $ pip install -e git+git://github.com/qubird/django-templateloaderwithpriorities#egg=loaderwithpriorities

Once installed, put the loader in your settings::

    TEMPLATE_LOADERS = (
        'loaderwithpriorities.Loader',
        # ...
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader',
        # ...
    )

Be sure that it's the first item of ``TEMPLATE_LOADERS``, else your priorities will be ignored.

Then add ``TEMPLATE_LOADER_PRIORITIES`` in your settings, like::

    TEMPLATE_LOADER_PRIORITIES = [
        'my.app',
        '/path/to/my/custom/templates'
    ]

First come, first served... 
