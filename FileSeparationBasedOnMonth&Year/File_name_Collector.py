#File_name_Collector.py
import glob

def allFileName():
    txtfiles = []
    for file in glob.glob("*.JPG"):
        txtfiles.append(file)

    return txtfiles

#print(allFileName())
