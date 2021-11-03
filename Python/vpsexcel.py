# vpsexcel

import pandas as pd

def main():

	# 引数からファイル名を得る
	cmdline = sys.argv
	if len(cmdline) <> 1:
		print "python vpsexcel ファイル名"
		exit()

	print(cmdline)

	# CSVファイルの読み込み
	data = pd.read_csv(cmdline + '.csv')
 
	# Excel形式で出力
	data.to_excel(cmdline + '.xlsx', encoding='sjis')

if __name__ == "__main__":
    main()
