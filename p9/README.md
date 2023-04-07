# Youtube Video/Shorts CLI downloader
####  Video Demo   https://youtu.be/NDydNfr863c
####  About
        ## Mohammed Faizan
        ## CS50p
        # 03-03-2023

## Project structure :
---
* project.py
* test_project.py
* requirements.txt
* README.md


## Installing Libraries
---

there is a a requirements.txt file that has all the libraries used.

and simply can be install by this pip command:

```
pip install -r requirements.txt
```

##  Description
---
 PROGRAM THAT TAKES IN A VALID YOUTUBE URL OR A FILE CONTAINING URLS
 AND CONVERTS IT TO USER DESIRED VIDEO OR AUDIO FORMAT

1. Taking input from user and passing into validating url function
2. Takes that url and passes it through regex and checks for valid urls
        It return True for the following corner cases
* https://www.youtube.com/shorts/EHWqOUzFSxU
* http://www.youtube.com/shorts/EHWqOUzFSxU
* www.youtube.com/shorts/EHWqOUzFSxU
* youtube.com/shorts/EHWqOUzFSxU
3. If everything is fine then it returns the title of the video
4. Then this url is passed through Youtube class object, then fetches the available resolution options available
5. Then user is given choice to select his desired resolution from given list
6. Finally the video is download with given youtube video title name


## Usage
---
```python
__   __          _         _           __     ___     _
\ \ / /__  _   _| |_ _   _| |__   ___  \ \   / (_) __| | ___  ___
 \ V / _ \| | | | __| | | | '_ \ / _ \  \ \ / /| |/ _` |/ _ \/ _ \
  | | (_) | |_| | |_| |_| | |_) |  __/   \ V / | | (_| |  __/ (_) |
  |_|\___/ \__,_|\__|\__,_|_.__/ \___|    \_/  |_|\__,_|\___|\___/

 ____                      _                 _
|  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __
| | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
| |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |
|____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|


Youtube URL:
```
Here you have to paste a valid youtube url to download. If invalid is given then code exits

After entering url it shows title
```
Youtube URL: https://www.youtube.com/shorts/y9lMQVPJjZ4

Title:  CS50 Fair at Yale - CS50 Reels #Shorts
```

It asks the user for quality to donwload:
```
Available resolutions
  360p
  720p
```

After entering it will download.
```
Enter resolution to download: 360
Downloading...
Download completed!!
```

Special thanks to David J Malan and CS50 team
