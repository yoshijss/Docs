# -*- coding: sjis -*-
# 

Hankei = 10

def main():

	while(1):

		RRR = float(input('R=').strip())

		if (0 == RRR):
			break

		XXX = float(input('X=').strip())
		YYY = float(input('Y=').strip())

		if (((XXX * -1) ** 2 + (YYY * -1) ** 2)  < (RRR ** 2)):
			print('In!\n')
		else:
			print('Out!\n')



if __name__ == "__main__":
    main()
