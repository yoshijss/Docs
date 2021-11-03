# -*- coding: sjis -*-
# 

import os           # OSモジュール
import xlrd         # Excel読み込み
#import bekarazu     # べからず集警告番号

# -*- coding: sjis -*-
# 

flgBekarazuR01 = False
flgBekarazuR02 = False
flgBekarazuR03 = False
flgBekarazuR06 = False
flgBekarazuR07 = False
flgBekarazuR08 = False
flgBekarazuR09 = False
flgBekarazuR10 = False
flgBekarazuR11 = False
flgBekarazuR13 = False
flgBekarazuR14 = False
flgBekarazuR15 = False
flgBekarazuR16 = False
flgBekarazuR17 = False
flgBekarazuR18 = False
flgBekarazuR19 = False
flgBekarazuR20 = False
flgBekarazuR21 = False
flgBekarazuR22 = False
flgBekarazuR23 = False
flgBekarazuR24 = False
flgBekarazuR25 = False
flgBekarazuR26 = False
flgBekarazuM03 = False
flgBekarazuM04 = False
flgBekarazuM05 = False
flgBekarazuM06 = False
flgBekarazuM07 = False
flgBekarazuM09 = False
flgBekarazuM10 = False
flgBekarazuM11 = False
flgBekarazuM12 = False
flgBekarazuM13 = False
flgBekarazuM14 = False
flgBekarazuM15 = False
flgBekarazuM17 = False
flgBekarazuM19 = False
flgBekarazuM20 = False
flgBekarazuM21 = False
flgBekarazuM22 = False
flgBekarazuM23 = False
flgBekarazuM24 = False
flgBekarazuM25 = False
flgBekarazuM26 = False
flgBekarazuM27 = False
flgBekarazuM28 = False
flgBekarazuM29 = False
flgBekarazuM30 = False
flgBekarazuM32 = False
flgBekarazuM33 = False
flgBekarazuM34 = False
flgBekarazuM35 = False
flgBekarazuM36 = False
flgBekarazuM37 = False
flgBekarazuM38 = False
flgBekarazuM39 = False
flgBekarazuM40 = False
flgBekarazuM41 = False
flgBekarazuM42 = False
flgBekarazuM43 = False
flgBekarazuM44 = False
flgBekarazuP01 = False
flgBekarazuP02 = False
flgBekarazuP04 = False
flgBekarazuP05 = False
flgBekarazuP07 = False
flgBekarazuP08 = False
flgBekarazuP09 = False
flgBekarazuP11 = False

def qacWarnCount(inExcel, outText):

    inExcel =  xlrd.open_workbook(inExcel)

    warnList = {}

    CountWarn(warnList, inExcel.sheet_by_name('2.チェック結果'))
    CountWarn(warnList, inExcel.sheet_by_name('3.チェック結果 (Optimus)'))

    print('<< 警告リスト >>')

    for pwarnNo in warnList.keys():
        print('key:{0:04d}, val:{1}'.format(pwarnNo, warnList.get(pwarnNo)))

    print('\n\n<< べからずスコア >>')

    OutBekarazuScore()



# 警告のリストを作成
def CountWarn(warnList, sheetObj):


   # F列を終わりまでループ
    for row in range(4, sheetObj.nrows):

        warnNo = int(sheetObj.cell_value(row, 5))

        # 既にリストにある警告ならばカウントをインクリメント
        if 0 == warnList.get(warnNo, 0):
            warnList.setdefault(warnNo, 1)
        else:
            warnList[warnNo] = warnList.get(warnNo) + 1

        # べからず集チェック
        CheckBekarazu(warnNo)


