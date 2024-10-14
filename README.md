# Homepage Icongrabber
Automatic favicon grabber for Homepage bookmarks. 

I wanted to add favicons to my bookmarks and tried to integrate that into Homepage myself but that caused a lot of slow downs; Here's a script to at least make it a bit easier. 

## Workings
The script will look for entries in `bookmarks.yaml` and grab the favicons for entries that do not yet have an icon defined. If the icon has been downloaded successfully, the entry will be updated with the icon. If the icon could not be downloaded, it can be replaced with a fallback of your choosing.  

## Setup
### Folder access
This script will download favicons for bookmarks in your `bookmarks.yaml` to a folder. This folder needs to be mapped to the public folder for your Homepage instance `/app/public`. If you are running a docker container, this can be done via your `docker-compose.yml` file:
```yaml
version: "3.3"

homepage:
  image: ghcr.io/gethomepage/homepage:latest
  container_name: homepage
  volumes:
    - /PATH/TO/CONFIG:/app/config
    - /PATH/TO/ICONS:/app/public/icons
  restart: unless-stopped
```
### Configuration
Set the user configurable values in `main.py`, these include:
- Icon download path
- `bookmarks.yaml` path
- Icon folder public URL 
- Fallback icon

Further explaination of the values above is given in `main.py`

### Install dependencies:
```bash
pip install grab-favicon pyyaml
```
or 
```bash
pip install -r requirements.txt
```

## Running
Simply run the script using python:
```bash
python ./src/main.py
```
The script has to be run every time you edit your bookmarks. You could put it on some sort of filesystem watcher or cron job but, unless you update your bookmarks a lot, I wouldn't recommend it. 

## Links
- [Homepage](https://github.com/gethomepage/homepage) by Homepage Contributors
- [grab-favicon](https://pypi.org/project/grab-favicon/) by Emilio Mendoza