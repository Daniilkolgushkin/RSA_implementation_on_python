#Kolgushkin Daniil
#RSA - test 19.09.2019
#18.09.2019

#imports------------------------------------------------------
import random
from secrets import randbelow
import math
import datetime
#end of imports-----------------------------------------------

#long arichmetics---------------------------------------------
class number:
    #base = 0
    #lbase = 0
    #digits = []
    def __init__(self, bas, inp =""):
        self.base = bas
        self.lbase = int(math.log10(bas))
        self.digits = []
       # print(lbase)
       # print(len(inp))
        c = 1
        if (len(inp) > 0 and str(inp[0]) == "-"):
            c = -1
            inp = inp[1:]
        for i in range(math.ceil(len(inp) / self.lbase)):
        #    print(c)
            self.digits.append(c * int(inp[len(inp) - int(min(len(inp), self.lbase * i + self.lbase)) : len(inp) - int(self.lbase * i)]))
    def __str__(self):
        res = []
      #  print(res)
      #  print(len(self.digits))
        if self.digits[len(self.digits) - 1] < 0:
            res.append("-")
        for i in range(len(self.digits)):
            tmp = str(abs(self.digits[len(self.digits) - i - 1]))
            if (len(tmp) < self.lbase and i != 0):
                tmp = '0'*(self.lbase - len(tmp)) + tmp
            res.append(tmp)
      #  print(res)
        return "".join(res)
    def getdigit(self, num):
        if (num < len(self.digits)):
            return self.digits[num]
        else:
            return 0
    def __add__(self, other):
        res = []
        rn = number(self.base, '')
        for i in range(max(len(self.digits), len(other.digits))):
            res.append(self.getdigit(i) + other.getdigit(i))
        rn.digits = res
        return rn
    def __sub__(self, other):
        res = []
        rn = number(self.base, '')
        for i in range(max(len(self.digits), len(other.digits))):
            res.append(self.getdigit(i) - other.getdigit(i))
        rn.digits = res
        return rn
    def __mul__(self, other):
        res = []
        rn = number(self.base, '0')
        p1 = number(self.base, '0')
        p2 = number(self.base, '0')
        p3 = number(self.base, '0')
        p4 = number(self.base, '0')
        A1 = 0
        A2 = 0
        A3 = 0
        k = max(math.ceil(len(self.digits) / 2), math.ceil(len(other.digits) / 2))
        if (len(self.digits) == 0):
            return number(self.base, '0')
        elif (len(other.digits) == 0):
            return number(other.base, '0')
        elif (len(self.digits) == 1):
            for i in range(len(other.digits)):
                res.append(self.digits[0]*other.digits[i])
            rn.digits = res
            rn.normalize()
            return rn
        elif (len(other.digits) == 1):
            for i in range(len(self.digits)):
                res.append(self.digits[i]*other.digits[0])
            rn.digits = res
            rn.normalize()
            return rn
        else:
            tmp1 = min(k, len(self.digits))
            tmp = []
            for i in range(tmp1):
                tmp.append(self.digits[i])
            p2.digits = tmp
            tmp = []
            tmp1 = min(k, len(other.digits))
            for i in range(tmp1):
                tmp.append(other.digits[i])
            p4.digits = tmp
            A3 = p4*p2
            if (len(other.digits) <= k):
                tmp = []
                for i in range(len(self.digits) - k):
                    tmp.append(self.digits[i + k])
                p1.digits = tmp
                A2 = p1*p4
                tmp = [0]*(k)
                A2.digits = tmp + A2.digits
                return A2 + A3
            elif (len(self.digits) <= k):
                tmp = []
                for i in range(len(other.digits) - k):
                    tmp.append(other.digits[i + k])
                p3.digits = tmp
                A2 = p2*p3
                tmp = [0]*(k)
                A2.digits = tmp + A2.digits
                return A2 + A3
            else:
                tmp = []
                for i in range(len(self.digits) - k):
                    tmp.append(self.digits[i + k])
                p1.digits = tmp
                tmp = []
                for i in range(len(other.digits) - k):
                    tmp.append(other.digits[i + k])
                p3.digits = tmp
                A1 = p1*p3
                tmp = [0]*2*(k)
                A1.digits = tmp + A1.digits
                A2 = p2*p3 + p1*p4
                tmp = [0]*(k)
                A2.digits = tmp + A2.digits
                return A1 + A2 + A3
    def __floordiv__(self, other):
        if (other > self):
            return number(self.base, '0')
        elif(other == self):
            return number(self.base, '1')
        else:
            rn = number(self.base, '0')
            res = []
            tmp = number(self.base, '0')
            dig = 0;
            for i in range(len(other.digits)):
                res.append(self.digits[i + len(self.digits) - len(other.digits)])
            tmp.digits = res
            res = []
            count = len(self.digits) - len(other.digits)
            while True:
                ledge = 0
                redge = self.base
                while True:
                    dig = (ledge + redge) // 2
                    med = []
                    for i in range(len(other.digits)):
                        med.append(dig*other.digits[i])
                    tmp1 = number(self.base, '')
                    tmp1.digits = med
                    if tmp1 > tmp:
                        redge = dig
                    elif tmp1 < tmp:
                        ledge = dig
                    else:
                        break
                    if abs(ledge - redge) <= 1:
                        break
                dig = (ledge + redge) // 2
                res = [dig] + res
                tmp = tmp - other * number(other.base, str(dig))
                count -= 1
                print()
                if count < 0:
                    break
                tmp.digits = [self.digits[count]] + tmp.digits
            rn.digits = res
            print(rn)
            return rn
    def __mod__(self, other):
        if (other > self):
            return self
        elif(other == self):
            return number(self.base, '0')
        else:
            res = []
            tmp = number(self.base, '0')
            dig = 0;
            for i in range(len(other.digits)):
                res.append(self.digits[i + len(self.digits) - len(other.digits)])
            tmp.digits = res
            res = []
            count = len(self.digits) - len(other.digits)
            while True:
                ledge = 0
                redge = self.base
                while True:
                    dig = (ledge + redge) // 2
                    med = []
                    for i in range(len(other.digits)):
                        med.append(dig*other.digits[i])
                    tmp1 = number(self.base, '')
                    tmp1.digits = med
                    if tmp1 > tmp:
                        redge = dig
                    elif tmp1 < tmp:
                        ledge = dig
                    else:
                        break
                    if abs(ledge - redge) <= 1:
                        break
                dig = (ledge + redge) // 2
                res = [dig] + res
                tmp = tmp - other * number(other.base, str(dig))
                count -= 1
                if count < 0:
                    break
                tmp.digits = [self.digits[count]] + tmp.digits
            return tmp

    def __pow__(self, p):
        l = len (bin(p)) - 2
        res = number(self.base, '1')
        for i in range(l):
            tmp = p >> (i)
            if tmp % 2 != 0:
                tmp1 = self
                for j in range (i):
                    tmp1 = ((tmp1) * (tmp1))
                res = (res * tmp1)
        return (res)

    def __lt__(self, other):
        self.normalize()
        other.normalize()
        for i in range(max(len(self.digits), len(other.digits))):
            if (self.getdigit(max(len(self.digits), len(other.digits)) - i - 1) > other.getdigit(max(len(self.digits), len(other.digits)) - i - 1)):
                return False
            if (self.getdigit(max(len(self.digits), len(other.digits)) - i - 1) < other.getdigit(max(len(self.digits), len(other.digits)) - i - 1)):
                return True
        return False
    def __gt__(self, other):
        self.normalize()
        other.normalize()
        for i in range(max(len(self.digits), len(other.digits))):
            if (self.getdigit(max(len(self.digits), len(other.digits)) - i - 1) < other.getdigit(max(len(self.digits), len(other.digits)) - i - 1)):
                return False
            if (self.getdigit(max(len(self.digits), len(other.digits)) - i - 1) > other.getdigit(max(len(self.digits), len(other.digits)) - i - 1)):
                return True
        return False
    def __eq__(self, other):
        self.normalize()
        other.normalize()
        for i in range(max(len(self.digits), len(other.digits))): 
            if (self.getdigit(max(len(self.digits), len(other.digits)) - i - 1) != other.getdigit(max(len(self.digits), len(other.digits)) - i - 1)):
                return False
        return True
    def __le__(self, other):
        return (self < other or self == other)
    def __ge__(self, other):
        return (self > other or self == other)
    def normalize(self):
        for i in range(len(self.digits)):
            if (abs(self.digits[i]) >= self.base):
                tmp = self.digits[i]
                self.digits[i] = self.digits[i] % self.base
                if (i == len(self.digits) - 1):
                    self.digits.append(0)
                self.digits[i + 1] += tmp // self.base
        while (len(self.digits) != 1 and self.digits[len(self.digits) - 1] == 0):
            del self.digits[len(self.digits) - 1]
        if (self.digits[len(self.digits) - 1] < 0):
            for i in range(len(self.digits)):
                if (self.digits[i] > 0):
                    self.digits[i] -= self.base
                    self.digits[i + 1] += 1
        else:
            for i in range(len(self.digits)):
                if (self.digits[i] < 0):
                    self.digits[i] += self.base
                    self.digits[i + 1] -= 1
        while (len(self.digits) != 1 and self.digits[len(self.digits) - 1] == 0):
            del self.digits[len(self.digits) - 1]

