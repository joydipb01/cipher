import numpy as np

def encrypt(msg):
    msg = msg.replace(" ", "")
    K = make_key()
    len_check = len(msg) % 2 == 0
    if not len_check:
        msg += "0"
    M = create_matrix_of_integers_from_string(msg)
    msg_len = int(len(msg) / 2)
    cipher_txt = ""
    for i in range(msg_len):
        row_0 = M[0][i] * K[0][0] + M[1][i] * K[0][1]
        integer = int(row_0 % 26 + 65)
        cipher_txt += chr(integer)
        row_1 = M[0][i] * K[1][0] + M[1][i] * K[1][1]
        integer = int(row_1 % 26 + 65)
        cipher_txt += chr(integer)
    return cipher_txt

def decrypt(cipher_txt):
    multiplicative_inverse = -1
    K = make_key()
    determinant = K[0][0] * K[1][1] - K[0][1] * K[1][0]
    determinant = determinant % 26
    #multiplicative_inverse = find_multiplicative_inverse(determinant)
    for i in range(26):
        inverse = determinant * i
        if inverse % 26 == 1:
            multiplicative_inverse = i
            break
    K_inverse = K
    K_inverse[0][0], K_inverse[1][1] = K_inverse[1, 1], K_inverse[0, 0]
    K[0][1] *= -1
    K[1][0] *= -1
    for row in range(2):
        for column in range(2):
            K_inverse[row][column] *= multiplicative_inverse
            K_inverse[row][column] = K_inverse[row][column] % 26
    M = create_matrix_of_integers_from_string(cipher_txt)
    msg_len = int(len(cipher_txt) / 2)
    plain_txt = ""
    for i in range(msg_len):
        column_0 = M[0][i] * K_inverse[0][0] + M[1][i] * K_inverse[0][1]
        integer = int(column_0 % 26 + 65)
        plain_txt += chr(integer)
        column_1 = M[0][i] * K_inverse[1][0] + M[1][i] * K_inverse[1][1]
        integer = int(column_1 % 26 + 65)
        plain_txt += chr(integer)
    if plain_txt[-1] == "0":
        plain_txt = plain_txt[:-1]
    return plain_txt

def make_key():
    determinant = 0
    C = None
    while True:
        key = input("Enter the key(4-letter): ")
        C = create_matrix_of_integers_from_string(key)
        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        determinant = determinant % 26
        inverse_element = -1
        for i in range(26):
            inverse = determinant * i
            if inverse % 26 == 1:
                inverse_element = i
                break
        if inverse_element == -1:
            print("Determinant is not relatively prime to 26, uninvertible key")
        elif np.amax(C) > 26 and np.amin(C) < 0:
            print("Only a-z characters are accepted")
            print(np.amax(C), np.amin(C))
        else:
            break
    return C

def create_matrix_of_integers_from_string(string):
    integers = [chr_to_int(c) for c in string]
    length = len(integers)
    M = np.zeros((2, int(length / 2)), dtype=np.int32)
    iterator = 0
    for column in range(int(length / 2)):
        for row in range(2):
            M[row][column] = integers[iterator]
            iterator += 1
    return M

def chr_to_int(char):
    char = char.upper()
    integer = ord(char) - 65
    return integer

if __name__ == "__main__":
    while True:
        choice = int(input("Enter 1 for encryption and 2 for decryption: "))
        if(choice==1):
            msg = input("Enter the text to be encrypted: ")
            encrypted_msg = encrypt(msg)
            print(encrypted_msg)
            break
        elif(choice==2):
            encrypted_msg = input("Enter the text to be decrypted: ")
            decrypted_msg = decrypt(encrypted_msg)
            print(decrypted_msg)
            break
        else:
            print("Please enter 1/2")