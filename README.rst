==============
Django noJS
==============

Simple application to plug to manage "javascript disabled" browser


Installation
------------

Add :mod:`nojs` to your :setting:`INSTALLED_APPS`::

    INSTALLED_APPS = (
            ...,
            ...,
            'nojs',
        )

Add `django.core.context_processors.request` to your :setting:`TEMPLATE_CONTEXT_PROCESSORS`::

    TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.request",
                               "django.contrib.messages.context_processors.messages")

Into your templates::

    <link href="{{ STATIC_URL }}nojs/nojs.css" rel="stylesheet" type="text/css" media="screen" />

    {% checkjs %}

    