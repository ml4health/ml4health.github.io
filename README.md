This repository contains all the source materials for NIPS ML4Health workshop website. 

# Usage for 2021

Creating new folder for a new year
1. Copied the `2020_content` to `2021_content`.

# Usage for 2020

Creating new folder for a new year
1. Copied the `2019_content` to `2020_content`.
2. Alter in `Makefile` to put to year 2020. Change link in `./index.html`. Switch years in `pelicanconf.py`
3. Edit homepage in `2020_content/pages/00_index.md`. Remove pages you don't need right now. You can always recopy them from `2019_content`
4. Website should initially have dates, schedule, speakers, and organizers. Add call for papers when ready.

Editing an existing page
1. Make edits on page in `2020_content/pages/`
2. `make html` in root. `make serve` to check it looks fine. Then push to public.

Adding a page from the 2018 website
1. Copy over the page from `2018_content/pages/.` to `2019_content/pages/.`
2. If the page looks "complicated", check and see if there is a corresponding `make organizers` or something else in the `Makefile`. In that case, you're meant to update the corresponding csv first and then run `make organizers` or `make accepted_papers`. This will generate the static page from the input files.
3. `make html` in root. `make serve` to check it looks fine. Then push to public.

# FAQs

 - Want to change the order of pages in toolbar? Alphabetical by page filename, but make title in page the actual thing you want.
 - Images for organizers or speakers looking strange? Make sure all of the captions are the same length (same number of lines), otherwise it will throw off the spacing.

# Usage for 2018

```
$ make organizers   # Build the organizers page from .csv file of raw data
$ make html         # Build static site on local machine under 2018/ output folder
$ make serve        # Serve website locally. Point browser to: localhost:8000
```

To push any local changes to the real site, just push to origin (assuming origin = github.com/ml4health/ml4health.github.io)
```
$ git push origin master
```

Remember, only content that you've turned into proper HTML files inside 2017/ with `make html` will be displayed on the website. Edits to the markdown source files in 2017_content/ do *not* automatically become html when pushed.

Hint: Adjust SITEURL inside pelicanconf.py to get links right when building locally.

## Dependencies
* Pelican: http://blog.getpelican.com/
* Markdown

### With conda
```
$ conda install -c conda-forge pelican=3.7.0
$ conda install markdown
```

### With pip
```
$ pip install pelican
$ pip install markdown
```

### With virtualenv
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Usage for 2017 (historical)

All the 2017 Makefiles, etc are preserved in the "release_v2017" branch. 

```
$ git checkout release_v2017
$ make organizers   # Build the organizers page from .csv file of raw data
$ make html         # Build static site on local machine under 2017/ output folder
$ make serve        # Serve website locally. Point browser to: localhost:8000
```


## Theme

Uses custom theme already included in repo (themes/customized-pelican-alchemy/)

Based on Pelican-Alchemy (https://nairobilug.github.io/pelican-alchemy/)

## Changelog from default theme
* Resized header so logo is smaller (2 cols in bootstrap, not 4).
* Removed "Archives" and "Categories" menu items (this site wont have "posts", just "pages")
