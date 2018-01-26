#!/usr/bin/env python3
'''
  * @time: Created on 17/01/2018 7:01 AM
  * @author: by Ysan

    paramiko 模块
    paramiko模块提供了ssh及sft进行远程登录服务器执行命令和上传下载文件的功能。

    RSA (非对称密钥验证)
    基于公钥密钥连接：
    1.

    ssh传文件
    ssh本身拥有scp的命令，可以传文件
    而scp则是基于ssh的sftp协议的

    mac安装VX ubuntu
    blog.csdn.net/shenhaifeiniao/article/details/69397000
'''

import paramiko


def normal_link():
    '''
    通过SSHClient
    用于连接远程服务器并执行基本命令
    :return:
    '''
    # 创建SSH
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    # 加上这句话不用担心选yes的问题，会自动选上（用ssh连接远程主机时，第一次连接时会提示是否继续进行远程连接，选择yes）
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    # 连接服务器
    ssh.connect(hostname='192.168.142.128', port=22, username='ysan', password='ysan')

    # 执行命令
    stdin, stdout, stderr = ssh.exec_command("df -hl")
    # 结果放到stdout中，如果有错误将放到stderr中
    print(stdout.read().decode())
    # 关闭连接
    ssh.close()


def transport_link():
    '''
    通过transport连接
    :return:
    '''
    transport = paramiko.Transport(('192.168.142.128', 22))
    transport.connect(username='ysan', password='ysan')

    ssh = paramiko.SSHClient()
    ssh._transport = transport
    stdin, stdout, sterr = ssh.exec_command("ls")
    print(stdout.read().decode())
    # 关闭连接
    ssh.close()


def sftp_client():
    '''
    通过sftp传送文件
    :return:
    '''
    transport = paramiko.Transport('192.168.142.128', 22)
    transport.connect(username='ysan', password='ysan')

    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put('aa.txt', '/tmp/from_windows_aa')
    sftp.close()


if __name__ == '__main__':
    sftp_client()
