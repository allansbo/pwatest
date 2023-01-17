from django import template

register = template.Library()


@register.filter
def filtered_list(full_list: list, arg: str) -> list:
    """
    This function will return a list of tasks that
    only have the same status as the received argument
    Example: [Task1(done), Task2(doing), Task3(doing)] and arg='done'
    return: A list filtered by the arg
    """
    new_list = []
    for value in full_list:
        if value.status == arg:
            new_list.append(value)

    return new_list

