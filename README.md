# Python Music Player
## Goal
My goal was to develop a fun program and enhance my skills in Pyqt5,pygame,python skills.. This is a multi-threaded MP3 music player, which lets you enjoy your music with awesome features such as random mode and etc. I've used multi-threading and synchronization techniques to achieve some features.

## How it works

-First you have to set up a very simple database shown like below:

-After setting up a database, create a file named `dB-Connection.txt` in current dir and write your database credentials in it according to mysql.connector.connect method(user,password,host,database).The program will read that file and connect to the database if the connection is established correctly.File example below:

-To add music, create a folder named `musics` in current dir, and put your .mp3 files in this `musics` folder.

-When you press the Add Music button or use Ctrl+O shortcut and add a music in suggested way, the music will be added to the database.

-You can add images for these musics. To do that, create a folder named `music-images` in current dir, and put your .png files in this `music-images` folder.

-Use Ctrl+Y shortcut or click the top-left most button Add, and then choose `Add Music Image`.It will upload the image file to the database.

-When you are done setting up your playlist, you can enjoy your musics with features like below.

## Features : What is working?

* Play music, pause music
* Rewind 15 seconds backwards
* Skip 15 seconds forwards
* Next music, Previous music. These features work with random mode as well.
* Random Mode.You can enjoy playing your playlist in random order
* Progress Bar. When the progress bar is finished, it will automatically change to the next music(Or next music in the random playlist).
* Sound settings
* Add music, delete music
* Add music image

## To run this program...

Requirements are:

* PyQt5
* Pygame 1.9 or above
* Python 3.7 or above
* Mysql.connector


## Credits
* REWIND BACK,REWIND FORWARD,PLAY BUTTON : "Icon made by Freepik from www.flaticon.com"
  https://www.flaticon.com/free-icon/play-button_375

* "Icon made by Freepik from www.flaticon.com"
https://www.flaticon.com/free-icon/next_2088535?term=next%20icon&page=1&position=5
* "Icon made by Those Icons from www.flaticon.com"
* For:delete,previous,next
https://www.flaticon.com/free-icon/music_1765334?term=add%20music&page=1&position=4
* "Icon made by Icongeek26 from www.flaticon.com"
https://www.flaticon.com/free-icon/exchange_569681?term=shuffle&page=1&position=4
* "Icon made by Smartline from www.flaticon.com"
https://www.flaticon.com/free-icon/shuffle_2611564
* "Icon made by Freepik from www.flaticon.com"

* For:Volume
 https://www.flaticon.com/free-icon/volume_727269?term=volume&page=1&position=2
* For:Pause
https://www.flaticon.com/free-icon/pause_633940?term=music&page=1&position=53

## Contact
Feel free to contact me at `yektabuyukkaya@outlook.com`.
