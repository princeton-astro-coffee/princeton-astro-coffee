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
    author_list = soup.find_all('ul', class_='people-info')
    headers = soup.find_all('div', class_='people-grid-image-container')
    lines = []
    for author, header in zip(author_list, headers):
        name = author.find('li', class_='people-grid-name-linked').text
        try:
            email = author.find('li', class_='people-grid-email').a.text
        except AttributeError:
            email = header.find('div', class_='file file-image file-image-jpeg file-people_grid_thumbnail_with_link').get('id')
        #print(name, email)
        lines.append(f"{name},{email}\n")
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


if __name__=='__main__':
    output_filename = 'static/images/AstroDeptList.csv'
    output_filename = sys.argv[1]
    auto_update_author_list(output_filename)
    webdb.purge_local_authors()
    webdb.add_local_authors(output_filename)
