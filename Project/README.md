## YACS (Yet another cluster scheduler)

* A cluster scheduler co-ordinates tasks sent to a cluster, which contains a master node and worker nodes. 
* The master node receives tasks and schedules them onto workers, which then complete the task and notify the master
* Each worker contains slots which complete tasks assigned to them
* Various scheduling algorithms such as **random assignment**, **least loaded** and **round robin** are used by the scheduler to assign tasks to worker nodes.

### Instructions to run

1. Clone the repository by using either
```bash
git clone https://github.com/RishithBhowmick/Big-Data.git
# or
git clone git@github.com:RishithBhowmick/Big-Data.git
``` 


2. Get into the directory and configure **config.json** as per your requirements

3. Run 3 workers in different terminal windows in the following format:
```bash
python3 worker.py <PORT> <WORKER_ID> <SLOTS>
```

4. Run the master in a terminal window using the following format: 
```bash
# the scheduling algorithm can be either of the 3: RANDOM,RR or LL
python3 master.py config.json <SCHEDULING ALGO>
```

5. Run either of the requests generator using the following syntax:
```bash
python3 requests.py <number of requests>
#or 
python3 request_eval.py <number of requests>
```