#end of long arichmetics--------------------------------------

#moduled multiplication---------------------------------------
def mMult(a, b, n):
    l = len (bin (b)) - 2
    res = 0
    for i in range(l):
        tmp = b >> (i)
        if tmp % 2 != 0:
            tmp = a % n
            for j in range (i):
                tmp = ((tmp % n) * 2) % n
            res = (res + tmp) % n
    return (res)
#end of moduled multiplication--------------------------------

#moduled power------------------------------------------------
def mPower(a, p, n):
    l = len (bin (p)) - 2
    res = 1
    for i in range(l):
        tmp = p >> (i)
        if tmp % 2 != 0:
            tmp = a % n
            for j in range (i):
                tmp = ((tmp % n) ** 2) % n
            res = (res * tmp) % n
    return (res)
#end of moduled power-----------------------------------------

#miller-rabin's test------------------------------------------
def primetest(n, k):
    testmass = open('output.out', 'r')
    for line in testmass:
        if (n % int(line) == 0):
            return False
    t = n - 1
    s = 0
    while (t % 2 == 0):
        t = t // 2
        s += 1
    for i in range (k):
        a = random.randint(2, n - 2)
        x = mPower(a, t, n)
        if (x == 1 or x == n - 1):
            continue        
        for j in range (s - 1):
            x = ((x % n) ** 2) % n
            if (x == 1):
                return False
            if (x == n - 1):
                break
        else:
            return False
    return True
