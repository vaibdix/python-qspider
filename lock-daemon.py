from threading import *


l=Lock()
def Test(name):
    l.acquire()
    for i in range(5):
        print("Lock Running")
        print(name)
    l.release()
t=Thread(target=Test, args=("ravi",))
t1=Thread(target=Test, args=("virat",))
t.start()
t1.start()