# coding: ShiftJIS

import os       # OS���W���[��
import xlrd     # Excel�ǂݍ���
import ResultSheet

# �\?����\�t�@�C��
cmFile = '\\\\t110ii\\share\\P\\MSE720\\01_�J���v��\\TSD720SDP0_5.3_�\���Ǘ��\.xlsx'

cmStartRow = 9              # �\���Ǘ��\�J�n��
cmDeliverableCol = 3        # �u���ʕ��v��
cmLatestFileCol = 4         # �u�ŐV�ŕۊǏꏊ�v��
cmIsConfCol = 6             # �u�\���Ǘ��Ώہv��
cmMark = '��'                # �u�\������Ώہv�}�[�N

def file_list(folder):

    print(folder)
    files = os.listdir(folder)

    for file in files:
        print(file)

def main():

    # �\���Ǘ��\��ǂ�
    cmExcel =  xlrd.open_workbook(cmFile)
    cmSheet = cmExcel.sheet_by_index(0)
    print(cmSheet.name)

    for row in range(cmStartRow, cmSheet.nrows):

        # �\���Ǘ��Ώۂ�
        if cmMark != cmSheet.cell_value(row, cmIsConfCol):
            print(row)
            print(cmSheet.cell_value(row, cmIsConfCol))
            file_list(cmSheet.cell_value(row, cmLatestFileCol))
            continue
        else:
            print(cmSheet.cell_value(row, cmDeliverableCol))

#    cmExcel.

if __name__ == "__main__":
    main()
