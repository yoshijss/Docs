# coding: ShiftJIS

import os       # OSモジュール
import xlrd     # Excel読み込み
import ResultSheet

# 構?管琿表ファイル
cmFile = '\\\\t110ii\\share\\P\\MSE720\\01_開発計画\\TSD720SDP0_5.3_構成管理表.xlsx'

cmStartRow = 9              # 構成管理表開始列
cmDeliverableCol = 3        # 「成果物」列
cmLatestFileCol = 4         # 「最新版保管場所」列
cmIsConfCol = 6             # 「構成管理対象」列
cmMark = '○'                # 「構成管琿対象」マーク

def file_list(folder):

    print(folder)
    files = os.listdir(folder)

    for file in files:
        print(file)

def main():

    # 構成管理表を読む
    cmExcel =  xlrd.open_workbook(cmFile)
    cmSheet = cmExcel.sheet_by_index(0)
    print(cmSheet.name)

    for row in range(cmStartRow, cmSheet.nrows):

        # 構成管理対象か
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
