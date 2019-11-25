import inkml2img
from os import listdir
from os.path import isfile, join

originalpath = '/home/shchae7/CV/data/original/CROHME2013_data/TrainINKML/MfrDB/'
convertpath = '/home/shchae7/CV/data/converted/CROHME2013_data/TrainINKML/MfrDB/'

onlyfiles = [f for f in listdir(originalpath) if isfile(join(originalpath, f))]

for files in onlyfiles:
    temp = convertpath + files
    temp = temp[:-6]
    inkml2img.inkml2img(originalpath + files, temp + '.png')
    #print(temp[:-5])


#inkml2img.inkml2img('./200923-1556-49.inkml', './test.png')
