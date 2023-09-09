from django import template

register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    """
    Replaces a specified field of the request,
    primarily used for links to paginated search results.
    E.g. {% url_replace request 'page' (wanted page number) %}

    Code from https://stackoverflow.com/a/67526160 by Mojtaba Arezoomand
    """
    dict_ = request.GET.copy()
    dict_[field] = value

    return dict_.urlencode()
