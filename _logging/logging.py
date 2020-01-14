import os
from datetime import datetime
__author__ = 'lorem.cookie'
class FileOnlyModule(Exception):
    def __init__(self):
        Exception.__init__(self,'FILE IS ONLY A MODULE')
class ErrorOpeningLogfile(Exception):
    def __init__(self):
        Exception.__init__(self,'ERROR OPENING LOG FILE')
class ErrorOpeningLogdir(Exception):
    def __init__(self):
        Exception.__init__(self,'ERROR OPENING LOG DIR')
class LogLevelError(Exception):
    def __init__(self):
        Exception.__init__(self,'LogLevel VAR MUST BE : WARNING, ERROR, INFO, DEBUG')
class NoLogLevel(Exception):
    def __init__(self):
        Exception.__init__(self,'LogLevel MUST BE SPECIFIED WHEN LOG FUNCTION IS CALLED')
class logging:
    def __init__(self, LogLevel='None', LogFile='LogFile.log', LogDir='Log', Debug=False):
        self.time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.LogFile = LogFile
        self.LogDir = LogDir
        self.Debug = Debug
        self.LogLevel = LogLevel
        LogDir = os.path.join(os.getcwd(), self.LogDir)
        self.LogDir = LogDir
        LogFile = os.path.join(self.LogDir, self.LogFile)
        self.LogFile = LogFile
        if self.Debug:
            print('[!]CHECK IF ({}) EXIST'.format(self.LogDir))
        if os.path.isdir(self.LogDir):
            if self.Debug:
                print('[+]({})DOES EXIST'.format(self.LogDir))
        else:
            if self.Debug:
                print('[-]({})DOES NOT EXIST'.format(self.LogDir))
                print('[+]({})CREATING DIR'.format(self.LogDir))
            try:
                os.mkdir(self.LogDir)
            except FileExistsError:
                if self.Debug:
                    print('[-]ERROR CREATING LOG DIR')
                    print('[-]EXITING PROGRAM...')
                raise ErrorOpeningLogdir
        if self.Debug:
            print('[!]CHECK IF ({}) EXIST'.format(self.LogFile))
        if os.path.isfile(self.LogFile):
            if self.Debug:
                print('[+]({})DOES EXIST'.format(self.LogFile))
        else:
            if self.Debug:
                print('[-]({})DOES NOT EXIST'.format(self.LogFile))
                print('[+]({})CREATING FILE'.format(self.LogFile))
            try:
                open(self.LogFile, 'a').close()
            except (IOError, OSError):
                if self.Debug:
                    print('[-]ERROR CREATING LOG FILE')
                    print('[-]EXITING PROGRAM...')
                raise ErrorOpeningLogfile
    def LOG(self, inputstr):
        if(self.LogLevel == 'WARNING'):
            self.LogLevel = 'WARNING'
        elif(self.LogLevel == 'ERROR'):
            self.LogLevel = 'ERROR'
        elif(self.LogLevel == 'DEBUG'):
            self.LogLevel = 'DEBUG'
        elif(self.LogLevel == 'None'):
            raise NoLogLevel
        else:
            raise LogLevelError
        if self.Debug:
            print('\n[{}]{}'.format(self.LogLevel, inputstr))
        try:
            with open(self.LogFile, 'a') as f:
                f.write('\n[{}]({}){}\n'.format(str(self.LogLevel), str(self.time_now), str(inputstr)))
        except (IOError, OSError):
            raise ErrorOpeningLogfile
    def INFO(self, inputstr):
        if self.Debug:
            print('\n[INFO]{}'.format(inputstr))
        try:
            with open(self.LogFile, 'a') as f:
                f.write('\n[INFO]({}){}'.format(str(self.time_now), str(inputstr)))
        except (IOError, OSError):
            raise ErrorOpeningLogfile
    def WARNING(self, inputstr):
        if self.Debug:
            print('\n[WARNING]{}'.format(inputstr))
        try:
            with open(self.LogFile, 'a') as f:
                f.write('\n[WARNING]({}){}'.format(str(self.time_now), str(inputstr)))
        except (IOError, OSError):
            raise ErrorOpeningLogfile
    def ERROR(self, inputstr):
        if self.Debug:
            print('\n[ERROR]{}'.format(inputstr))
        try:
            with open(self.LogFile, 'a') as f:
                f.write('\n[ERROR]({}){}'.format(str(self.time_now), str(inputstr)))
        except (IOError, OSError):
            raise ErrorOpeningLogfile
    def DEBUG(self, inputstr):
        if self.Debug:
            print('\n[DEBUG]{}'.format(inputstr))
        try:
            with open(self.LogFile, 'a') as f:
                f.write('\n[DEBUG]({}){}'.format(str(self.time_now), str(inputstr)))
        except (IOError, OSError):
            raise ErrorOpeningLogfile
if __name__ == '__main__':
    raise FileOnlyModule