# べからず集チェック　該当警告ならばフラグを立てる
def CheckBekarazu(warnNo):

    bekarazuR01 = [ 3321, 3347, 3348, 3349, 3353, 3354 ]
    bekarazuR02 = [  723 ]
    bekarazuR03 = [  488,  489 ]
    bekarazuR06 = [ 3341 ]
    bekarazuR07 = [ 3340 ]
    bekarazuR08 = [ 3302, 3303, 3304]
    bekarazuR09 = [ 4121, 4126, 4127, 4128 ]
    bekarazuR10 = [ 3908, 3909, 3910, 3912, 3913, 3915, 3917, 3919, 3920, 3921,
                    3923, 3925, 3927, 3929, 3930, 3931, 3932, 3934, 3935, 3936,
                    3938, 3940, 3941, 3942, 3943, 3945, 3946, 3947, 3948, 3950,
                    3952, 3953, 3954, 3956, 3957, 3958, 3959, 3960, 3962, 3963,
                    3964, 3965, 3967, 3968, 3969, 3970, 3971, 3972, 3974, 3975,
                    3976, 3978, 3979, 3980, 3981, 3982, 3983, 3984, 3985, 3986,
                    3987, 3989, 3990, 3991, 3992, 3993, 3994, 3995, 3996, 3997,
                    3998, 4034, 4037, 4039, 4040, 4043, 4044, 4047, 4048, 4051,
                    4052, 4053, 4054, 4055, 4056, 4057, 4058, 4059, 4060, 4061,
                    4062, 4064, 4065, 4066, 4067, 4068, 4069, 4070, 4071, 4072,
                    4073, 4074, 4075, 4120, 4240, 4241, 4242, 4243, 4244, 4245,
                    3878, 3879, 3880, 3881, 3999, 4000, 4001, 4002, 4003, 4004,
                    4005, 4006, 4007, 4010, 4011, 4012, 4013, 4014, 4015, 4016,
                    4017, 4018, 4019, 4021, 4022, 4023, 4024, 4025, 4026, 4027,
                    4028, 4029, 4030, 4031, 4076, 4077, 4078, 4079, 4080, 4081,
                    4123, 4124, 4125 ]
    bekarazuR11 = [ 3101, 3102 ]
    bekarazuR13 = [  499,  500,  501 ]
    bekarazuR14 = [  634,  635, 3660 ]
    bekarazuR15 = [ 4130, 4131 ]
    bekarazuR16 = [  302,  307,  313,  301,  303,  305,  306,  310 ]
    bekarazuR17 = [  311,  312 ]
    bekarazuR18 = [ 5069, 3200 ]
    bekarazuR19 = [ 3002, 3335, 3450, 1504, 1505, 1331, 1332, 1333, 3320,  626,
                     627,  628, 1510 ]
    bekarazuR20 = [ 3684 ]
    bekarazuR21 = [ 5069, 3200 ]
    bekarazuR22 = [ 1520, 3670 ]
    bekarazuR23 = [  594,  689, 1460, 1503, 2008, 2018, 3201, 3219, 3325, 2004 ]
    bekarazuR24 = [ 2002, 2009 ]
    bekarazuR25 = [ 3440 ]
    bekarazuR26 = [  400,  401,  402,  403 ]
    bekarazuM03 = [  735 ]
    bekarazuM04 = [ 3398, 3399, 3400 ]
    bekarazuM05 = [ 3389, 3391, 3392, 3393, 3394, 3395, 3396, 3397, 3417, 3418 ]
    bekarazuM06 = [  428 ]
    bekarazuM07 = [ 3344 ]
    bekarazuM09 = [ 2547, 3334, 1506, 1507, 1508, 3448,  547, 1525, 1526, 1527,
                    1528, 1529,  780,  781 ]
    bekarazuM10 = [  836,  848,  854, 3439, 5114, 5214, 5125,  602, 5115 ]
    bekarazuM11 = [ 3415 ]
    bekarazuM12 = [ 3411, 3412, 3413, 3431, 3458, 3460, 3461 ]
    bekarazuM13 = [ 3601 ]
    bekarazuM14 = [  336,  339, 3628 ]
    bekarazuM15 = [ 3109 ]
    bekarazuM17 = [ 3673 ]
    bekarazuM19 = [ 3115 ]
    bekarazuM20 = [  679,  686,  693,  694 ]
    bekarazuM21 = [ 3402 ]
    bekarazuM22 = [ 1514, 3218 ]
    bekarazuM23 = [ 3002, 3335, 3450, 1504, 1505 ]
    bekarazuM24 = [ 3002, 3335, 3450, 1504, 1505, 3224 ]
    bekarazuM25 = [  771, 3333 ]
    bekarazuM26 = [ 2001 ]
    bekarazuM27 = [  770 ]
    bekarazuM28 = [ 2003 ]
    bekarazuM29 = [ 2006 ]
    bekarazuM30 = [ 3389, 3391, 3392, 3393, 3394, 3395, 3396, 3397, 3417, 3418 ]
    bekarazuM32 = [ 2462, 2463 ]
    bekarazuM33 = [ 2469 ]
    bekarazuM34 = [ 3326 ]
    bekarazuM35 = [ 5102 ]
    bekarazuM36 = [ 1513, 3222, 3408, 3447, 3451 ]
    bekarazuM37 = [  842 ]
    bekarazuM38 = [  652, 1330, 1334 ]
    bekarazuM39 = [ 5087, 3410 ]
    bekarazuM40 = [ 3317, 3318 ]
    bekarazuM41 = [  885,  887,  888 ]
    bekarazuM42 = [  842 ]
    bekarazuM43 = [  841 ]
    bekarazuM44 = [  880,  881,  341,  342 ]
    bekarazuP01 = [  180,  240,  241,  246,  410,  551,  601,  604,  609,  611,
                     612,  614,  639,  647,  662,  715,  739,  810,  828,  830,
                     857,  858,  859,  875,  930, 1003, 1006, 1008, 1014, 1015,
                    1018, 1019, 1020, 1021, 1022, 1026, 1027, 1028, 1029, 1030,
                    1031, 1033, 1034, 1035, 1036, 1037, 1038, 1041, 1042, 1043,
                    1044, 1051, 1052, 1053, 1054, 3664 ]
    bekarazuP02 = [  202,  284,  285,  286,  287,  288,  289,  308,  878, 2850,
                    2851, 2852, 2853, 2855, 2856, 2857, 2860, 2861, 2862, 2890,
                    2895, 3702, 3703, 3704, 3705, 3706, 3707, 3832, 3833, 3902,
                    3903, 3904, 3905, 3906, 3907, 4032, 4033 ]
    bekarazuP04 = [  235 ]
    bekarazuP05 = [ 3711, 3722, 3733, 3744, 3755, 3766, 3777, 3788, 3850, 3863,
                    3911, 3922, 3933, 3944, 3955, 3966, 3977, 3988, 4050, 4063,
                    3700, 3701, 3900, 3901 ]
    bekarazuP07 = [  809 ]
    bekarazuP08 = [  813,  814,  831 ]
    bekarazuP09 = [ 3006 ]
    bekarazuP11 = [ 5013 ]

    global flgBekarazuR01
    global flgBekarazuR02
    global flgBekarazuR03
    global flgBekarazuR06
    global flgBekarazuR07
    global flgBekarazuR08
    global flgBekarazuR09
    global flgBekarazuR10
    global flgBekarazuR11
    global flgBekarazuR13
    global flgBekarazuR14
    global flgBekarazuR15
    global flgBekarazuR16
    global flgBekarazuR17
    global flgBekarazuR18
    global flgBekarazuR19
    global flgBekarazuR20
    global flgBekarazuR21
    global flgBekarazuR22
    global flgBekarazuR23
    global flgBekarazuR24
    global flgBekarazuR25
    global flgBekarazuR26
    global flgBekarazuM03
    global flgBekarazuM04
    global flgBekarazuM05
    global flgBekarazuM06
    global flgBekarazuM07
    global flgBekarazuM09
    global flgBekarazuM10
    global flgBekarazuM11
    global flgBekarazuM12
    global flgBekarazuM13
    global flgBekarazuM14
    global flgBekarazuM15
    global flgBekarazuM17
    global flgBekarazuM19
    global flgBekarazuM20
    global flgBekarazuM21
    global flgBekarazuM22
    global flgBekarazuM23
    global flgBekarazuM24
    global flgBekarazuM25
    global flgBekarazuM26
    global flgBekarazuM27
    global flgBekarazuM28
    global flgBekarazuM29
    global flgBekarazuM30
    global flgBekarazuM32
    global flgBekarazuM33
    global flgBekarazuM34
    global flgBekarazuM35
    global flgBekarazuM36
    global flgBekarazuM37
    global flgBekarazuM38
    global flgBekarazuM39
    global flgBekarazuM40
    global flgBekarazuM41
    global flgBekarazuM42
    global flgBekarazuM43
    global flgBekarazuM44
    global flgBekarazuP01
    global flgBekarazuP02
    global flgBekarazuP04
    global flgBekarazuP05
    global flgBekarazuP07
    global flgBekarazuP08
    global flgBekarazuP09
    global flgBekarazuP11

    # 信頼性

    if False == flgBekarazuR01:
        if True == (warnNo in bekarazuR01):
            flgBekarazuR01 = True

    if False == flgBekarazuR02:
        if True == (warnNo in bekarazuR02):
            flgBekarazuR02 = True

    if False == flgBekarazuR03:
        if True == (warnNo in bekarazuR03):
            flgBekarazuR03 = True

    if False == flgBekarazuR06:
        if True == (warnNo in bekarazuR06):
            flgBekarazuR06 = True

    if False == flgBekarazuR07:
        if True == (warnNo in bekarazuR07):
            flgBekarazuR07 = True

    if False == flgBekarazuR08:
        if True == (warnNo in bekarazuR08):
            flgBekarazuR08 = True

    if False == flgBekarazuR09:
        if True == (warnNo in bekarazuR09):
            flgBekarazuR09 = True

    if False == flgBekarazuR10:
        if True == (warnNo in bekarazuR10):
            flgBekarazuR10 = True

    if False == flgBekarazuR11:
        if True == (warnNo in bekarazuR11):
            flgBekarazuR11 = True

    if False == flgBekarazuR13 :
        if True == (warnNo in bekarazuR13):
            flgBekarazuR13 = True

    if False == flgBekarazuR14:
        if True == (warnNo in bekarazuR14):
            flgBekarazuR14 = True

    if False == flgBekarazuR15:
        if True == (warnNo in bekarazuR15):
            flgBekarazuR15 = True

    if False == flgBekarazuR16:
        if True == (warnNo in bekarazuR16):
            flgBekarazuR16 = True

    if False == flgBekarazuR17:
        if True == (warnNo in bekarazuR17):
            flgBekarazuR17 = True

    if False == flgBekarazuR18:
        if True == (warnNo in bekarazuR18):
            flgBekarazuR18 = True

    if False == flgBekarazuR19:
        if True == (warnNo in bekarazuR19):
            flgBekarazuR19 = True

    if False == flgBekarazuR20:
        if True == (warnNo in bekarazuR20):
            flgBekarazuR20 = True

    if False == flgBekarazuR21:
        if True == (warnNo in bekarazuR21):
            flgBekarazuR21 = True

    if False == flgBekarazuR22:
        if True == (warnNo in bekarazuR22):
            flgBekarazuR22 = True

    if False == flgBekarazuR23:
        if True == (warnNo in bekarazuR23):
            flgBekarazuR23 = True

    if False == flgBekarazuR24:
        if True == (warnNo in bekarazuR24):
            flgBekarazuR24 = True

    if False == flgBekarazuR25:
        if True == (warnNo in bekarazuR25):
            flgBekarazuR25 = True

    if False == flgBekarazuR26:
        if True == (warnNo in bekarazuR26):
            flgBekarazuR26 = True

    # 保守性

    if False == flgBekarazuM03:
        if True == (warnNo in bekarazuM03):
            flgBekarazuM03 = True

    if False == flgBekarazuM04:
        if True == (warnNo in bekarazuM04):
            flgBekarazuM04 = True

    if False == flgBekarazuM05:
        if True == (warnNo in bekarazuM05):
            flgBekarazuM05 = True

    if False == flgBekarazuM06:
        if True == (warnNo in bekarazuM06):
            flgBekarazuM06 = True

    if False == flgBekarazuM07:
        if True == (warnNo in bekarazuM07):
            flgBekarazuM07 = True

    if False == flgBekarazuM09:
        if True == (warnNo in bekarazuM09):
            flgBekarazuM09 = True

    if False == flgBekarazuM10:
        if True == (warnNo in bekarazuM10):
            flgBekarazuM10 = True

    if False == flgBekarazuM11:
        if True == (warnNo in bekarazuM11):
            flgBekarazuM11 = True

    if False == flgBekarazuM12:
        if True == (warnNo in bekarazuM12):
            flgBekarazuM12 = True

    if False == flgBekarazuM13:
        if True == (warnNo in bekarazuM13):
            flgBekarazuM13 = True

    if False == flgBekarazuM14:
        if True == (warnNo in bekarazuM14):
            flgBekarazuM14 = True

    if False == flgBekarazuM15:
        if True == (warnNo in bekarazuM15):
            flgBekarazuM15 = True

    if False == flgBekarazuM17:
        if True == (warnNo in bekarazuM17):
            flgBekarazuM17 = True

    if False == flgBekarazuM19:
        if True == (warnNo in bekarazuM19):
            flgBekarazuM19 = True

    if False == flgBekarazuM20:
        if True == (warnNo in bekarazuM20):
            flgBekarazuM20 = True

    if False == flgBekarazuM21:
        if True == (warnNo in bekarazuM21):
            flgBekarazuM21 = True

    if False == flgBekarazuM22:
        if True == (warnNo in bekarazuM22):
            flgBekarazuM22 = True

    if False == flgBekarazuM23:
        if True == (warnNo in bekarazuM23):
            flgBekarazuM23 = True

    if False == flgBekarazuM24:
        if True == (warnNo in bekarazuM24):
            flgBekarazuM24 = True

    if False == flgBekarazuM25:
        if True == (warnNo in bekarazuM25):
            flgBekarazuM25 = True

    if False == flgBekarazuM26:
        if True == (warnNo in bekarazuM26):
            flgBekarazuM26 = True

    if False == flgBekarazuM27:
        if True == (warnNo in bekarazuM27):
            flgBekarazuM27 = True

    if False == flgBekarazuM28:
        if True == (warnNo in bekarazuM28):
            flgBekarazuM28 = True

    if False == flgBekarazuM29:
        if True == (warnNo in bekarazuM29):
            flgBekarazuM29 = True

    if False == flgBekarazuM30:
        if True == (warnNo in bekarazuM30):
            flgBekarazuM30 = True

    if False == flgBekarazuM32:
        if True == (warnNo in bekarazuM32):
            flgBekarazuM32 = True

    if False == flgBekarazuM33:
        if True == (warnNo in bekarazuM33):
            flgBekarazuM33 = True

    if False == flgBekarazuM34:
        if True == (warnNo in bekarazuM34):
            flgBekarazuM34 = True

    if False == flgBekarazuM35:
        if True == (warnNo in bekarazuM35):
            flgBekarazuM35 = True

    if False == flgBekarazuM36:
        if True == (warnNo in bekarazuM36):
            flgBekarazuM36 = True

    if False == flgBekarazuM37:
        if True == (warnNo in bekarazuM37):
            flgBekarazuM37 = True

    if False == flgBekarazuM38:
        if True == (warnNo in bekarazuM38):
            flgBekarazuM38 = True

    if False == flgBekarazuM39:
        if True == (warnNo in bekarazuM39):
            flgBekarazuM39 = True

    if False == flgBekarazuM40:
        if True == (warnNo in bekarazuM40):
            flgBekarazuM40 = True

    if False == flgBekarazuM41:
        if True == (warnNo in bekarazuM41):
            flgBekarazuM41 = True

    if False == flgBekarazuM42:
        if True == (warnNo in bekarazuM42):
            flgBekarazuM42 = True

    if False == flgBekarazuM43:
        if True == (warnNo in bekarazuM43):
            flgBekarazuM43 = True

    if False == flgBekarazuM44:
        if True == (warnNo in bekarazuM44):
            flgBekarazuM44 = True

    # 保守性

    if False == flgBekarazuP01:
        if True == (warnNo in bekarazuP01):
            flgBekarazuP01 = True

    if False == flgBekarazuP02:
        if True == (warnNo in bekarazuP02):
            flgBekarazuP02 = True

    if False == flgBekarazuP04:
        if True == (warnNo in bekarazuP04):
            flgBekarazuP04 = True

    if False == flgBekarazuP05:
        if True == (warnNo in bekarazuP05):
            flgBekarazuP05 = True

    if False == flgBekarazuP07:
        if True == (warnNo in bekarazuP07):
            flgBekarazuP07 = True

    if False == flgBekarazuP08:
        if True == (warnNo in bekarazuP08):
            flgBekarazuP08 = True

    if False == flgBekarazuP09:
        if True == (warnNo in bekarazuP09):
            flgBekarazuP09 = True

    if False == flgBekarazuP11:
        if True == (warnNo in bekarazuP11):
            flgBekarazuP11 = True

