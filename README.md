### Prayer Time Audio Pause
A python script that pauses the audio on praying times.
***
## Prerequisites
* [Python 3.9](https://www.python.org/downloads/release/python-399/) ( 3.10 version have issues with installing **winrt** library )  
***
## Installation Process  
1. Change the file path in the main file 
![](https://github.com/HusseinSamy/PrayerTimesAudioPause/blob/main/gifs/ChangDeirectoryInMainFile.gif)
2. Run the **intall requirements** file
![](https://github.com/HusseinSamy/PrayerTimesAudioPause/blob/main/gifs/InstallRequirements.gif)
***
## Run the script manually
* Run the vbs file
![](https://github.com/HusseinSamy/PrayerTimesAudioPause/blob/main/gifs/OpenVbsFile.gif)
***
## Run the script on windows startup 
* Open run ```(win + R)```
* Type ```regedit``` and press enter
* Go to ``` Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run ```
* Right click and create a new string value 
![](https://github.com/HusseinSamy/PrayerTimesAudioPause/blob/main/gifs/CreateNewStringValue.gif)
* Modify the string value to the file path of the .vbs file in the project folder
![](https://github.com/HusseinSamy/PrayerTimesAudioPause/blob/main/gifs/ModifyTheValueData.gif)
