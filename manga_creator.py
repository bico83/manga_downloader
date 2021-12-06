import argparse
import os
import re
from bs4 import BeautifulSoup
import requests


def get_manga(full_collection=True, source=None, dest=None):
    # Get the url of available chapters in a link with available chapters
    try:
        if full_collection:
            chapters_url = get_url_of_available_chapters(source)
        else:
            if type(source) is list:
                chapters_url = source
            elif type(source) is str:
                chapters_url = list()
                chapters_url.append(source)
            else:
                return 'Fail', \
                       'source should be a link to page with the list of chapters, ' \
                       'a list with the links of chapters you want to download or, ' \
                       'the link of the chapter you want to download'
    except Exception as e:
        return e, 'source was not passed or is invalid'

    # Get the indexes of chapters to download
    try:
        chapters_ids = get_indexes_of_available_chapters(chapters_url)
    except Exception as e:
        return e, 'source link probably does not contain the number of chapter or page'

    try:
        # Get books and store them by book
        get_images_per_chapter(chapters_url, chapters_ids, dest)
    except Exception as e:
        return e, 'destination folder was not passed or is invalid'


def get_url_of_available_chapters(source):
    href_class_name = source.split('/')[-1] + '-chapter'
    req_result = requests.get(source)
    page_content = BeautifulSoup(req_result.content, 'html.parser')
    classes = page_content.find_all(href=re.compile(href_class_name))
    urls = list(set([x.attrs['href'] for x in classes]))
    return urls


def get_indexes_of_available_chapters(available_chapters):
    indexes = [x.split('-')[-1] for x in available_chapters]
    return [x.split('#')[0] for x in indexes]


def get_images_per_chapter(chapters_url, chapter_ids, dest):
    # Match chapter_url with chapter_id in order to name folders
    for chapter_url, chapter_id in zip(chapters_url, chapter_ids):
        # Get urls of pages
        req_result = requests.get(chapter_url)
        if req_result.status_code == 200:
            page_content = BeautifulSoup(req_result.content, 'html.parser')
            classes = page_content.find(id='arraydata')
        else:
            continue

        # Save images in the destination
        urls = classes.text.split(',')
        for id, url in enumerate(urls):
            response = requests.get(url)
            folder = os.path.join(dest, f'chapter_{chapter_id}')
            file = os.path.join(folder, f'image_{id}.jpg')
            if not os.path.isdir(folder):
                os.mkdir(folder)
            if response.status_code == 200:
                if not os.path.isfile(file):
                    with open(file, 'wb') as f:
                        f.write(response.content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path',
                        help='Path where the book will be downloaded to')
    parser.add_argument('-l', '--link',
                        help='link to kissmanga book')
    args = parser.parse_args()

    # Download manga full collection
    get_manga(source=args.link,
               dest=args.path)

    # get_manga(source=f'http://kissmanga.nl/manga/naruto-full-color',
    #           dest=f'/Users/miguelpalos/Downloads/miguel_palos/mamadas_de_bico/')

    #get_manga(source=f'http://kissmanga.nl/manga/cowboy-bebop',
    #          dest=f'/Users/miguelpalos/Downloads/miguel_palos/mamadas_de_bico/')

    # Download a single chapter of the whole manga
    # get_manga(full_collection=False,
    #           source='http://kissmanga.nl/naruto-full-color-chapter-175#1',
    #           dest=f'/Users/miguelpalos/Downloads/miguel_palos/mamadas_de_bico')

    # Download a bunch of chapters
    # get_manga(full_collection=False,
    #           source=['http://kissmanga.nl/naruto-full-color-chapter-158',
    #                   'http://kissmanga.nl/naruto-full-color-chapter-159'],
    #           dest=f'/Users/miguelpalos/Downloads/miguel_palos/mamadas_de_bico')
