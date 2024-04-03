# Andrew Butler             11-3-2022
# Lab week 11 - exercise #1

# 27 variations + functions for each
#01 A+B+C+D AAA
def calcAAA(a, b, c, d):
    return a+b+c+d
#02 A+B+C-D AAS
def calcAAS(a, b, c, d):
    return a+b+c-d
#03 A+B-C+D ASA
def calcASA(a, b, c, d):
    return a+b-c+d
#04 A+B-C-D ASS
def calcASS(a, b, c, d):
    return a+b-c-d
#05 A+B+C*D AAM
def calcAAM(a, b, c, d):
    return a+b+c*d
#06 A+B*C+D AMA
def calcAMA(a, b, c, d):
    return a+b*c+d
#07 A+B-C*D ASM
def calcASM(a, b, c, d):
    return a+b-c*d
#08 A+B*C-D AMS
def calcAMS(a, b, c, d):
    return a+b*c-d
#09 A+B*C*D AMM
def calcAMM(a, b, c, d):
    return a+b*c*d


#10 A-B+C+D SAA
def calcSAA(a, b, c, d):
    return a-b+c+d
#11 A-B+C-D SAS
def calcSAS(a, b, c, d):
    return a-b+c-d
#12 A-B-C+D SSA
def calcSSA(a, b, c, d):
    return a-b-c+d
#13 A-B-C-D SSS
def calcSSS(a, b, c, d):
    return a-b-c-d
#14 A-B+C*D SAM
def calcSAM(a, b, c, d):
    return a-b+c*d
#15 A-B*C+D SMA
def calcSMA(a, b, c, d):
    return a-b*c+d
#16 A-B-C*D SSM
def calcSSM(a, b, c, d):
    return a-b-c*d
#17 A-B*C-D SMS
def calcSMS(a, b, c, d):
    return a-b*c-d
#18 A-B*C*D SMM
def calcSMM(a, b, c, d):
    return a-b*c*d


#19 A*B+C+D MAA
def calcMAA(a, b, c, d):
    return a*b+c+d
#20 A*B+C-D MAS
def calcMAS(a, b, c, d):
    return a*b+c-d
#21 A*B-C+D MSA
def calcMSA(a, b, c, d):
    return a*b-c+d
#22 A*B-C-D MSS
def calcMSS(a, b, c, d):
    return a*b-c-d
#23 A*B+C*D MAM
def calcMAM(a, b, c, d):
    return a*b+c*d
#24 A*B*C+D MMA
def calcMMA(a, b, c, d):
    return a*b*c+d
#25 A*B-C*D MSM
def calcMSM(a, b, c, d):
    return a*b-c*d
#26 A*B*C-D MMS
def calcMMS(a, b, c, d):
    return a*b*c-d
#27 A*B*C*D MMM
def calcMMM(a, b, c, d):
    return a*b*c*d


def main():
    a = int(input("Enter an integer a: "))
    b = int(input("Enter an integer b: "))
    c = int(input("Enter an integer c: "))
    d = int(input("Enter an integer d: "))

    dict = {}

    # assigning calculated values to key with name of operators used for each of the 27 variations
    dict["AAA"] = calcAAA(a, b, c, d)
    dict["AAS"] = calcAAS(a, b, c, d)
    dict["ASA"] = calcASA(a, b, c, d)
    dict["ASS"] = calcASS(a, b, c, d)
    dict["AAM"] = calcAAM(a, b, c, d)
    dict["AMA"] = calcAMA(a, b, c, d)
    dict["ASM"] = calcASM(a, b, c, d)
    dict["AMS"] = calcAMS(a, b, c, d)
    dict["AMM"] = calcAMM(a, b, c, d)

    dict["SAA"] = calcSAA(a, b, c, d)
    dict["SAS"] = calcSAS(a, b, c, d)
    dict["SSA"] = calcSSA(a, b, c, d)
    dict["SSS"] = calcSSS(a, b, c, d)
    dict["SAM"] = calcSAM(a, b, c, d)
    dict["SMA"] = calcSMA(a, b, c, d)
    dict["SSM"] = calcSSM(a, b, c, d)
    dict["SMS"] = calcSMS(a, b, c, d)
    dict["SMM"] = calcSMM(a, b, c, d)

    dict["MAA"] = calcMAA(a, b, c, d)
    dict["MAS"] = calcMAS(a, b, c, d)
    dict["MSA"] = calcMSA(a, b, c, d)
    dict["MSS"] = calcMSS(a, b, c, d)
    dict["MAM"] = calcMAA(a, b, c, d)
    dict["MMA"] = calcMMA(a, b, c, d)
    dict["MSM"] = calcMSM(a, b, c, d)
    dict["MMS"] = calcMMS(a, b, c, d)
    dict["MMM"] = calcMMM(a, b, c, d)

    for key in dict:
        print(key + ": " + str(dict[key]))
    

if __name__ == "__main__":
    main()