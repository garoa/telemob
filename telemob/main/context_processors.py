# -*- coding: utf-8 -*-

from django.conf import settings


def google_tag_manager(request):
    return {'GTM_CONTAINER': settings.GTM_CONTAINER}
