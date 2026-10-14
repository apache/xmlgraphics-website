# Apache XML Graphics website

Source for the [Apache XML Graphics](https://xmlgraphics.apache.org/) website
(FOP, Batik and XML Graphics Commons). The site is built with
[Pelican](https://getpelican.com/) from the Markdown (`.mdtext`) files under
`content/`.

## Prerequisites

- Python 3
- The build dependencies:

      pip install -r requirements.txt

## Build and preview locally

1. Build the site into `output/`:

       pelican content -s pelicanconf.py -o output

2. Serve `output/` over HTTP on port 8000:

       pelican -l -o output -s pelicanconf.py

3. Open the site in your browser, for example:

   - <http://localhost:8000/> — site home
   - <http://localhost:8000/fop/2.12/releaseNotes_2.12.html> — a specific page

While editing, you can build, serve and auto-rebuild on changes in one command
(then just refresh the browser):

    pelican -lr content -s pelicanconf.py -o output

**Note:** `SITEURL` is empty and `RELATIVE_URLS` is off, so pages use
root-relative links (`/fop/...`, `/images/...`). Open the pages through the
local HTTP server above rather than with `file://`, otherwise links, CSS and
images will not resolve. (Setting `RELATIVE_URLS = True` in `pelicanconf.py`
makes `file://` work, but serving over HTTP matches the live site.)

## Layout

- `content/` — the page sources (`content/fop/`, `content/batik/`,
  `content/commons/`, ...)
- `theme/` — templates and static assets
- `pelicanconf.py` — Pelican configuration (current versions, Markdown setup)
- `output/` — generated site (not committed)
