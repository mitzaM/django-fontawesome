from django import template
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html

register = template.Library()

@register.simple_tag
def fontawesome_icon(icon, large=False, fixed=False, spin=False, li=False, rotate=False):

    return '<i class="fa fa-{icon} {large} {fixed} {spin} {li} {rotate}"></i>'.format(
        icon=icon,
        large='fa-lg' if large is True else '',
        fixed='fa-fw' if fixed else '',
        spin='fa-spin' if spin else '',
        li='fa-li' if li else '',
        rotate='fa-rotate-%s' % str(rotate) if rotate else ''
    )

@register.simple_tag
def fontawesome_stylesheet():
    href = getattr(settings, 'FONTAWESOME_CSS_URL', static('fontawesome/css/font-awesome.min.css'))
    link = format_html('<link href="{0}" rel="stylesheet" media="all">', href)
    return link