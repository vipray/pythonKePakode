#Extract_Date_from_Image.py
from PIL import Image
from File_name_Collector import allFileName #self made
import os

#function to get Date of Image Captured
def get_date_taken(path):
    return Image.open(path)._getexif()[36867]

for f in allFileName():
    print(f)
    try:
        Date_time = get_date_taken(f);
        #print("Date and Time of Image:-> "+Date_time)
        #split the result by :
        DateSplit = Date_time.split(":")
        #print("hh:"+str(f))
        
        #saperation directory path and file name
        try:
            dirPath = f.split("\\")[0]
            fileName = f.split("\\")[1]
        except:
            dirPath = os.getcwd()
            fileName = f 
        
        #store Year and month to make different nested folders 
        directoryYear = dirPath+"/"+DateSplit[0];
        directoryMonth = DateSplit[1];

        #make nested path and change name of file by its date
        #newPath = directoryYear+"/"+directoryMonth+"/"+fileName+".JPG"
        ''' need to find soln for same date images for above line
            so using natural number to name the images for now
        '''
        newPath = directoryYear+"/"+directoryMonth+"/"+(fileName)
        print("New-->"+newPath)

        #check if this year folder exist if not,make it
        if not os.path.exists(directoryYear):
            os.makedirs(directoryYear)

        #check if this month folder inside year folder exist if not,make it
        if not os.path.exists(directoryYear+"/"+directoryMonth):
            os.makedirs(directoryYear+"/"+directoryMonth)

        #Replace the file to the new location
        os.replace(f, newPath)
    except:
        print(f+"-->Bad File")
