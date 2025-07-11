import urllib.parse

from django.http import HttpResponseRedirect
from django.urls import reverse


def redirect_with_get_params(viewname, **kwargs):
    rev = reverse(viewname)

    params = urllib.parse.urlencode(kwargs)
    if params:
        rev = f"{rev}?{params}"

    return HttpResponseRedirect(rev)
