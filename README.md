### About the script
I have always had a problem when it comes to listening to music; in most of the times I am listening to music and there is an Azan, I miss out hearing it because of the music. 

So I have came up with this python script that fetches Azan times from an API and pause the music automatically and give you a notification that it's a prayer time and automatically play the music again after the Azan is finished. (for windows only).
***
## Prerequisites
* [Python 3.9](https://www.python.org/downloads/release/python-399/) ( 3.10 version have issues with installing **winrt** library )  
***
## Installation Process  
1. Run the **intall requirements** file
![](https://github.com/HusseinSamy/PrayerTimesAudioPause/blob/main/gifs/InstallRequirements.gif)
***
## Run the script manually
* Run the vbs file
![](https://github.com/HusseinSamy/PrayerTimesAudioPause/blob/main/gifs/OpenVbsFile.gif)
***
## Run the script on windows startup 
### Windows registry editor
You can use windows registry editor to run the script on windows startup as follows:

* Open run ```(win + R)```.
* Type ```regedit``` and press ```enter```.
* Go to ``` Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run ```.
* Right click and create a new string value.
![](https://github.com/HusseinSamy/PrayerTimesAudioPause/blob/main/gifs/CreateNewStringValue.gif)
* Modify the string value to the file path of the .vbs file in the project folder
![](https://github.com/HusseinSamy/PrayerTimesAudioPause/blob/main/gifs/ModifyTheValueData.gif)
### Widows startup file 
Or you can also use the startup folder to achieve the same goal as follows: 
* Create a shortcut to the ```.vbs``` file in the directory. 
* Open run ```win + R```.
* Type ```shell:startup``` and press ```enter```.
* Move the shortcut that you have made to the ```startup``` folder.
![](https://github.com/HusseinSamy/PrayerTimesAudioPause/blob/main/gifs/CreateShortCut.gif)