#end of miller-rabin's test-----------------------------------

#big hardprime generator--------------------------------------
def primegen(le, te):
   # te = te // 3
    x = (randbelow(te - le) + le)
    x += x % 2 - 1
    while (True):
        if (not primetest(x, 1)):
            x += 2
            continue
        else:
            break 
    return x
#end of big hardprime generator-----------------------------

#solution of diafant equation--------------------------------
def diafsolve(a, b):
    x = []
    r = []
    r.append(b)
    r.append(a % b)
    x.append(0)
    x.append(1)
    i = 0
    print (str(x[i % 2]) + " x")
    print (str(r[i % 2]) + " r")

    while (r[(i) % 2] != 1):
        x[i % 2] = (x[i % 2] - (r[i % 2] // r[(i + 1) % 2]) * x[(i + 1) % 2])
        r[i % 2] = (r[i % 2] % r[(i + 1) % 2])
        print (str(x[i % 2]) + " x")
        print (str(r[i % 2]) + " r")
        i += 1
    #while (x[i % 2] <= 0):
    #    x[i % 2] += b
    if (x[i % 2] <= 0):
        x[i % 2] += (-x[i % 2] // b + 1) * b
    return (x[i % 2])
#end of solution of diafant equation------------------------

#key generation---------------------------------------------
def keygen(keylen, tst = 0):
    ple = 1
    ple = ple << keylen - 1
    minrange = (ple - ple >> 1 - 1) // 100 
    pte = 1
    pte = pte << keylen
    pte -= 1
   #print (ple)
   #print (pte)
    while (True):
        p = primegen(5, pte >> (keylen // 3))
        Lqle = ple // p
        Rqte = pte // p
        #Lqte = p // 2
        #Rqle = 2 * p
        #q = 1
        if minrange <= (Rqte - Lqle):
            q = primegen(Lqle, Rqte)
            #if (Rqte - Rqle < Lqte - Rqte):
             #   q = primegen(Lqle, Lqte)
            #else:
             #   q = primegen(Rqle, Rqte)
        else:
            continue
        break
       # q = primegen(Lqle, Rqte)
    n = p * q
    f = mMult((p - 1), (q - 1), n)
    e = primegen(f // 55, f // 5)
    d = diafsolve(e, f)
    privatkey = open('privat.key', 'w')
    publickey = open('public.key', 'w')
    privatkey.write(str(d) + '\n' + str(n))
    publickey.write(str(e) + '\n' + str(n))
    if (tst == 1):
        print (str(p) + ' ' + str(q) + ' ' + str(n) + ' ' + str(f) + ' ' + str(e) + ' ' + str(d) + '\n' + 27 + '\n')
        print (str(mPower(27, e, n)) + '\n')
        print (str(mPower(27, d, n)) + '\n')
    privatkey.close()
    publickey.close()
    return 0
#end of key generation--------------------------------------

#encrypting-------------------------------------------------
def encrypt(inname, outname):
    inp = open(inname, 'rb')
    key = open('public.key', 'r')
    out = open(outname, 'w')
    e = int(key.readline())
    n = int(key.readline())
    current = []
    current.append(inp.read(3))
    i = 0
    while (current[i] != b''):
        current.append(inp.read(3))
        i += 1
    i = 0
    for i in range(len(current) - 1):
        current[i] = mPower(int.from_bytes(current[i], byteorder='little'), e, n)
        out.write(str(current[i]) + ' ')
    inp.close()
    key.close()
    out.close()
    return 0
#end of encrypting------------------------------------------

#decryption-------------------------------------------------
def decrypt(inname, outname):
    inp = open(inname, 'r')
    key = open('privat.key', 'r')
    out = open(outname, 'w')
    d = int(key.readline())
    n = int(key.readline())
    current = inp.read()
    current = current.split(' ')
    for i in range(len(current)):
        if (current[i] != ''):
            prtb = (mPower(int(current[i]), d, n).to_bytes(3, byteorder='little')).decode('utf-8')
            for j in range(len(prtb)):
                if (prtb[j] != '\0' ):
                    out.write(prtb[j])
    inp.close()
    key.close()
    out.close()
    return 0
#end of decryption------------------------------------------
#a = (input())
#b = (input())
#c = int(input())
#print(-13 % 10)
#if b[0] == "-":
#    b = b[1:]
#else:
#b = "-" + b
b = datetime.datetime.now()
keygen(256)

#print(diafsolve(265828085806221232860719200134904897753, 306368584669373876582051392872309529776))

#print (datetime.datetime.now() - b)
a = number(10, "816")
c = number(10, "68")
lc = a // c
print(lc)
encrypt("testinput", "testoutput")
decrypt("testoutput", "testoutput2")
#encrypt("SBib", "SBib1")
#decrypt("SBib1", "SBib2")
#base = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#tst = number(base, a)
#tst2 = number(base, b)
#tst3 = tst * tst2

#print(diafsolve(17, 57))

#ledge1 = number(base, '')
#redge1 = number(base, '')

#print([0] * (len(tst.digits) // 4) + [1])

#ledge1.digits = [0]*((len(tst.digits) - 1) // 2) + [1]
#redge1.digits = [0]*((len(tst.digits) + 1) // 2) + [1]
#print([0] * (len(tst.digits) // 4) + [1])
#print(ledge1)
#print(redge1)
#l = number(base, '1')
#t = number(base, '2')
#while ledge1 * ledge1 <= tst:
#        ledge1 += l
#ans = (ledge1 - l)
#ans.normalize()
#print(ans)
#while True:
#    med = (ledge1 + redge1) // t
#    medl = med + l
#    ms = med * med
#    m1s = medl * medl
#    if (ms <= tst and m1s > tst):
#        med.normalize()
#        print (med)
#        break
#    elif (m1s <= tst):
#        ledge1 = med
#    elif (ms > tst):
#        redge1 = med
print (datetime.datetime.now() - b)

#tst3.normalize()

#print (tst3)

#print(tst)
#print(str(mMult(a, b, c)))
##cfg = input()
##cfg = cfg.split(' ')
#print(diafsolve(int(cfg[0]),int(cfg[1])))
#print (int(cfg[0]))
##if (int(cfg[0]) == 1):
  ##  keygen(int(cfg[1]))
##if (int(cfg[0]) == 2):
  ##  keygen(int(cfg[1]), 1)
##if (int(cfg[1 + int(cfg[0])]) == 1):
   ## decrypt(cfg[2 + int(cfg[0])], cfg[3 + int(cfg[0])])
##if (int(cfg[1 + int(cfg[0])]) == 2):
  ##  encrypt(cfg[2 + int(cfg[0])], cfg[3 + int(cfg[0])])
