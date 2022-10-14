import numpy as np
import collections
import random
from collections import ChainMap


pp = []


s_box = [0xC, 0x5, 0x6, 0xB, 0x9, 0x0, 0xA, 0xD, 0x3, 0xE, 0xF, 0x8, 0x4, 0x7, 0x1, 0x2]
inv_sbox = [s_box.index(x) for x in range(len(s_box))]
p_box = [0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51, 4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38,
         54, 7, 23, 39, 55, 8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59, 12, 28, 44, 60, 13,
         29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63]
inv_p_box = [p_box.index(x) for x in range(64)]
rounds = 32


#variables
M = []
counter = 0
def add():
    global counter
    counter = counter + 1 # increment by 2

argument =  [ ]

# sbox layer taking hexadecimal string block
def sBoxLayer(state):
    sub_block = ""
    for i in range(len(state)):
        sub_block += str(hex(s_box[int(state[i], 16)])[2])
    return int(sub_block, 16)


def sBoxLayerInverse(state):
    sub_block = ""
    for i in range(len(state)):
        sub_block += str(hex(inv_sbox[int(state[i], 16)])[2])
    return int(sub_block, 16)


def sBox4Layer(state):
    sub_block = ""
    state = hex(int(state, 2))
    sub_block += str(hex(s_box[int(state, 16)])[2])
    sub_block = int(sub_block, 16)
    x = '{0:04b}'.format(sub_block)
    return x


# pbox layer taking binary string block
def pLayer(state):
    perm_block = state
    perm_list = [0 for x in range(64)]  # put 64 zeros in perm_list
    for i in range(len(state)):
        perm_list[p_box[i]] = state[i]
    perm_block = ''.join(perm_list)
    return int(perm_block, 2)


def pLayerInverse(state):
    perm_block = state
    perm_list = [0 for x in range(64)]
    for i in range(len(state)):
        perm_list[inv_p_box[i]] = state[i]
    perm_block = ''.join(perm_list)
    return int(perm_block, 2)


def xor2strings(string, count):
    y = '{0:05b}'.format(int(string, 2) ^ count)
    return y


def generateRoundKeys(key):
    K = []  # list of 128 bit decimal keys.
    string = bin(key)[2:].zfill(128)
    K.append(int(string[:64], 2))
    for i in range(0, 31):
        string = string[61:] + string[:61]
        string = sBox4Layer(string[:4]) + string[4:]
        string = string[:4] + sBox4Layer(string[4:8]) + string[8:]
        string = string[:61] + xor2strings(string[61:66], i + 1) + string[66:]

        # string = string[:60] +
        K.append(int(string[0:64], 2))
    return K


def addRoundKey(state, K64):
    x = state ^ K64
    #x = '{0:064b}'.format(x)
    return x


# Round Loop for Encryption
def encrypt(state, K):
    for i in range(rounds - 1):
        # XOR with Key
        state = addRoundKey(state, K[i])
        # SBox
        state = hex(state)[2:].zfill(16)  #
        state = sBoxLayer(state)
        # PBox
        state = bin(state)[2:].zfill(64)
        state = pLayer(state)
    state = addRoundKey(state, K[31])
    return state


def decrypt(state, K):
    for i in range(rounds - 1):
        #LFA on Last round

        if(i==0):
            Saver1 = str(bin(state))
            Saver2=list(Saver1[2:])
            n1 = (len(Saver2))


            
            K1 = str(bin(K[-i - 1]))
            K2=list(K1[2:])
            n2 = (len(K2))

            
            global inter0, inter1, inter2, inter3, inter4, inter5, inter6, inter7
            global k0, k1, k2, k3, k4, k5, k6, k7
            #MSB
            inter0 = int((Saver2)[n1-1],2)
            inter1 = int((Saver2)[n1-17],2)
            inter2 = int((Saver2)[n1-33],2)
            inter3 = int((Saver2)[n1-49],2)
            inter4 = int((Saver2)[n1-2],2)
            inter5 = int((Saver2)[n1-18],2)
            inter6 = int((Saver2)[n1-34],2)
            inter7 = int((Saver2)[n1-50],2)
            k0 = int((K2)[n2-1],2)
            k1 = int((K2)[n2-17],2)
            k2 = int((K2)[n2-33],2)
            k3 = int((K2)[n2-49],2)
            k4 = int((K2)[n2-2],2)
            k5 = int((K2)[n2-18],2)
            k6 = int((K2)[n2-34],2)
            k7 = int((K2)[n2-50],2)
            if( (inter0^inter4 == k0 ^ k4 ) and  (inter1^inter5 == k1 ^ k5 ) and  (inter2^inter6 == k2 ^ k6 ) and  (inter3^inter7== k3 ^ k7 ) ):
                  add()
        # Inverse PBox
        state = bin(state)[2:].zfill(64)
        state = pLayerInverse(state)

        # Inverse SBox
        state = hex(state)[2:].zfill(16)
        state = sBoxLayerInverse(state)
    state = addRoundKey(state, K[0])
    
    #print("--------------")
    return state




if __name__ == '__main__':
    for n in range (1000):
            for i in range(len(pp)):          # N=6   missfaults:85%
                         plain = pp[random.randint(0,len(pp)-1)]
                         key = 0x00000000000000000000000000000000
                         K = generateRoundKeys(key)
                         #cipher_text = encrypt(plain, K)
                         #print('0x' + '{0:016x}'.format(cipher_text))
                         plain_text = decrypt(plain, K)
                         #print('0x' + '{0:016x}'.format(plain_text))
            #cnt = collections.Counter(argument)         #involved bits of last round key(MSB) : (bit0^bit1),(bit16^bit17),(bit32^bit33),(bit48^bit49) ::0b1110
            #print(cnt)
            argument.append(counter)
            #
            #print(counter)
            counter = 0
    cnt = collections.Counter(argument)       
    print(cnt)
