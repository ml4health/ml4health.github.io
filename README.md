This repository contains all the source materials for NIPS ML4Health workshop website. 

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
