import csv
import os

path = '/home/zippo/MEDIA/video/Star Trek The Next Generation/'
files = os.listdir(path)

with open ('Untitled 2.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'{", ".join(row)}')
            line_count =+ 1
        else:
            StripSeason = (f'\t {row["Season"]}').rstrip().lstrip()
            StripEp= (f'\t {row["EpSeason"]}').rstrip().lstrip()
            StripTitle = (f'\t {row["Title"]}').rstrip().lstrip()
            StripEpTotal = (f'\t {row["EpTotal"]}').rstrip().lstrip()
            NewName = (f'Star Trek The Next Generation - S{StripSeason} - Ep {StripEp} - {StripTitle}.mp4')
            #print(NewName)
            for f in files:
                if int(f.split(" ", 1)[0]) == int(StripEpTotal):
                    oldname = path + f
                    newname = path + NewName
                    print (oldname, " --> ", newname, "\n")
                    os.rename(oldname, newname)
                    



           