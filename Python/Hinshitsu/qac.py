# -*- coding: sjis -*-
# 
import sys
import qacwarn

def main():

    # �R�}���h���C����in��out�t�@�C�����w�肳��Ă��Ȃ��Ƃ���
    argv = sys.argv
    argc = len(argv)
    if (argc != 3):
        print('usage: pyton %s redmineprojectname' % argv[0])
        quit()

    # �v���W�F�N�g��
    inFile = argv[1]
    outFile = argv[2]

    retVal = qacwarn.qacWarnCount(inFile, outFile)

#    if 0 == retVal:


if __name__ == "__main__":
    main()
