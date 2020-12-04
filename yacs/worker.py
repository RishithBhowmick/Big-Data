from socket import *
import sys
import time
import json
import threading
from datetime import datetime


masterIP = '127.0.0.1'
masterPort = 0
updatesPort = 5001
HeartbeatPort = 5029

def execute_task(num_slots,execution_pool,worker,lock):
    
    while 1:
        time.sleep(1)
        if execution_pool != []:
            lock.acquire()
            for task in execution_pool:
                task['duration'] -= 1
                if task['duration'] == 0:
                    send_update(task,worker)
                    execution_pool.remove(task)
                    print("Number of tasks present",len(execution_pool))
                    num_slots += 1
            lock.release()


def send_heart_beat(num_slots,execution_pool,worker,lock):
    print("Initialising heartbeats")

    while 1:
        
        
        masterSocket = socket(AF_INET, SOCK_STREAM)
        try:
            masterSocket.connect((masterIP, HeartbeatPort))
            print("Sending HeartBeat...",datetime.now())
            lock.acquire()
            update = {"worker_id":worker,"num_slots":num_slots}
            lock.release()
            masterSocket.send(json.dumps(update).encode())
            # receive 'happening' from worker
            workerAck = masterSocket.recv(1024)
            # print('Server HeartBeat acknowledgement received  ', workerAck.decode())
            
            masterSocket.close()
        except ConnectionRefusedError:
            print("Connection refused,trying again in 1s...")
        except TimeoutError:
            print('Timeout, retrying in 1s... ')
       
        time.sleep(0.5)         
        


def send_update(task,worker):
    
    print(task)
    update = {"worker_id":worker,"task_id":task['task_id']}
    print(f"Task {task['task_id']} Completed, Sending update")
    try:
        masterSocket = socket(AF_INET, SOCK_STREAM)
        masterSocket.connect((masterIP, updatesPort))
        masterSocket.send(json.dumps(update).encode())
        timing = datetime.now()
        info = "Task "+task['task_id']+" Completed at " + str(timing)
        with open('worker-log '+worker+'.txt', 'a') as f:
            f.write("\n")
            f.writelines(info)
    except TimeoutError:
        print("server busy, sleeping and trying again...")
        time.sleep(1)
        send_update(task,worker)
    except ConnectionError:
        time.sleep(1)
        send_update(task,worker)
    # except Exception as e:
        
    


def receive_task(num_slots,execution_pool,worker,lock):
    global masterPort
    # global num_slots, execution_pool
    masterSocket = socket(AF_INET, SOCK_STREAM)
    masterSocket.bind((masterIP, masterPort))
    masterSocket.listen(1)

    print("Listening for events...")
    while 1:

        # receive connection from requests
        masterConnection, _ = masterSocket.accept()
        task = masterConnection.recv(1024)
        
        task_to_do = json.loads(task.decode())
        timing = datetime.now()
        info = "Received Task " +str(task_to_do['task_id'])+" at "+str(timing)+" Running..."
        print(info)
        with open('worker-log '+worker+'.txt', 'a') as f:
            f.write("\n")
            f.writelines(info)
        lock.acquire()
        execution_pool.append(task_to_do)
        num_slots-=1
        lock.release()
        print("Number of tasks present",len(execution_pool))
        masterConnection.close()

        # send_update(task_to_do)

        # b = capitalizedSentence.encode('utf-8')
        # masterConnection.send(b)

        # create thread before heartbeat(first time when master sends duration) and send to function
        # else:


def main():
    if len(sys.argv) != 4:
        print('usage file_name.py port worker_id num_slots')
        exit()
    # num_slots,execution_pool
    global masterPort
    execution_pool = list()  # list of dictionary items
    lock = threading.Lock()
    num_slots = int(sys.argv[3])
    worker = sys.argv[2]
    masterPort = int(sys.argv[1])
    t1 = threading.Thread(target=receive_task,args=(num_slots,execution_pool,worker,lock))
    t2 = threading.Thread(target=send_heart_beat,args=(num_slots,execution_pool,worker,lock))
    t3 = threading.Thread(target=execute_task,args=(num_slots,execution_pool,worker,lock))
    

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()


main()
