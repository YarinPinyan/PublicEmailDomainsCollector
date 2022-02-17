import requests
from bs4 import BeautifulSoup

GITHUB_FREE_EMAIL_DOMAIN_URL: str = "https://gist.github.com/ammarshah/f5c2624d767f91a7cbdc4e54db8dd0bf"
HTML_QUERY: str = '[class*="blob-code blob-code-inner js-file-line"]'


def collect() -> set:
    ret_val: set = set()

    data = requests.get(GITHUB_FREE_EMAIL_DOMAIN_URL)
    HTML = BeautifulSoup(data.text, "html.parser")

    html_filtered = HTML.select(HTML_QUERY)
    for html_tag in html_filtered:
        ret_val.add(html_tag.text)

    return ret_val
  

def main():
  return collect()

if __name__ == "__main__":
  main()
