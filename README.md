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


## Finding your favorite mangas
1. Open the manga_creator.py file
2. Go to the main section
3. Replace the source parameter by the link of your favorite manga in http://kissmanga.nl
4. Replace the destination parameter by a folder name to store the downloaded manga

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