def OutBekarazuScore():

    global flgBekarazuR01
    global flgBekarazuR02
    global flgBekarazuR03
    global flgBekarazuR06
    global flgBekarazuR07
    global flgBekarazuR08
    global flgBekarazuR09
    global flgBekarazuR10
    global flgBekarazuR11
    global flgBekarazuR13
    global flgBekarazuR14
    global flgBekarazuR15
    global flgBekarazuR16
    global flgBekarazuR17
    global flgBekarazuR18
    global flgBekarazuR19
    global flgBekarazuR20
    global flgBekarazuR21
    global flgBekarazuR22
    global flgBekarazuR23
    global flgBekarazuR24
    global flgBekarazuR25
    global flgBekarazuR26
    global flgBekarazuM03
    global flgBekarazuM04
    global flgBekarazuM05
    global flgBekarazuM06
    global flgBekarazuM07
    global flgBekarazuM09
    global flgBekarazuM10
    global flgBekarazuM11
    global flgBekarazuM12
    global flgBekarazuM13
    global flgBekarazuM14
    global flgBekarazuM15
    global flgBekarazuM17
    global flgBekarazuM19
    global flgBekarazuM20
    global flgBekarazuM21
    global flgBekarazuM22
    global flgBekarazuM23
    global flgBekarazuM24
    global flgBekarazuM25
    global flgBekarazuM26
    global flgBekarazuM27
    global flgBekarazuM28
    global flgBekarazuM29
    global flgBekarazuM30
    global flgBekarazuM32
    global flgBekarazuM33
    global flgBekarazuM34
    global flgBekarazuM35
    global flgBekarazuM36
    global flgBekarazuM37
    global flgBekarazuM38
    global flgBekarazuM39
    global flgBekarazuM40
    global flgBekarazuM41
    global flgBekarazuM42
    global flgBekarazuM43
    global flgBekarazuM44
    global flgBekarazuP01
    global flgBekarazuP02
    global flgBekarazuP04
    global flgBekarazuP05
    global flgBekarazuP07
    global flgBekarazuP08
    global flgBekarazuP09
    global flgBekarazuP11

    # 信頼性
    cntShinrai = 0

    if True == flgBekarazuR01:
        cntShinrai += 1

    if True == flgBekarazuR02:
        cntShinrai += 1

    if True == flgBekarazuR03:
        cntShinrai += 1

    if True == flgBekarazuR06:
        cntShinrai += 1

    if True == flgBekarazuR07:
        cntShinrai += 1

    if True == flgBekarazuR08:
        cntShinrai += 1

    if True == flgBekarazuR09:
        cntShinrai += 1

    if True == flgBekarazuR10:
        cntShinrai += 1

    if True == flgBekarazuR11:
        cntShinrai += 1

    if True == flgBekarazuR13:
        cntShinrai += 1

    if True == flgBekarazuR14:
        cntShinrai += 1

    if True == flgBekarazuR15:
        cntShinrai += 1

    if True == flgBekarazuR16:
        cntShinrai += 1

    if True == flgBekarazuR17:
        cntShinrai += 1

    if True == flgBekarazuR18:
        cntShinrai += 1

    if True == flgBekarazuR19:
        cntShinrai += 1

    if True == flgBekarazuR20:
        cntShinrai += 1

    if True == flgBekarazuR21:
        cntShinrai += 1

    if True == flgBekarazuR22:
        cntShinrai += 1

    if True == flgBekarazuR23:
        cntShinrai += 1

    if True == flgBekarazuR24:
        cntShinrai += 1

    if True == flgBekarazuR25:
        cntShinrai += 1

    if True == flgBekarazuR26:
        cntShinrai += 1

    # 保守性
    cntHosyu = 0

    if True == flgBekarazuM03:
        cntHosyu += 1

    if True == flgBekarazuM04:
        cntHosyu += 1

    if True == flgBekarazuM05:
        cntHosyu += 1

    if True == flgBekarazuM06:
        cntHosyu += 1

    if True == flgBekarazuM07:
        cntHosyu += 1

    if True == flgBekarazuM09:
        cntHosyu += 1

    if True == flgBekarazuM10:
        cntHosyu += 1

    if True == flgBekarazuM11:
        cntHosyu += 1

    if True == flgBekarazuM12:
        cntHosyu += 1

    if True == flgBekarazuM13:
        cntHosyu += 1

    if True == flgBekarazuM14:
        cntHosyu += 1

    if True == flgBekarazuM15:
        cntHosyu += 1

    if True == flgBekarazuM17:
        cntHosyu += 1

    if True == flgBekarazuM19:
        cntHosyu += 1

    if True == flgBekarazuM20:
        cntHosyu += 1

    if True == flgBekarazuM21:
        cntHosyu += 1

    if True == flgBekarazuM22:
        cntHosyu += 1

    if True == flgBekarazuM23:
        cntHosyu += 1

    if True == flgBekarazuM24:
        cntHosyu += 1

    if True == flgBekarazuM25:
        cntHosyu += 1

    if True == flgBekarazuM26:
        cntHosyu += 1

    if True == flgBekarazuM27:
        cntHosyu += 1

    if True == flgBekarazuM28:
        cntHosyu += 1

    if True == flgBekarazuM29:
        cntHosyu += 1

    if True == flgBekarazuM30:
        cntHosyu += 1

    if True == flgBekarazuM32:
        cntHosyu += 1

    if True == flgBekarazuM33:
        cntHosyu += 1

    if True == flgBekarazuM34:
        cntHosyu += 1

    if True == flgBekarazuM35:
        cntHosyu += 1

    if True == flgBekarazuM36:
        cntHosyu += 1

    if True == flgBekarazuM37:
        cntHosyu += 1

    if True == flgBekarazuM38:
        cntHosyu += 1

    if True == flgBekarazuM39:
        cntHosyu += 1

    if True == flgBekarazuM40:
        cntHosyu += 1

    if True == flgBekarazuM41:
        cntHosyu += 1

    if True == flgBekarazuM42:
        cntHosyu += 1

    if True == flgBekarazuM43:
        cntHosyu += 1

    if True == flgBekarazuM44:
        cntHosyu += 1

    # 移植性
    cntIsyoku = 0

    if True == flgBekarazuP01:
        cntIsyoku += 1

    if True == flgBekarazuP02:
        cntIsyoku += 1

    if True == flgBekarazuP04:
        cntIsyoku += 1

    if True == flgBekarazuP05:
        cntIsyoku += 1

    if True == flgBekarazuP07:
        cntIsyoku += 1

    if True == flgBekarazuP08:
        cntIsyoku += 1

    if True == flgBekarazuP09:
        cntIsyoku += 1

    if True == flgBekarazuP11:
        cntIsyoku += 1

    print('信頼性:{0:.1f} 保守性：{1:.1f} 移植性：{2:.1f}'.format(100 - ((cntShinrai / 26) * 100), 100 - ((cntHosyu / 44) * 100), 100 - ((cntIsyoku / 11) * 100)))
