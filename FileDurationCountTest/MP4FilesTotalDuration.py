from moviepy.editor import VideoFileClip
import os

# to get clip duration time in seconds
def getLength(filename):
    clip = VideoFileClip(filename)
    return clip.duration

#convert seconds into Days Hours minutes seconds
def ConvertSectoDay(n): 
    day = n // (24 * 3600); 
    n = n % (24 * 3600); 

    hour = n // 3600; 
    n = n % 3600; 
    
    minutes = n // 60 ; 
    n = n % 60; 
    
    seconds = n; 

    print("Days: " +str(day)+ " Hour: "+str(hour)+" min: "+str(minutes)+" sec: "+str(seconds));  

timeInSec=0;

for path, subdirs, files in os.walk('.'):
    for f in files:
        print(f)
        if(f.endswith('.mp4')):
            timeInSec= timeInSec + getLength(f)

timeInSec=int(timeInSec)

ConvertSectoDay(timeInSec);