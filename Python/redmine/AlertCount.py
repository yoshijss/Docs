# -*- coding: sjis -*-
# 

from redminelib import Redmine
from redminelib.exceptions import ResourceNotFoundError

import RedmineStat

# Redmine用定数
REDMINE_SERVER = 'http://t110ii:3000'
REDMINE_USER = 'automate'
REDMINE_PASS = 'Hiragana46'

REDMINE_PROJECT_LIST = ['MSE744', 'MSE760']

def main():

    # プロジェクト名
    for redmine_prj in REDMINE_PROJECT_LIST

        reslist = []

        if False != ExpiredIssues(REDMINE_SERVER, REDMINE_USER, REDMINE_PASS, redmine_prj, reslist):
            for printres in reslist
                print ()
        NoLimitIssues(REDMINE_SERVER, REDMINE_USER, REDMINE_PASS, redmine_prj, reslist)


if __name__ == "__main__":
    main()
