# coding: ShiftJIS

import os       # OS���W���[��
import xlwt     # Excel�������݃��[�e�B���e�B

class ResultSheet:
    def __init__(self):
        self.filename = ''
        file = ""

    def __del__(self):
        if file != "":
            close(file)

    def SetFile(filename):
        file = open(filename)
        self.filename = ''
    
    def GetError():
        return "Can't write Result File."