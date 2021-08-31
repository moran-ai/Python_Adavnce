线程：
    ① 内核线程：由操作系统内核创建和撤销
    ② 用户线程：不需要内核支持而在用户程序中实现的线程

线程的状态：
    ① 新建
    ② 就绪状态  由CPU调度进入运行状态
    ③ 运行状态  等待的条件 等待/阻塞    满足条件就进入就绪状态  运行结束进入终止状态
    ④ 终止

线程的创建：
    ① 通过函数封装的方式进行创建
    ② 通过类的方式创建

获取线程数量:
    len(threading.enumerate())
    threading.activeCount()

设置守护线程:
    主线程结束，子线程也结束
    thread_t.setDaemon(True)
    thread_t.daemon = True

threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：

- threading.currentThread(): 返回当前的线程变量。
- threading.enumerate(): 返回一个包含正在运行的线程的list。
    正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
- threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
- run(): 用以表示线程活动的方法。
- start():启动线程活动。
- join([time]):等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
- isAlive(): 返回线程是否活动的。
- getName: 返回线程名。
- setName:设置线程名。
- isDaemon:查看线程是否是后台运行标志
- setDaemon:设置线程的后台运行标志
