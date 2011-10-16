==============
Django noJS
==============

Simple application to plug to manage "javascript disabled" events


Installation
------------

Add `nojs` to your `INSTALLED_APPS`::

    INSTALLED_APPS = (
            ...,
            ...,
            'nojs',
        )

Add `django.core.context_processors.request` and `django.core.context_processors.static` to your `TEMPLATE_CONTEXT_PROCESSORS`::

    TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.request",
                               "django.contrib.messages.context_processors.messages")

Into your templates::

    <link href="{{ STATIC_URL }}nojs/nojs.css" rel="stylesheet" type="text/css" media="screen" />

    <body>
    {% checkjs %}
    </body>

    