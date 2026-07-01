from app.models.article import Article


def remove_duplicates(articles: list[Article]) -> list[Article]:
    """
    Remove duplicate articles using link first, then title.
    """

    unique_articles = []
    seen_links = set()
    seen_titles = set()

    for article in articles:

        # Skip duplicate links
        if article.link and article.link in seen_links:
            continue

        # Skip duplicate titles
        if article.title and article.title in seen_titles:
            continue

        if article.link:
            seen_links.add(article.link)

        if article.title:
            seen_titles.add(article.title)

        unique_articles.append(article)

    return unique_articles