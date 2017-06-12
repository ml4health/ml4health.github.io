# This repository contains all the source materials for draft website for NIPS ML4Health workshop website. 

Usage
-----

```
$ make html         # Build static site on local machine under output/
$ make serve        # Serve website locally. Point browser to localhost:8000
$ make rsync_upload # TODO this doesnt work yet, but will once we setup a server
```

Dependencies
-----
* Pelican: http://blog.getpelican.com/

```
pip install pelican
```

Theme
-----

Uses custom theme already included in repo (themes/customized-pelican-alchemy/)

Based on Pelican-Alchemy (https://nairobilug.github.io/pelican-alchemy/)

Changelog from default theme
----------------------------
* Resized header so logo is smaller (2 cols in bootstrap, not 4).
* Removed "Archives" and "Categories" menu items (this site wont have "posts", just "pages")
