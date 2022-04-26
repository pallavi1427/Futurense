import time
import pyautogui
from tkinter import filedialog
from datetime import datetime
import os

n = 16
m = n+1
for i in range(n//2-1):
    for j in range(m):
        if i == n//2-2 and (j == 0 or j == m-1):
            print("*", end=" ")
        
        elif j <= m//2 and ((i+j == n//2-3 and j <= m//4)  or (j-i == m//2-n//2+3 and j > m//4)):
           print("*", end=" ")
        elif j > m//2 and ((i+j == n//2-3+m//2 and j < 3*m//4) or (j-i == m//2-n//2+3+m//2 and j >= 3*m//4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


for i in range(n//2-1, n):
    for j in range(m):
        if (i-j == n//2-1) or (i+j == n-1+m//2):
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print()
time.sleep(5)
s2=pyautogui.screenshot()
#s2.save("star2.jpg")
folder=filedialog.askdirectory()
#File=os.path.join(Folder, "star3.jpg")
#Screen.save(File)

count_time=datetime.now().replace(microsecond=0)
print(type(count_time))
Format="%y_%b_%d_%H_%M_%S"
new_time=datetime.strftime(count_time,Format)
filename="star3"+new_time+".png"
file=os.path.join(folder,filename)
s2.save(file)

