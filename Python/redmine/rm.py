# -*- coding: sjis -*-
# 
import sys
import EVRedmineLib

def main():

    # �R�}���h���C���Ńv���W�F�N�g���w�肳��Ă��Ȃ��Ƃ���
    argv = sys.argv
    argc = len(argv)
    if (argc != 2):
        print('usage: pyton %s redmineprojectname' % argv[0])
        quit()

    # �v���W�F�N�g��
    redmine_prj = argv[1]

    if (False == RedmineStat.GetProjectInformation(redmine_prj)):
        print('Bad Project name!' % argv[0])
        quit()



if __name__ == "__main__":
    main()
