from scraper import get_page_source

if __name__ == "__main__":
    link = "https://www.hometogo.com/opensearch?q=orlando,usa"

    page_source = get_page_source(link)

    print(page_source)