from bs4 import BeautifulSoup
import requests
import sys
import webdb

def _scrape_authors(url):
    """
    Scrape local authors from a given URL of Princeton astro webpages.

    This function is specific to Princeton astro webpages. Other
    department/institution webpages may have different tags.
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    authors = soup.find_all('div', class_='content-list-item feature-is-3x4')
    lines = []
    for author in authors:
        name = author.find('span', class_='field field--name-title field--type-string field--label-hidden').text
        try:
            email = author.find('div', class_=('field field--name-field-ps-people-email field--type-email '
                                               'field--label-inline clearfix')).find('div', 'field__item').text
        except AttributeError:
            email = author.find('span', class_='field field--name-title field--type-string field--label-hidden').a['href']
	name = name.encode('utf-8')
	email = email.encode('utf-8')
        lines.append("{0},{1}\n".format(name, email))
    return lines

def auto_update_author_list(output_filename='static/images/AstroDeptList.csv'):
    """
    Scrape from the Princeton astro webpages and output a CSV file.

    This function scrapes from the following list of pages:
    - Faculty & Research Scholars
    - Postdoctoral Research Staff
    - Graduate Students
    - Undergraduate Students

    Department staff and Assoc. Faculty & Dept. Affiliates are not included.

    The list of people and their email address (if available) is output to a
    CSV file.
    """
    pages = (
             "https://web.astro.princeton.edu/people/astronomy-Faculty%20and%20Research%20Scholars",
             "https://web.astro.princeton.edu/people/postdocs-researchers",
             "https://web.astro.princeton.edu/people/graduate-students",
             "https://web.astro.princeton.edu/people/undergraduate-students",
    )
    lines = []
    for page in pages:
        lines += _scrape_authors(page)

    with open(output_filename, 'w') as f:
        f.writelines(lines)

    return len(lines)


if __name__=='__main__':
    output_filename = sys.argv[1]
    nauthors = auto_update_author_list(output_filename)
    if nauthors > 0:
        webdb.purge_local_authors()
        webdb.add_local_authors(output_filename)
