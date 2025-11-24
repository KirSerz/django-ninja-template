from django.contrib import messages


def message_user(
    request,
    message,
    level=messages.INFO,
    extra_tags='',
    fail_silently=False
):
    if not isinstance(level, int):
        # attempt to get the level if passed a string
        try:
            level = getattr(messages.constants, level.upper())
        except AttributeError:
            levels = messages.constants.DEFAULT_TAGS.values()
            levels_repr = ', '.join('`%s`' % level for level in levels)
            raise ValueError(
                'Bad message level string: `%s`. Possible values are: %s'
                % (level, levels_repr)
            )

    messages.add_message(request, level, message, extra_tags=extra_tags, fail_silently=fail_silently)
