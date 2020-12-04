from socket import *
import json
import threading
import sys
import random
from datetime import datetime
import time
from queue import Queue
import os

workerIP = '127.0.0.1'
updatesPort = 5001
requestPort = 5000
HeartbeatPort = 5029
# slots = []
curr_worker_index = 0


def listen_to_heartbeat(worker_slots, task_pool, lock):

    masterSocket = socket(AF_INET, SOCK_STREAM)
    masterSocket.bind((workerIP, HeartbeatPort))
    masterSocket.listen(1)
    print("listening for heartbeats...")
    while 1:
        workerHeartBeat, _ = masterSocket.accept()

        workerUpdate = workerHeartBeat.recv(2048)
        worker_data = json.loads(workerUpdate.decode())

        worker_id = worker_data['worker_id']
        slots_available = worker_data['num_slots']
        
        if slots_available != worker_slots[int(worker_id)]['slots']:
            lock.acquire()
            worker_slots[int(worker_id)]['slots'] = slots_available
            lock.release()

        workerHeartBeat.close()


def listen_to_updates(task_execution_pool, worker_slots, algo, task_queue, jobs, lock):
    masterSocket = socket(AF_INET, SOCK_STREAM)
    masterSocket.bind((workerIP, updatesPort))
    masterSocket.listen(1)
    print("listening for updates...")
    while 1:
        # parsing incoming message
        workerHeartBeat, _ = masterSocket.accept()
        workerUpdate = workerHeartBeat.recv(2048)
        taskCompleted = json.loads(workerUpdate.decode())

        # decoding json
        job_id = taskCompleted['task_id'].split("_")[0]
        task_type = taskCompleted['task_id'].split("_")[1][0]
        worker = taskCompleted['worker_id']

        timing = datetime.now().time()
        lock.acquire()
        for i in range(len(task_execution_pool)):
            if job_id in task_execution_pool[i].keys():
                if task_type == "M":
                    
                    task_execution_pool[i][job_id]['num_map'] -= 1
                    worker_slots[int(worker)]['slots'] += 1
                    print(f"increasing worker : {worker}")
                    show_slots(task_execution_pool,worker_slots,algo,lock)
                    # lock.release()
                if task_type == "R":
                    # lock.acquire()
                    task_execution_pool[i][job_id]['num_reduce'] -= 1
                    worker_slots[int(worker)]['slots'] += 1
                    # lock.release()
                # if all mappers have completed execution
                # if task_execution_pool[i][job_id]['num_map'] == 0 and task_execution_pool[i][job_id]['num_reduce'] != 0:
                #     if jobs[job_id]['reduce_tasks']:
                #         lock.acquire()
                #         for task in jobs[job_id]['reduce_tasks']:
                #             task_queue.put(task)
                #         lock.release()
                if task_execution_pool[i][job_id]['num_map'] == 0 and task_execution_pool[i][job_id]['num_reduce'] == 0:
                    # job completion
                    timing = datetime.now().time()
                    info = 'Completed Job '+job_id+' at '+str(timing)+" "+algo
                    with open('Master-log '+algo+'.txt', 'a') as f:
                        f.write("\n")
                        f.writelines(info)
        lock.release()

        info = 'Received task '+taskCompleted['task_id']+' at '+str(timing)
        with open('Master-log '+algo+'.txt', 'a') as f:
            f.write("\n")
            f.writelines(info)
        workerHeartBeat.close()


def determine_worker(worker_info, algo, lock):
    global curr_worker_index
    lock.acquire()
    all_workers = [i for i in worker_info.keys()]
    slots = [worker_info[i]['slots'] for i in worker_info]
    # for i in worker_info:
    #     slots.append(worker_info[i]['slots'])
    if algo == "RANDOM":

        worker_id = all_workers[random.randrange(0, len(all_workers))]

        if worker_info[worker_id]['slots'] > 0:
            lock.release()
            return worker_id
        else:
            lock.release()
            time.sleep(1)
            return determine_worker(worker_info, algo, lock)

    if algo == "RR":
        worker_id = all_workers[curr_worker_index]
        if worker_info[worker_id]['slots'] > 0:
            curr_worker_index = (curr_worker_index+1) % len(all_workers)
            lock.release()
            return worker_id
        else:
            l = curr_worker_index
            curr_worker_index = (curr_worker_index+1) % len(all_workers)
            while curr_worker_index != l:
                curr_worker_index = (curr_worker_index+1) % len(all_workers)
                worker_id = all_workers[curr_worker_index]
                if worker_info[worker_id]['slots'] > 0:
                    lock.release()
                    return worker_id
            lock.release()
            time.sleep(1)
            return determine_worker(worker_info, algo, lock)

    if algo == "LL":
        # need to test
        worker_id = all_workers[slots.index(max(slots))]

        if worker_info[worker_id]['slots'] > 0:
            lock.release()
            return worker_id
        else:
            lock.release()
            time.sleep(1)
            return determine_worker(worker_info, algo, lock)


