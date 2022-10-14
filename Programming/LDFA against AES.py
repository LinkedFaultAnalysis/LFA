import numpy as np
import collections
import random
from collections import ChainMap 

#you can Import the data file with  the following commands:
#with open('data file address', 'r') as fin
#because our data file involves more than 20K faulty vectors, we didn't call that directly here(also recommend for you).

faultylist =[ ]  #select from data Zip file if you want effective or ineffective fault


#AES source code
#reference for source code : https://github.com/Ysjshine/encryption-AES 
sbox = np.array([
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
     ],dtype=np.int64)

#inverse Sbox
inv_sbox = np.array([
    [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
    [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
    [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
    [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
    [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
    [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
    [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
    [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
    [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
    [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
    [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
    [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
    [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
    [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
    [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]
],dtype=np.int64)

#mix columns matrix
mix_mat = np.array([
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
],dtype=np.int64)

#inverse columns matrix
inv_mix_mat = np.array([
    [0x0e, 0x0b, 0x0d, 0x09],
    [0x09, 0x0e, 0x0b, 0x0d],
    [0x0d, 0x09, 0x0e, 0x0b],
    [0x0b, 0x0d, 0x09, 0x0e]
],dtype=np.int64)

#GF(2^8) multiply operation need
GF_bit = np.array([0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80],dtype=np.int64)

#round key constant
round_constant = np.array([0x01000000,0x02000000,0x04000000,0x08000000,0x10000000,
                           0x20000000,0x40000000,0x80000000,0x1b000000,0x36000000],dtype=np.int64)



M = []
counter = 0
argument =  [ ]
class AES:
    def __init__(self,src,key):
        '''
        constructor
        :param src:plain text or cypher text
        :param key:key
        '''
        self.__src = src
        self.__key = key

    def __index_sbox(self, num,type):
        '''
        search in sbox or inv_sbox
        :param num:input byte
        :param type:decode or encode
        :return:output byte
        '''
        temp = int(num)
        #get left 4 bits of input byte
        row = (temp & 0xf0) >> 4
        #get right 4 bits of input byte
        col = temp & 0x0f
        if type == 0:return sbox[row][col]
        else:return inv_sbox[row][col]

    def __sub_bytes(self, src,type):
        '''
        :param src:input data
        :param type:decode or encode
        :return:output
        '''
        ans = np.zeros((4,4),dtype=np.int64)
        for i in range(4):
            for j in range(4):
                ans[i][j] = self.__index_sbox(src[i][j],type)


        
        return ans

    def __shift_row(self, src,type):
        '''
        shift rows:
        1.forward
        the first row does nothing,the second moves a byte to left,
        the third moves 2 bytes and the last moves 3 bytes
        2. inverse:
        the first row does nothing,the second moves a byte to right,
        the third moves 2 bytes and the last moves 3 bytes
        :param src: input
        :param type: decode or encode
        :return:output
        '''
        ans = np.zeros((4,4),dtype=np.int64)
        # for left_num in range(4):
        for i in range(4):
            for j in range(4):
                if type == 0:ans[i][(j-i+4)%4] = src[i][j]
                else:ans[i][(j+i)%4] = src[i][j]
        return ans

    def __GF28mul(self, op1, op2):
        '''
        bytes' multiplicative operation in GF(2^8) field
        :param op1:the first operand
        :param op2:the second operand
        :return:answer
        '''
        ans = []; var = op2; total = 0
        for i in range(8):
            x = (var&GF_bit[7])
            ans.append(var)
            if x == 0:var = (var << 1)&0xff
            elif x == 0x80:var = ((var<<1)&0xff)^0x1b

        for i in range(8):
            if op1&GF_bit[i] == 1<<i:
                total = total^ans[i]
        return total

    def __mix_column(self, src,type):
        '''
        mix column operation
        :param src: input
        :param type: decode or encode
        :return: output
        '''
        ans = np.zeros((4,4),dtype=np.int64)
        for i in range(4):
            for k in range(4):
                sum = 0
                for j in range(4):
                    if type == 0:sum =sum^self.__GF28mul(mix_mat[i][j], src[j][k])
                    else:sum = sum ^ self.__GF28mul(inv_mix_mat[i][j], src[j][k])
                ans[i][k] += sum
        return ans

    def __calculate_ti(self, w, i):
        '''
        calculate the middle variables ti
        :param w: w[i-1]
        :param i: the sequence number
        :return: output
        '''
        #make sure that w is 32-bits
        w1 = w&0xffffffff
        #move a byte to left then add the  byte to the tail
        p = ((w1&0xff000000)>>24)^((w1<<8)&0xffffffff)
        #sbox
        x1 = self.__index_sbox(p & 0x000000ff,0)
        x2 = self.__index_sbox((p & 0x0000ff00) >> 8,0)
        x3 = self.__index_sbox((p & 0x00ff0000) >> 16,0)
        x4 = self.__index_sbox((p & 0xff000000) >> 24,0)

        ans = ( x1 ^ (x2 << 8) ^ (x3 << 16 )^( x4 <<24))^round_constant[i]
        # print("ti",hex(ans))
        return ans

    def __generate_init(self, i):
        '''
        get w0,w1,w2,w3
        '''
        key = self.__key
        return (key[4*i]<<24)^(key[4*i+1]<<16)^(key[4*i+2]<<8)^(key[4*i+3])

    def __expand_key(self):
        '''
        expand key and get round keys
        :return:round keys
        '''
        round_key = []; w = np.zeros(100,dtype=np.int64)
        for i in range(4):
            w[i] = self.__generate_init(i)

        for i in range(4,44):
            if i % 4 == 0:
                w[i] = self.__calculate_ti(w[i - 1], int(i / 4) - 1) ^ w[i - 4]
            else:
                w[i] = w[i-1]^w[i-4]

        #divide w[i] into 4 bytes
        for i in range(44):
            if i % 4 != 0:continue
            key = []; bit = 0xff000000
            for j in range(4):
                for k in range(4):
                    key.append((w[i+j]&(bit>>(k*8)))>>(24-k*8))
            round_key.append(key)
        return round_key

    def __add_round_key(self, round_key_i, src):
        '''
        :param round_key_i: i_th round_key
        :param src: input
        :return: output
        '''
        round_key = np.array(round_key_i).reshape((4,4)).T
        ans = np.zeros((4,4),dtype=np.int64)
        for i in range(4):
            for j in range(4):
                ans[i][j] = src[i][j]^round_key[i][j]

        return ans

    #encode
    def encode(self):
        round_key = self.__expand_key()
        ans = self.__add_round_key(round_key[0], self.__src)
        for i in range(1,10):
            sub_ans = self.__sub_bytes(ans,0)
            shift_ans = self.__shift_row(sub_ans,0)
            mix_ans = self.__mix_column(shift_ans,0)
            ans = self.__add_round_key(round_key[i], mix_ans)
        sub_ans = self.__sub_bytes(ans,0)
        shift_ans = self.__shift_row(sub_ans,0)
        result = self.__add_round_key(round_key[10], shift_ans)
        return result

    #decode
    def decode(self):
        round_key = self.__expand_key()
        ans = self.__add_round_key(round_key[10],self.__src)
        for i in range(9,0,-1):
            inv_shift_ans = self.__shift_row(ans,1)
            inv_sub_ans = self.__sub_bytes(inv_shift_ans,1)
            if (i==9):
                     C12 = hex(self.__src[0][3])    # byte 12 Ciphertext
                     B12C = ((int((C12),16)))
                     C13 = hex(self.__src[1][3])    # byte 13 Ciphertext
                     B13C = ((int((C13),16)))
                     
                     for k12 in range(0x100):
                         for k13 in range(0x100):
                            if(k12!=k13):
                              if ( B12C ^ B13C == k12 ^ k13):
                                 global counter
                                 counter  = counter  +1
                                 x = hex(B12C ^ B13C)
                                 argument.append(x)
                                 x=0
            add_ans = self.__add_round_key(round_key[i],inv_sub_ans)
            ans = self.__mix_column(add_ans,1)
        inv_shift_ans = self.__shift_row(ans,1)
        inv_sub_ans = self.__sub_bytes(inv_shift_ans,1)
        result = self.__add_round_key(round_key[0],inv_sub_ans)

        return result

    def debug(self,ans):
        for i in range(4):
            for j in range(4):
                print(hex(int(ans[i][j])), end=" ")
                if j == 3:print("")
        print("\n")

if __name__ == '__main__':

 for o in range(1000):
     for i in range(30): #N : number of faulty vectors
            if (i<25): # selection % of the effective or ineffective faulty vectors
                src = faultylist[random.randint(0,15000)]
            else:
                src = faultylist[random.randint(30000,45658)]
            key = np.array([0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c],dtype=np.int64)
            aes = AES(src.T,key)
            ans2 = aes.decode()
     cnt = collections.Counter(argument)  #key is fixed, and the correct key byte is 0xD5 - We evaluated the key equation for finding the success probability in different N faulty cipher
     print(c)
     argument = [ ]
     counter = 0
#Each time, We decrypt the AES and evaluate the key guessing equation

