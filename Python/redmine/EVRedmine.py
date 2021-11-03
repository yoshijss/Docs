# -*- coding: sjis -*-
# 

from redminelib import Redmine
from redminelib.exceptions import ResourceNotFoundError

# Redmin????
REDMINE_SERVER = 'http://t110ii:3000'
REDMINE_USER = 'username=\'yoshiito\''
REDMINE_PASS = 'password=\'ninomiya\''

REDMINE_PROJECT = 'sepg'


def GetProjectInformation(projname):

    redmine = Redmine(REDMINE_SERVER, username='yoshiito', password='ninomiya')
    status = redmine.issue_status.all()

    proj = redmine.project.get(projname)

    issues = redmine.issue.filter(project_id = proj.identifier)

    if len(issues) > 0:
        print("##", str(len(issues)))
        for issue in issues:
                print('(%s) - %d:%s' % (GetStatusText(issue.status), issue.id, issue.subject))

def GetStatusText(status):

    numStatus = int(status)

    if 1 == numStatus:
        txtStatus = '解析'
    elif 8 == numStatus:
        txtStatus = '対策'
    elif 9 == numStatus:
        txtStatus = '検証'
    elif 12 == numStatus:
        txtStatus = '承認'
    elif 13 == numStatus:
        txtStatus = '確認'
    elif 14 == numStatus:
        txtStatus = '新規'
    elif 15 == numStatus:
        txtStatus = '対応中'
    elif 16 == numStatus:
        txtStatus = '承認待ち'
    elif 22 == numStatus:
        txtStatus = '影響分析'
    elif 25 == numStatus:
        txtStatus = '変更実施'
    else:
        txtStatus = '不明'

    return txtStatus