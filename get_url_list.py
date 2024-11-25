import logging


def get_url_list(categories, data_start, data_range):
    url_list = []

    # Счетчик для статей
    total_articles = 0

    for category in categories:
        iterations = int((data_range - data_start) / 10)
        query_range = [i + iterations for i in range(data_start, data_range, iterations)]
        query_range.insert(0, data_start)
        for i in range(len(query_range) - 1):
            url = f'http://export.arxiv.org/api/query?search_query=cat:{category}&start={query_range[i]}&max_results=10&sortBy=submittedDate&sortOrder=descending'
            url_list.append((category, url))  # Сохраняем категорию с URL

            # Увеличиваем счетчик статей на 10 (или меньше, если это последняя итерация)
            articles_to_add = min(10, query_range[i + 1] - query_range[i])
            total_articles += articles_to_add

    for category in categories:
        logging.info(f'Процесс завершен для категории "{category}". Количество статей: {total_articles}')

    return url_list
