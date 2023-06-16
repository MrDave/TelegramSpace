# Telegram Space

A collection of scripts designed to download images from SpaceX launches, NASA's [Astronomy Picture of the Day (APOD)](https://apod.nasa.gov/apod/astropix.html) and [Earth Polychromatic Imaging Camera (EPIC)](https://epic.gsfc.nasa.gov/) and to upload them (or other files) to a Telegram channel of your choice.

## Installing

Download the project to your local machine.

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

Using virtual environment [virtualenv/venv](https://docs.python.org/3/library/venv.html) is recommended for project isolation.

Scripts can be run as is, however to increase NASA's hourly/daily requests limit, obtaining [NASA API Key](https://api.nasa.gov/#signUp) is recommended. 

Store it in `.env` file in root folder of the project as "NASA_TOKEN"
```
NASA_TOKEN = 'abC12deFg345hi6gk78lMN9op012QRS345tuVw6xyz'
```

To upload images to a Telegram channel, bot access token is also needed as well as Telegram channel ID. Put them in the .env file along with the NASA token:
```
TG_BOT_TOKEN = '1234567890:AAEAtJ5Lde5YYfkjergber'
TG_CHANNEL_ID = '@YourChannel'
```
Bot token can be obtained [via BotFather bot](https://t.me/BotFather) and the bot itself should be added to said channel as an Admin


## Using the program

All scripts can be run from command line "as is" as well as with optional arguments.

Images are downloaded to a separate folder "images" which is automatically generated if it doesn't exist. 

### SpaceX Launch Images

Downloads images from SpaceX launches.
```commandline
python3 fetch_spacex_images.py
```

Optional arguments:  
`--id ID` - ID of SpaceX launch. By default, fetches latest launch.

Launches do not always contain photos. In case latest launch doesn't download images, try using a specific launch ID, such as `5eb87d42ffd86e000604b384`.

### NASA - Astronomy Picture of the Day (APOD)

Downloads today's APOD.
```commandline
python3 fetch_nasa_apod_images.py
``` 
By default, uses demo API key, but using personal API token is recommended.

Optional arguments:  
`-t, --token` - use personal NASA API Key token instead of the default one  
`-c COUNT, --count COUNT` - download multiple random APOD's

### NASA - Earth Polychromatic Imaging Camera (EPIC)

Downloads Hi-Res Earth images (at the moment works only with current day's images)

```commandline
python3 fetch_nasa_epic_images.py
```
By default, uses demo API key, but using personal API token is recommended.

Optional arguments:  
`-t, --token` - use personal NASA API Key token instead of the default one  
`-c [1-20], --count [1-20]` - number of images to download

### Uploading images to Telegram channel

#### All images
Uploads all images from `images` folder to a selected Telegram channel one by one in a random order. 

```
pyhton3 auto_upload.py
```

Optional arguments:  
`-t TIME, --time TIME` - set how often (in seconds) an image is uploaded

It is also possible to change default waiting time (in seconds) by putting a WAIT_TIME environmental variable in `.env`
```
WAIT_TIME = 14400
```
#### Single image
For a single manual upload, use `upload_telegram_picture.py`. If no argument given, uploads a random file from the `images` folder
```commandline
python3 upload_telegram_picture.py images/image.jpg
```
Optional arguments:  
`-f FILE, --file FILE` - path of specific file to upload. Example: "images\image.jpg"
## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
