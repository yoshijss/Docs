# coding: utf-8

import xlrd				# Excel読み込み
import configparser		# iniファイル制御

import os
import sys

# ファイル名
EXCELFILE = ".\\NCAT5メッセージ日英.xlsm"
JP_INIFILE = ".\\Language_ja.ini"
EN_INIFILE = ".\\Language_en.ini"

# 定数
#EXCEL_START_ROW = 3
#EXCEL_KEY_COL = 2
#EXCEL_JP_COL = 3
#EXCEL_EN_COL = 4

EXCEL_START_ROW = 1
EXCEL_KEY_COL = 1
EXCEL_JP_COL = 2
EXCEL_EN_COL = 3



def main():

	book =  xlrd.open_workbook(EXCELFILE)
	sheets = book.sheets()
	sheet = sheets[0]

	# JP
	iniJP = configparser.ConfigParser()
	iniJP.read(JP_INIFILE)

	# EN
	iniEN = configparser.ConfigParser()
	iniEN.read(EN_INIFILE)

	Sect = ""

	for row in range(EXCEL_START_ROW, sheet.nrows):

		strKey = sheet.cell_value(row, EXCEL_KEY_COL)
		strKey = str.strip(strKey)

		if 0 >= len(strKey):	# 空は読み飛ばし

			continue

		elif '[' == strKey[0]:		# セクション指定

			Sect = strKey[1: len(strKey)-1]

			if True != iniJP.has_section(Sect):
				iniJP.add_section(Sect)

			if True != iniEN.has_section(Sect):
				iniEN.add_section(Sect)

		else:
			strJP = str.strip(sheet.cell_value(row, EXCEL_JP_COL))
			strEN = str.strip(sheet.cell_value(row, EXCEL_EN_COL))

			iniJP.set(Sect, strKey, strJP.replace('%','\%'))
			iniEN.set(Sect, strKey, strEN.replace('%','\%'))

#			print("[{}] {}={}\n".format(Sect, strKey, strJP)) 

	try:
		with open(JP_INIFILE, mode = 'w') as fileJP:
			iniJP.write(fileJP)

	except Exception as e:
		print >> sys.stderr, 'Error: Could not write to config file: %s' % e

	try:
		with open(EN_INIFILE, mode = 'w') as fileEN:
			iniEN.write(fileEN)

	except Exception as e:
		print >> sys.stderr, 'Error: Could not write to config file: %s' % e


if __name__ == "__main__":
    main()
