import os
import time

'''
this will pop up three time to play a song
'''

total_breaks = 3
break_count = 0
while(break_count < total_breaks):
    wait = time.sleep(10)
    browser_for_file = os.startfile('C:\\Users\\linux\\Music\\take_a_break.mp3')
    break_count = break_count + 1




