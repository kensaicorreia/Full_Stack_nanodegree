'''this script is use to rename file that have number in front of the file name 
and are seprated with space and have and index number at the back fo the file name '''

import os

# change directory 
os.chdir("C:/Users/linux/Documents/New folder")
#print(os.getcwd())
for f_name in os.listdir():
    #print(f_name) # test
    file_name, file_ext = os.path.splitext(f_name)
    #print(file_name) # test 
    # split file name and separate  extension 
    title_front, file_title, title_back = file_name.split(' ')
    # split the file name if separate by space
    #print(title_back) # test
    
    title_front = title_front.strip('0123456789')
    # strip any number from the front of the name 
    title_back = title_back.strip()[:].zfill(3)
    # strip any space from the back and zero fill any number to 2 place holder

    new_name = '{}-{}{}'.format(file_title,title_back, file_ext)
    os.rename(f_name, new_name)
    print(new_name)

        

