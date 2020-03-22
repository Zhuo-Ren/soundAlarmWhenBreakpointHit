from multiprocessing import Process
import subprocess
import sys
import os


def func():
    path = os.path.join(__file__, '..', 'sound.py')

    # os.system("python ./test2.py")
    # os.system("gnome-terminal -e 'bash -c \"ls; exec bash\"'")
    # subprocess.call_in_new_window('python ./test2.py', shell=True)
    # subprocess.call(['gnome-terminal', '-x', 'python ./test2.py'])
    subprocess.call('python '+path, creationflags=subprocess.CREATE_NEW_CONSOLE)

p = Process(target=func)

def alarm():
    return 'this %d' % (1 if p.start() is None else 2)