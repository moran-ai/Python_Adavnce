import subprocess


# 1.简单的写法
# 开启一个子进程，用来执行系统命令 args,encoding,shell三个参数
# run_cmd = subprocess.run('dir E:\\virenv\\python全栈\\Python网络编程和并发', encoding='utf-8', shell=True)


# print(run_cmd)

# 2.定义一个方法，调用系统所有命令
def runCmd(command):
    # 定义一个子进程，用来执行系统所有命令
    runMd = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='GBK', shell=True)
    # 判断执行是否正常  returncode为0代表正常
    if runMd.returncode == 0:
        print('success:')
        print(runMd.stdout)
    else:
        print('命令执行错误:')
        print(runMd.stderr)


runCmd('dir E:\\virenv\\python全栈\\Python网络编程和并发')
runCmd('exit 1')
