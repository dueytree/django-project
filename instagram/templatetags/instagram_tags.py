from django import template

register = template.Library()


@register.filter
def is_likeuser(post, user):
    return post.is_likeuser(user)