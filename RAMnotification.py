import psutil
from plyer import notification
import pynput.keyboard as keyboard
from pynput.keyboard import Key, Listener , Controller
from time import sleep as sleep
import subprocess
import os
import threading, pynput, time

def shownoti():
    """
    show thông báo systray
    """
    ramUsed = dict(psutil.virtual_memory()._asdict())
    Cpu = psutil.cpu_percent()
    notification.notify(
    title='CPU: '+str(Cpu)+'%',
    message='RAM Used: '+str(ramUsed['percent']), 
    timeout= 5)

def keydel():
    # print('del start')
    def on_press(key):
        pass
    def on_release(key):
        if key== Key.delete:
            killall()
            listenerDEL.stop()
            # print('del stop')
    with Listener(on_press=on_press,on_release=on_release) as listenerDEL:
        listenerDEL.start()       ###bỏ dòng này vì nó start sẵn khi gọi with ###
        sleep(5)
        listenerDEL.stop()
        # print('del stop')    

def killall():
    """Kill process in list by call """
    commmand='Nox,NoxVMHandle,nox_adb,NoxVMSVC,python,cmd,hkmd,TeamViewer_Service,GoogleCrashHandler,IDMan'
    for x in commmand.split(','):
        subprocess.call(['taskkill','/f','/im',x +'.exe','/t'])

# presses                                     =   0
class thread_keyboard(threading.Thread):
    listener                                =   None
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name                           =   name
        self.listener                       =   pynput.keyboard.Listener(on_press = thread_keyboard.on_press)
    def on_press(key):
        # global presses
        # presses                             +=  1
        print(key)
keyboard                                    =   thread_keyboard("thread.listener.keyboard")
keyboard.listener.start()
while(True):
    time.sleep(0.1)

def keybo():
    print('HadStarted')
    def on_press(key):
        pass
    def on_release(key):
        if key== Key.home:
            shownoti()
            keydel()
            listener.wait()

    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()     #chờ phản hồi từ keyboard

if __name__ == '__main__':
    keybo()