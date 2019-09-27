def create_query(languages, stars):
    """Builds the query string

    Arguments:
        languages {list} -- the list of languages
        stars {int} -- the minimum number of stars

    Returns:
        {str} -- the built query string
    """

    query = f"stars:>{stars} "

    for language in languages:
        query += f"language:{language} "

    return query


def build_parameters(languages, sort, order, stars):
    """Builds the request parameters

    Arguments:
        languages {list} -- the list of languages
        sort {str} -- the sort condition
        order {str} -- the order pattern
        stars {int} -- the minimum number of stars

    Returns:
        {str} -- the built query string
    """
    query = create_query(languages, stars)

    return {"q": query, "sort": sort, "order": order}
