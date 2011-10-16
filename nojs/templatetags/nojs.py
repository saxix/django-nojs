#
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.http import urlencode, urlquote
from django.utils.translation import gettext

__author__ = 'sax'

from django import template

register = template.Library()


# <img align="absmiddle" src = "%(static)snojs/error.gif">
@register.simple_tag(takes_context=True)
def checkjs(context, auto_redir= -1):
    """
        Write html code to handle javascript disabled browser.

        auto_redir :if > 0 enable "meta...refresh" code after <auto_redir> seconds. <b>Does not work on Chrome</b>
    """
    url = "%s?page=%s" % (reverse( 'nojs', ), urlquote(context['request'].path, ''))

    redir = ''
    if auto_redir >=0:
        redir = '''<noscript><meta http-equiv="refresh" content="%s; url=%s"></noscript>''' % (auto_redir, url)

    return  r"""<div id="nojs-js-off">&nbsp;&nbsp;%(message)s. <a href="%(url)s">%(link)s</a> %(help)s</div>
<script type="text/javascript">document.getElementById('nojs-js-off').style.display = 'none';</script>%(redir)s
""" % {'url': url,
       'message': gettext('Javascript Is Not Enabled'),
       'link': gettext('Click here'),
       'redir' : redir,
       'help': gettext('to get the instructions to reactivate Javascript in your web browser'),
       'static': settings.STATIC_URL}
