import os
import subprocess
import shutil


c = 'ipconfig'
s = subprocess.getoutput(c)
with open('ipaddress.txt', 'w')as w:
    w.write(s)

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        d = os.path.join(root, file)
        if d.endswith('.ini') or d.endswith('.log.tmp') or d.endswith('.log') or d.endswith('.DAT') or d.endswith('.sys'):
            continue
        else:
            scr = 'C:\\Users\\admin\\Desktop' # you can use any path to save file
            shutil.move('ipaddress.txt', scr)
           

# IT'S THE EASIEST METHOD TO HACK THE IP OF VICTIM SYSTEM . HERE I HAVE GIVEN JUST BASIC AND FOR ADVANCE U CAN USE SOCKET OR OTHER MODULE TO PERFORM FUTHUR ACTIVITY 
# IT'S JUST FOR EDUCATIONAL PURPOSE
