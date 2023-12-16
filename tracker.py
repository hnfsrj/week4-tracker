'''
When you run this software, it goes through your the directories and files under the directory of this python file
to collect all the files which have been modified within 24 hrs and keep them in a dedicated folder.

It then returns those files back to their original directory when their modification time exceeds 24 hrs

you can change the time from 24 hours to seconds or minutes according to your convinience
'''



import os
from datetime import datetime
import threading
import time


tracking = [] #this is the array which keeps all the files which are being tracked right now for being modified under the specified time
next_return = datetime.now().timestamp() + 30*3600 #the time to return the next file back to its original path

current_path = os.getcwd() #the path of this python file
destination_path = current_path + '\\' + 'last_24hrs' #the path of the 24 hrs foleder

last = 20 #change this to change the time of modification from 24 hrs to anything. The unit is second.

tracked = [] #the next file which is going to be returned back to its original path
go = True #when this is true then the return to original path function has a file to return back to its original path and if it is false then the 24 hrs folder is empty and the function will stop trying to return files back to origin


def initialize():
    #creates the last 24 hrs folder if it isnt available

    list_of_dirs = os.listdir()

    if 'last_24hrs' not in list_of_dirs:
        os.mkdir('last_24hrs')





def return_to_origin():
    # this function returns files to their original path ones their time in the 24hrs folder expires

    global next_return, tracking, tracked, go


    while True:
        if go: #if we have something to track in the tracking array
            if datetime.now().timestamp() >= next_return: #if the time is past the return to origin time of the file to be returned

                os.rename(destination_path + '\\' + tracked[0], tracked[1] + '\\' + tracked[0]) #return the file to its origin
                tracking.remove(tracked) #remove the file from the tracking array


                being_tracked = []

                if tracking != []:
                    next_return = tracking[0][2]
                    being_tracked = tracking[0]
                    for i in tracking:
                        if i[2] < next_return:
                            next_return = i[2]
                            being_tracked = i

                    tracked = being_tracked #setting the next file to be returned to origin
                else:
                    go = False #stop from trying to return files back to their origin if their is nothing being tracked
        

        time.sleep(1)




def append_to_tracking(path,file):
    #this function appends files modified under the specied time to the tracking array and also moves them to the 24 hrs folder

    global next_return, destination_path, current_path, tracked, go

    if path == current_path and 'tracker.py' in file: #this is to prevent tracking this python file
        file.remove('tracker.py')
    


    os.chdir(path)


    for i in file:
        mod_time = os.stat(i).st_mtime #modification time of the file we are working on
        duration = datetime.now().timestamp() - mod_time #how long has it been since it was modified

        if duration < last: #if the mod time duration of the file is under our specified time
            return_time = mod_time + last #the time when the file should return back to its original path

            tracking.append([i,path,return_time]) #append the file's name, original path and return to origin time to the tracking array

            source_path = path + '\\' + i
            
            os.rename(source_path, destination_path + '\\' + i) #move the file to the 24 hrs folder

            if go: #if the function has been running previously
                if return_time < next_return:
                    tracked = tracking[-1]
                    next_return = return_time

            else: #if the function wasnt running i.e the tracking array was empty for a while
                tracked = tracking[-1]
                next_return = return_time
                
                go = True


def collect_data():
    #checks all the directories within the directory of this python file to collect every file and send it to append_to_tracking function to be tracked if the file has been modified under the specified time

    global current_path

    for path, folder, file in os.walk(current_path):
        thepath = path.split('\\')

        if '.git' not in thepath: #we dont want to track git files
            if '\\'.join([thepath[i] for i in range(len(thepath)-1)]) == current_path: #if we are only one directory deep from the directory path of this python file

                if 'last_24hrs' not in thepath: #if this file is not in the last 24hrs folder. because we dont want to track the tracked again
                    append_to_tracking(path,file) #run the append to tracking function with the path and files under that path as parameters
            else:
                append_to_tracking(path,file)




initialize()
collect_data()


t = threading.Thread(target = return_to_origin)
t.start() #putting the return to origin function on its own thread since it is a separate function with its own sleep timer