def send_task(worker_slots, algo, task_execution_pool, task_queue, lock):

    while 1:
        lock.acquire()

        if not task_queue.empty():

            # print('sending task')
            task = task_queue.get()
            lock.release()
            workerId = determine_worker(worker_slots, algo, lock)

            lock.acquire()
            print(f'reducing worker {workerId}')
            worker_slots[workerId]['slots'] -= 1
            show_slots(task_execution_pool,worker_slots,algo,lock)
            lock.release()
            # print("task popped from queue", task)

            worker = worker_slots[workerId]

            timing = datetime.now().time()
            info = 'sending task ' + \
                str(task['task_id'])+' to '+str(workerId) + \
                ' at ' + str(timing)+' algo '+algo
            # print(info)
            with open('Master-log '+algo+'.txt', 'a') as f:
                f.write("\n")
                f.writelines(info)
            # print(f'sending to {worker}')
            workerSocket = socket(AF_INET, SOCK_STREAM)
            
            workerSocket.connect((workerIP, worker['port']))
            workerSocket.send(json.dumps(task).encode())
        else:
            lock.release()
            time.sleep(1)


def receive_task(worker_slots, algo, task_execution_pool, task_queue, jobs, lock):
    masterSocket = socket(AF_INET, SOCK_STREAM)
    masterSocket.bind((workerIP, requestPort))
    masterSocket.listen(1)
    print("listening for Tasks...")
    while 1:

        masterConnection, _ = masterSocket.accept()
        taskJson = masterConnection.recv(1024)
        masterConnection.close()
        job = json.loads(taskJson.decode())

        if job['map_tasks'] != []:
            timing = datetime.now().time()
            info = 'Received Job '+job['job_id']+' at '+str(timing)+" "+algo
            print(info)
            with open('Master-log '+algo+'.txt', 'a') as f:
                f.write("\n")
                f.writelines(info)

            # add job to job execution pool and then add the reduce tasks to jobs (a dictionary)
            lock.acquire()
            job_info = {job['job_id']: {'num_map': len(
                job['map_tasks']), 'num_reduce': len(job['reduce_tasks'])}}

            # to keep track of number of tasks pending/completed
            task_execution_pool.append(job_info)

            # needed for adding reduce tasks to the pool
            jobs[job['job_id']] = job['reduce_tasks']

            # adding tasks to queue
            for task in job['map_tasks']:
                task_queue.put(task)
            for task in job['reduce_tasks']:
                task_queue.put(task)
            lock.release()
            # time.sleep(1)


def show_slots(task_execution_pool, worker_slots, algo, lock):
    # while 1:
        # lock.acquire()
        # print(worker_slots)
        print("-----------------------")
        # print("Worker"worker_slots)
        for i in worker_slots:
            print("Worker: ", i, "Slots: ", worker_slots[i]['slots'])
            # print(i)
        print("-----------------------")
        # lock.release()
        # time.sleep(1)


def main():

    if len(sys.argv) != 3:
        print('usage file_name.py config.json scheduling_algo')
        exit()

    # variable declaration
    config = sys.argv[1]
    f = open(config, "r")
    worker_info = json.load(f)

    algo = sys.argv[2]
    workers = worker_info['workers']
    worker_slots = {i['worker_id']: {
        'slots': i['slots'], 'port': i['port']} for i in workers}

    lock = threading.Lock()
    task_execution_pool = list()
    jobs = dict()
    task_queue = Queue()
    t1 = threading.Thread(target=receive_task, args=(
        worker_slots, algo, task_execution_pool, task_queue, jobs, lock))
    t2 = threading.Thread(target=listen_to_heartbeat,
                          args=(worker_slots, task_execution_pool, lock))
    t3 = threading.Thread(target=listen_to_updates,
                          args=(task_execution_pool, worker_slots, algo, task_queue, jobs, lock))
    t4 = threading.Thread(target=send_task,
                          args=(worker_slots, algo, task_execution_pool, task_queue, lock))
    t4 = threading.Thread(target=send_task,
                          args=(worker_slots, algo, task_execution_pool, task_queue, lock))
    # t5 = threading.Thread(target=show_slots,
    #                       args=(task_execution_pool, worker_slots, algo, lock))
    os.system("rm worker-log*")
    os.system("rm Master-log*")
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    # t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    # t5.join()


main()
