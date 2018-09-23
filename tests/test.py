# 进程池
# 适用情况
# 1.
# 多个进程执行任务
# 2.
# 任务非常多，且执行时间短，需要频繁创建删除进程的时候
# 步骤
# 1.
# 使用multiprocessing.Pool创建进程池，得到进程池对象
# pools = Pool(processes=4)
# 2.
# 使用apply_async将事件放入进程池，等待执行
# pools.apply_async(worker, (i,))  # 异步
# 3.
# 如果池内有空闲进程，则会执行等待的事件
# 4.
# 使用close()
# 关闭进程池，不能够在投放进程
# 5.
# 使用join()
# 阻塞等待进程池内现有所有事件都被执行结束后，回收子进程（进程池内所有进程均为子进程）
# a)  如果没有join()，则主进程会直接退出
# b)  join()
# 必须在close()
# 或者terminate()
# 之后
# 进程池对象的方法
# 1.
# pools.apply_async(fun, [args = (), [kwargs = {}]])：异步加载事件到进程池
# 2.
# pools.apply(fun, [args = (), [kwargs = {}]])：同步加载事件到进程池【一般不用，有序执行，效率很低】
# 3.
# pools.close()：在进程池全部执行之后，关闭进程池
# 4.
# pools.join()：阻塞，等待进程池的子进程退出，必须在close()
# 后
# 5.
# pools.map(fun, iterable)：功能上与内建函数map类似。将第二个参数中的每一个数作为参数，带入到第一个函数中，然后将该事件放入进程池中【兼顾了apply_async的功能】
# 示例：
import multiprocessing as mp
from time import sleep
import os
import datetime
import random

def worker(msg):
    # print(os.getpid())
    a = []
    for i in range(100000):
        a.append(i)
    a.clear()
    if '1' in msg:
        sleep(10)
    print(msg)
    return msg


if __name__ == '__main__':
    # 创建一个包含４个进程的进程池，得到进程池对象
    print(datetime.datetime.utcnow())

    """
    2018-09-21 04:00:03.368197
    进程池关闭前
    进程池关闭后，回收之前
    回收之后
    2018-09-21 04:00:09.328215
    """
    pools = mp.Pool(processes=4)
    result = []
    for i in range(10):
        msg = 'hello %d' % i
        # 向进程池中加载事件　
        result.append(pools.apply_async(worker, (msg,)))

    # 关闭进程池
    print('进程池关闭前')
    pools.close()
    print('进程池关闭后，回收之前')
    # 进程池回收
    pools.join()
    print('回收之后')

    print('=================', len(result))
    # for i in result:
    #     print(i.get())


    """
    2018-09-21 03:58:32.223550
    2018-09-21 03:59:11.165509
    """
    # for _ in range(100):
    #     a = []
    #     for i in range(1000000):
    #         a.append(i)
    #     a.clear()

    print(datetime.datetime.utcnow())
