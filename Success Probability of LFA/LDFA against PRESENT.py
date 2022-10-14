import numpy as np
import collections
import random
from collections import ChainMap 



pp= []  #faulty ciphertexts list >>find in implementation  file.rar
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
             #print(type(state))   
            global Saver
            Saver = bin(state)
            global inter0, inter1, inter2, inter3, inter4, inter5, inter6, inter7
            #print(Saver)
            inter0 = int(str(Saver)[2],2)
            inter1 = int(str(Saver)[3],2)
            inter2 = int(str(Saver)[18],2)
            inter3 = int(str(Saver)[19],2)
            inter4 = int(str(Saver)[34],2)
            inter5 = int(str(Saver)[35],2)
            inter6 = int(str(Saver)[50],2)
            inter7 = int(str(Saver)[51],2)

            for k0 in range(2):                 #b0,b1,b2,b3 bits info about last round key
                 for k1 in range(2):
                     for k2 in range(2):
                         for k3 in range(2):
                             for k4 in range(2):
                                 for k5 in range(2):
                                     for k6 in range(2):
                                         for k7 in range(2):

                                            if( (inter0^inter1 == k0 ^ k1 ) and (inter2^inter3 == k2 ^ k3 ) and (inter4^inter5 == k4 ^ k5 ) and (inter6^inter7 == k6 ^ k7 ) ):
                                                    b0 = (inter0^inter1)
                                                    b1 =  (inter2^inter3)
                                                    b2 = (inter4^inter5)
                                                    b3 = (inter6^inter7)
                                                    x = "0b"+str(b0)+str(b1)+str(b2)+str(b3)
                                                    argument.append(x)
                                                    x=0  
        # XOR with Key
        state = addRoundKey(state, K[-i - 1])                                                
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
            for i in range(len(pp)):          # N=?   number missedfaults
                         if (i<3): # selection % of the effective or ineffective faulty vectors
                                plain = pp[random.randint(0,i)]
                         else:
                                plain = pp[random.randint(i,len(pp)-1)]
                         key = 0x00000000000000000000000000000000  #specific vector
                         K = generateRoundKeys(key)
                         #cipher_text = encrypt(plain, K)
                         #print('0x' + '{0:016x}'.format(cipher_text))
                         plain_text = decrypt(plain, K)
                         #print('0x' + '{0:016x}'.format(plain_text))

            cnt = collections.Counter(argument)         #involved bits of last round key(MSB) : (bit0^bit1),(bit16^bit17),(bit32^bit33),(bit48^bit49) ::0b1110 >> for a specific vector
            print(cnt)
            argument = [ ]
            counter = 0
            
    
