M0 = [98, 89, 52]
M1 = [57, 95, 80, 92, 57, 78]
M2 = [82, 74, 97, 75, 51, 92, 83]
M3 = [97, 88, 51, 68, 76]
M4 = [63]
M5 = [94, 91, 51, 63]
M6 = [61, 54, 94, 71, 74, 68, 98, 83]
M7 = [90, 56]
I0 = 0
I1 = 0
I2 = 0
I3 = 0
I4 = 0
I5 = 0
I6 = 0
I7 = 0


def Monkey0(M0, I0):
    NM6 = []
    NM1 = []
    for j in range(len(M0)):
        M0[j] = int((M0[j] * 2))
        if M0[j] > 9699690:
            M0[j] = M0[j] % 9699690
    for j in M0:
        I0 += 1
        if j % 5 == 0:
            NM6.append(j)
        else:
            NM1.append(j)
    return NM6, NM1, I0


def Monkey1(M1, I1):
    NM2 = []
    NM6 = []
    for j in range(len(M1)):
        M1[j] = int((M1[j] * 13))
        if M1[j] > 9699690:
            M1[j] = M1[j] % 9699690
    for j in M1:
        I1 += 1
        if j % 2 == 0:
            NM2.append(j)
        else:
            NM6.append(j)
    return NM2, NM6, I1


def Monkey2(M2, I2):
    NM7 = []
    NM5 = []
    for j in range(len(M2)):
        M2[j] = int((M2[j] + 5))
        if M2[j] > 9699690:
            M2[j] = M2[j] % 9699690
    for j in M2:
        I2 += 1
        if j % 19 == 0:
            NM7.append(j)
        else:
            NM5.append(j)
    return NM7, NM5, I2


def Monkey3(M3, I3):
    NM0 = []
    NM4 = []
    for j in range(len(M3)):
        M3[j] = int((M3[j] + 6))
        if M3[j] > 9699690:
            M3[j] = M3[j] % 9699690
    for j in M3:
        I3 += 1
        if j % 7 == 0:
            NM0.append(j)
        else:
            NM4.append(j)
    return NM0, NM4, I3


def Monkey4(M4, I4):
    NM0 = []
    NM1 = []
    for j in range(len(M4)):
        M4[j] = int((M4[j] + 1))
        if M4[j] > 9699690:
            M4[j] = M4[j] % 9699690
    for j in M4:
        I4 += 1
        if j % 17 == 0:
            NM0.append(j)
        else:
            NM1.append(j)
    return NM0, NM1, I4


def Monkey5(M5, I5):
    NM4 = []
    NM3 = []
    for j in range(len(M5)):
        M5[j] = int((M5[j] + 4))
        if M5[j] > 9699690:
            M5[j] = M5[j] % 9699690
    for j in M5:
        I5 += 1
        if j % 13 == 0:
            NM4.append(j)
        else:
            NM3.append(j)
    return NM4, NM3, I5


def Monkey6(M6, I6):
    NM2 = []
    NM7 = []
    for j in range(len(M6)):
        M6[j] = int((M6[j] + 2))
        if M6[j] > 9699690:
            M6[j] = M6[j] % 9699690
    for j in M6:
        I6 += 1
        if j % 3 == 0:
            NM2.append(j)
        else:
            NM7.append(j)
    return NM2, NM7, I6


def Monkey7(M7, I7):
    NM3 = []
    NM5 = []
    for j in range(len(M7)):
        M7[j] = int((M7[j] * M7[j]))
        if M7[j] > 9699690:
            M7[j] = M7[j] % 9699690
    for j in M7:
        I7 += 1
        if j % 11 == 0:
            NM3.append(j)
        else:
            NM5.append(j)
    return NM3, NM5, I7


for i in range(10000):
    print(i)
    x, y, I0 = Monkey0(M0, I0)
    M6 += x
    M1 += y
    M0 = []
    x, y, I1 = Monkey1(M1, I1)
    M2 += x
    M6 += y
    M1 = []
    x, y, I2 = Monkey2(M2, I2)
    M7 += x
    M5 += y
    M2 = []
    x, y, I3 = Monkey3(M3, I3)
    M0 += x
    M4 += y
    M3 = []
    x, y, I4 = Monkey4(M4, I4)
    M0 += x
    M1 += y
    M4 = []
    x, y, I5 = Monkey5(M5, I5)
    M4 += x
    M3 += y
    M5 = []
    x, y, I6 = Monkey6(M6, I6)
    M2 += x
    M7 += y
    M6 = []
    x, y, I7 = Monkey7(M7, I7)
    M3 += x
    M5 += y
    M7 = []
    print(max(M1))
monkeys = [I0, I1, I2, I3, I4, I5, I6, I7]
monkeys.sort()
print(monkeys[-1] * monkeys[-2])
