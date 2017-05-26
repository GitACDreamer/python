'多进程'

import subprocess
from multiprocessing import Process
from multiprocessing import Pool

import os
import time
import random


def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


def testCreateProcess():
    print('Process (%s) start……' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start...')
    p.start()
    p.join()
    print('Child process end.')


def long_time_task(name):
    print('Run task %s (%s)……' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f seconds' % (name, (end - start)))


def testProcessPool():
    print('Parent process %s: ' % os.getpid())
    p = Pool(4)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done……')
    p.close()
    p.join()
    print('All subprocesses done.')


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


def testProcesses():
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()


def testSubprocess():
    print('$ ping www.python.org')
    r = subprocess.call(['ping', 'www.python.org'])
    print('Exit code:', r)


def testSubprocessCommunicate():
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('GBK'))
    print('Exit code:', p.returncode)


def main():
    testCreateProcess()
    testProcesses()
    testSubprocess()
    testProcessPool()
    testSubprocessCommunicate()


if __name__ == '__main__':
    main()
