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
        txtStatus = '���'
    elif 8 == numStatus:
        txtStatus = '�΍�'
    elif 9 == numStatus:
        txtStatus = '����'
    elif 12 == numStatus:
        txtStatus = '���F'
    elif 13 == numStatus:
        txtStatus = '�m�F'
    elif 14 == numStatus:
        txtStatus = '�V�K'
    elif 15 == numStatus:
        txtStatus = '�Ή���'
    elif 16 == numStatus:
        txtStatus = '���F�҂�'
    elif 22 == numStatus:
        txtStatus = '�e������'
    elif 25 == numStatus:
        txtStatus = '�ύX���{'
    else:
        txtStatus = '�s��'

    return txtStatus