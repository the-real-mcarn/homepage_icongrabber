from grab_favicon import download_favicon, download_favicons
from urllib.parse import urlparse
import yaml
import os
import filecmp

'''
Path where icons will be saved
Make sure the folder exists prior to running this script and the script is able to write to the folder
'''
icon_path = os.path.join(os.getcwd(), "test/icons/")

'''
Path to your bookmarks.yaml file
Make sure the script can write to the file
'''
config_path = os.path.join(os.getcwd(), "test/bookmarks.yaml")

'''
URL prefix for the icons;
If you mapped your first icon folder to /app/public/icons/ then the URL prefix would be /icons/
'''
url_prefix = "/icons/"

'''
Fallback icon
If the script is unable to download the icon from the website, it will use this icon instead.
This can be any valid string that could be used in homepage. 

You are advised to use a fallback icon, since it will be themed along with the rest of your homepage. 
If left empty, the google default icon will be used
'''
fallback_icon = "mdi-web"

### End of configuration ###
C_INFO = "\u001b[96m*INFO*\u001b[0m\t"  # Info          - Cyan
C_WARN = "\u001b[33m*WARN*\u001b[0m\t"  # Warning       - Orange
C_ERR  = "\u001b[31m*ERR*\u001b[0m\t"   # Error         - Red
C_USER = "\u001b[35m*USER*\u001b[0m\t"  # User input    - Purple
C_DONE = "\u001b[32m*DONE*\u001b[0m\t"  # Done          - Green
C_DBUG = "\u001b[94m*DBUG*\u001b[0m\t"  # Debug         - Blue

counter_total = 0
counter_warning = 0

print("Homepage Favicon Downloader\nthe-real-mcarn, 2024")

# Find homepage config file
with open(config_path, 'r') as file:
    # Load bookmark file
    bookmarks = yaml.safe_load(file)
    
    # Cycle through categories and urls
    for categories in bookmarks:
        for category in categories:
            for site in categories[category]:
                for url in site:
                    if "icon" in site[url][0]:
                        continue
                    
                    href = site[url][0]["href"]
                    hostname = urlparse(href).hostname
                    filename = hostname + ".png"
                    
                    print("\n" + C_INFO, "Downloading", hostname)
                    download_favicon(url=hostname, path=icon_path, size=32, silent=0)
                    counter_total += 1
                    
                    # Check if the resulting file is the google default, throw an error and use a default icon
                    if filecmp.cmp(icon_path + filename, os.path.join(os.getcwd(), "res/default.png")):
                        print(C_WARN, "Failed to download", hostname)
                        counter_warning += 1
                        
                        if fallback_icon != "":
                            print(C_INFO, "Using fallback icon:", fallback_icon)
                            site[url][0]["icon"] = fallback_icon
                            continue
                        else:
                            print(C_WARN, "No fallback icon set, using Google default")
                        
                    site[url][0]["icon"] = url_prefix + filename
    
    # Write the updated bookmark file
    with open(config_path, 'w') as file:
        yaml.dump(bookmarks, file)
        
    if counter_total > 0:
        print("\n" + C_INFO, "Downloaded", counter_total, "icon(s),", counter_warning, "failed")
    else:
        print("\n" + C_WARN, "No new icons to download")
    
    print(C_DONE, "Done")