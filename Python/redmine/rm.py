# -*- coding: sjis -*-
# 
import sys
import EVRedmineLib

def main():

    # コマンドラインでプロジェクトが指定されていないとだめ
    argv = sys.argv
    argc = len(argv)
    if (argc != 2):
        print('usage: pyton %s redmineprojectname' % argv[0])
        quit()

    # プロジェクト名
    redmine_prj = argv[1]

    if (False == RedmineStat.GetProjectInformation(redmine_prj)):
        print('Bad Project name!' % argv[0])
        quit()



if __name__ == "__main__":
    main()
