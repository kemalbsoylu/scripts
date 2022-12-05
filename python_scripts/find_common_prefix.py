def find_common_prefix(string_list):
    """Find common prefix from the list of strings.

    Args:
        string_list (list): a list of strings.

    Returns:
        str: common prefix or empty if there is none.
    """

    if not isinstance(string_list, list) or not all(isinstance(s, str) for s in string_list):
        raise ValueError("Input must be a list of strings.")

    if not string_list:
        raise ValueError("Empty lists are not allowed. Expecting list of strings.")

    common_prefix = string_list[0]

    for string in string_list[1:]:
        while not string.startswith(common_prefix):
            common_prefix = common_prefix[:-1]

    return common_prefix
