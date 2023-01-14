# function to convert camelCase string to snake_case
def camel_to_snake(name):
    import re

    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def main(methods: list[str]):
    """
    update the README.md file with the methods that are implemented in pydate-fns
    """
    import os
    import re

    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pydate"))
    # print list all directories in current directory
    pydate_methods = [i for i in os.listdir() if os.path.isdir(i)]

    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    # print a text table with 3 columns, left aligned, 30 chars wide: method, pydate, date-fns
    table = ["<!-- methods -->", "", "### method", "", "---", ""]
    for method in sorted(methods):
        table.append(f"- [{'x' if camel_to_snake(method) in pydate_methods else ' '}] {method}")
    table.append("<!-- /methods -->")

    # update the README.md file
    with open("README.md", "r") as f:
        readme = f.read()
        updated = re.sub(r"<!-- methods -->.*<!-- /methods -->", "\n".join(table), readme, flags=re.DOTALL)

    with open("README.md", "w") as f:
        f.write(updated)


def scrape_date_fns():
    """
    scrape the date-fns github repo for the list of methods
    """
    import requests
    from bs4 import BeautifulSoup

    # Make a request to the URL
    response = requests.get("https://github.com/date-fns/date-fns/tree/main/src")

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the directories on the page
    directories = soup.select("span.css-truncate.css-truncate-target")

    # Extract the names of the directories
    names = {d.text for d in directories if not (d.text.startswith("\n") or d.text.startswith("_") or "." in d.text)}
    return names


if __name__ == "__main__":
    scraped_methods = scrape_date_fns()
    local_methods = main(list(scraped_methods))
