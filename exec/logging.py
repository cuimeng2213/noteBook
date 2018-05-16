#!/usr/bin/env python

"""
@author cuimeng
"""
import time

class MyLog(object):
    '''
    @level: 日志级别默认为3,只有出错日志写入到日志文件 【1：info 2：debug 3：error】
    #writeToFile: 是否要写入到日志文件,默认为True写入到文件
    '''
    LEVEL = {'INFO':1,'DEBUG':2,"ERROR":3}
    def __init__(self,localFile,level = 3,writeToFile=True):
        self.level = level
        self.writeToFile = writeToFile
        try:
            self.logFile=open(localFile,'a+')
        except:
            self.logFile=open(localFile,'a+')

    def printf(self,*message):
        '''
        @message 可变长参数 第一个参数是日志标记： INFO DEBUG ERROR
        '''
        if self.level <= self.LEVEL.get(message[0]):
            data=''
            for i in range(len(message)):
                if i == 0:
                    data += '[{0}] '.format(message[i])
                else:
                    data += '{0}'.format(message[i])
            if self.writeToFile:
                print('[{0}] -- {1}'.format(time.strftime("%H:%M:%S", time.localtime()),data),file=self.logFile)
            else:
                print('[{0}] -- {1}'.format(time.strftime("%H:%M:%S", time.localtime()),data))

    def setLevel(self, l):
        self.level = l
    def getLevel(self):
        return self.level


if __name__ == "__main__":
    fileName = time.strftime("%Y-%m-%d", time.localtime())
    log = MyLog(fileName)
    tag = 'ERROR'
    log.printf(tag,'This is test :%s %d %s' % (1,2,time.localtime()))
    log.printf(tag,'This is test :%s %d %s' % (1,2,time.localtime()))
    log.printf(tag,'This is test :%s %d %s' % (1,2,time.localtime()))
    log.printf(tag,'This is test :%s %d %s' % (1,2,time.localtime()))
    time.sleep(1)
    #tag = INFO 当前日志级别为 3 不能打印出日志信息
    tag = 'INFO'
    log.printf(tag,'A :%s %d %s' % (1,2,time.localtime()))
    log.printf(tag,'A :%s %d %s' % (1,2,time.localtime()))
    log.printf(tag,'A :%s %d %s' % (1,2,time.localtime()))
    log.printf(tag,'A :%s %d %s' % (1,2,time.localtime()))
    time.sleep(1)
    #设置日志级别为1 可以输出所有日志级别
    log.setLevel(1)
    log.printf(tag,'B :%s %d %s' % (1,2,time.localtime()))
    log.printf(tag,'B :%s %d %s' % (1,2,time.localtime()))
    log.printf(tag,'B :%s %d %s' % (1,2,time.localtime()))
    log.printf(tag,'B :%s %d %s' % (1,2,time.localtime()))
    log.printf('DEBUG','B :%s %d %s' % (1,2,time.localtime()))
    log.printf('ERROR','B :%s %d %s' % (1,2,time.localtime()))

 

