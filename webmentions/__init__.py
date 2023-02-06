class WebmentionCollection:
    pass


class SearchAdaptorBase:
    pass


def search(search_adaptor: SearchAdaptorBase) -> WebmentionCollection:
    return WebmentionCollection()
