# Module for accessing system info.
import sys
import os

class SysInterface:
    def __init__(self):
        self.ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/..'
        self.homedir = os.path.expanduser('~')
        self.dirpath = os.getcwd()
        self.cmdargument = None
        self.cmdflag = None
        try:
            self.cmdargument = sys.argv[1]
            self.cmdflag = sys.argv[2]
        except IndexError:
            pass

    def createpath(self, path_list):
        try:
            os.makedirs('/'.join(path_list))
        except:
            print('Could not create directories of the following path:\n' + '/'.join(path_list))