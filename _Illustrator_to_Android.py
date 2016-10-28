#Android file sorter for illustrator exports
#By: Jorge Bautista <jorgebautista@gmail.com>
#This utility allows you to arrange the exported resources from illustrator for android 
#application development. The script removes the extra information on the file names and
#put each file on the correct folder.
#
#


import glob, re, os
from shutil import move,copy2

#Directories to be created
folders=['mipmap-xxxhdpi','mipmap-xxhdpi','mipmap-xhdpi','mipmap-hdpi','mipmap-mdpi','mipmap-ldpi']

#absoluthe path to our location
main_folder=os.path.dirname(__file__)

#loop to create directories in case they don't exists
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

#array with the extensions needed to clasify the different files
extensions=['xxxhdpi.png','xxhdpi.png','xhdpi.png','hdpi.png','mdpi.png','ldpi.png']    

#loop to check all the files in the folder
for filename in glob.glob('*.png'):


#loop through the different extensions and clasify the file
    for x in range(0, 6):
        
        #Check if the file name contains that extension        
        if extensions[x] in filename:
            
           #dst will have our destination folder hdpi, xhdpi etc.
            dst=folders[x]+'/'

            #new name for our file (without the xxxhdpi, xxhdpi, etc)
            new_name=(filename).replace(extensions[x],".png",1)

            # if the destination file exists, it will be deleted
            if os.path.exists(main_folder+'/'+dst+filename):                
                os.remove(dst+filename)
            if os.path.exists(main_folder+'/'+dst+new_name):                
                os.remove(dst+new_name)
                print ('removed '+dst+new_name)
            print(main_folder+'/'+dst+new_name)
            
            #move the new file to the destination folder
            move(filename,dst,copy_function=copy2)
            print ('moving '+dst+new_name)
            
            #leave the file with the appropriate name (without the xxxhdpi, xxhdpi, etc)                           
            os.rename(dst+filename, dst+ new_name)

            #we exit to continue with the next file
            break
                
      
      
