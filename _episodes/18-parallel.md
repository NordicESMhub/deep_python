---
title: Parallelize your code
teaching: 0
exercises: 0
questions:
- "What python package could I use to parallelize my Python code?"
- "What is Data parallelism?"
---

# Multiprocessing

- [Introduction to Parallel computing](https://hpc-carpentry.github.io/hpc-python/06-parallel/)

The HPC Carpentry course on [Analysis pipelines with Python](https://hpc-carpentry.github.io/hpc-python/).


```python
import psutil
# logical=True counts threads, but we are interested in cores
psutil.cpu_count(logical=False)
```




    32




```python
import time

def sleeping(arg):
    time.sleep(0.1)

%timeit list(map(sleeping, range(24)))
```

    2.4 s ± 76.8 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)



```python
from multiprocess import Pool
pool = Pool(8)
%timeit pool.map(lambda x: time.sleep(0.1), range(24))
pool.close()
```

    304 ms ± 75.2 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)


# References

- [https://pymotw.com/2/multiprocessing/basics.html](https://pymotw.com/2/multiprocessing/basics.html)

## Multiprocessing Basics
The simplest way to spawn a second is to instantiate a Process object with a target function and call start() to let it begin working.


```python
import multiprocess

def worker(num):
    """thread worker function"""
    print ('Worker:', num)
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocess.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
```

    Worker: 0
    Worker: 1
    Worker: 2
    Worker: 3
    Worker: 4


## Determining the Current Process
Passing arguments to identify or name the process is cumbersome, and unnecessary. Each Process instance has a name with a default value that can be changed as the process is created. Naming processes is useful for keeping track of them, especially in applications with multiple types of processes running simultaneously.


```python
import multiprocess
import time

def worker():
    name = multiprocess.current_process().name
    print (name, 'Starting')
    time.sleep(2)
    print (name, 'Exiting')

def my_service():
    name = multiprocess.current_process().name
    print (name, 'Starting')
    time.sleep(3)
    print (name, 'Exiting')

if __name__ == '__main__':
    service = multiprocess.Process(name='my_service', target=my_service)
    worker_1 = multiprocess.Process(name='worker 1', target=worker)
    worker_2 = multiprocess.Process(target=worker) # use default name

    worker_1.start()
    worker_2.start()
    service.start()
```

    worker 1 Starting
    Process-11 Starting
    my_service Starting
    worker 1 Exiting
    Process-11 Exiting
    my_service Exiting


## Daemon Processes
By default the main program will not exit until all of the children have exited. There are times when starting a background process that runs without blocking the main program from exiting is useful, such as in services where there may not be an easy way to interrupt the worker, or where letting it die in the middle of its work does not lose or corrupt data (for example, a task that generates “heart beats” for a service monitoring tool).

To mark a process as a daemon, set its daemon attribute with a boolean value. The default is for processes to not be daemons, so passing True turns the daemon mode on.

The output does not include the “Exiting” message from the daemon process, since all of the non-daemon processes (including the main program) exit before the daemon process wakes up from its 2 second sleep.

The daemon process is terminated automatically before the main program exits, to avoid leaving orphaned processes running. You can verify this by looking for the process id value printed when you run the program, and then checking for that process with a command like ps.


```python
import multiprocess
import time
import sys

def daemon():
    p = multiprocess.current_process()
    print ('Starting:', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print ('Exiting :', p.name, p.pid)
    sys.stdout.flush()

def non_daemon():
    p = multiprocess.current_process()
    print ('Starting:', p.name, p.pid)
    sys.stdout.flush()
    print ('Exiting :', p.name, p.pid)
    sys.stdout.flush()

if __name__ == '__main__':
    d = multiprocess.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocess.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()
```

    Starting: daemon 27853
    Starting: non-daemon 27856
    Exiting : non-daemon 27856
    Exiting : daemon 27853


## Waiting for Processes
To wait until a process has completed its work and exited, use the join() method.
Since the main process waits for the daemon to exit using join(), the “Exiting” message is printed this time.


```python
import multiprocess
import time
import sys

def daemon():
    print ('Starting:', multiprocess.current_process().name)
    time.sleep(2)
    print ('Exiting :', multiprocess.current_process().name)

def non_daemon():
    print ('Starting:', multiprocess.current_process().name)
    print ('Exiting :', multiprocess.current_process().name)

if __name__ == '__main__':
    d = multiprocess.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocess.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

    d.join()
    n.join()
```

    Starting: daemon
    Starting: non-daemon
    Exiting : non-daemon
    Exiting : daemon


## Timout argument
By default, join() blocks indefinitely. It is also possible to pass a timeout argument (a float representing the number of seconds to wait for the process to become inactive). If the process does not complete within the timeout period, join() returns anyway.


```python
import multiprocess
import time
import sys

def daemon():
    print ('Starting:', multiprocess.current_process().name)
    time.sleep(2)
    print ('Exiting :', multiprocess.current_process().name)

def non_daemon():
    print ('Starting:', multiprocess.current_process().name)
    print( 'Exiting :', multiprocess.current_process().name)

if __name__ == '__main__':
    d = multiprocess.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocess.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    n.start()

    d.join(1)
    print 'd.is_alive()', d.is_alive()
    n.join()
```


# Snakemake

- [Create workflow with snakemake](https://coderefinery.github.io/reproducible-research/03-workflow-management/)

## Introduction to snakemake

- [Snakemake from scratch](https://hpc-carpentry.github.io/hpc-python/11-snakemake-intro/)
- [Snakefiles](https://hpc-carpentry.github.io/hpc-python/12-snakefiles/)
- [Wildcards](https://hpc-carpentry.github.io/hpc-python/13-wildcards/)
- [Pattern rules](https://hpc-carpentry.github.io/hpc-python/14-patterns/)
- [Snakefiles are python codes](https://hpc-carpentry.github.io/hpc-python/15-snakemake-python/)
- [Resources and parallelism](https://hpc-carpentry.github.io/hpc-python/16-resources/)
- [Scaling a pipeline across a cluster](https://hpc-carpentry.github.io/hpc-python/17-cluster/)
- [Final notes](https://hpc-carpentry.github.io/hpc-python/18-final-notes/)

# Data parallelism

- [Handling large data files](https://annefou.github.io/metos_python/07-LargeFiles/)
- [Dask array](http://matthewrocklin.com/dask-website/)

{% include links.md %}
