# Basic script to download MANGAS
This script will download images and store them by chapters from a KissManga link
with the name of your favorite manga.
Check the already tested samples and replace source and destination folder by yours.

## Installation

```
pip install virtualenv

python -m virtualenv venv --python=python3.8

source venv/bin/activate

pip install bs4
pip install requests
```


## Download your favorite mangas
Two parameters are enabled:

-p, --path: This is the folder where the chapters will be stored

-l, --link: The link to the manga in Kissmanga, e.g.: http://kissmanga.nl/manga/chainsaw-man

Example:

\>python manga_creator.py --path C:\chainsaw-man --link http://kissmanga.nl/manga/chainsaw-man

> ##### Downloading Collections
> 
> - If you want to download all the available collection, pass `full_collection` param as `True`
> - if you don'n need the full collection, pass `full_collection` param as `False` and pass the link or list of links you want to download to the source param


## Deployment
- Enable virtual environment
```
source venv/bin/activate
```
- Go to the folder where app.py is located
- Execute app.py
```
python manga_creator.py
```
