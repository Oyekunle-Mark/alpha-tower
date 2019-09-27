def create_query(languages, stars):
    query = f"stars:>{stars} "

    for language in languages:
        query += f"language:{language} "

    return query


def build_parameters(languages, sort, order, stars):
    query = create_query(languages, stars)

    return {"q": query, "sort": sort, "order": order}
