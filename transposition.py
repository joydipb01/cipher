import math 

def encrypt(msg): 
    cipher = "" 
    k_idx = 0
    msg_len = float(len(msg)) 
    msg_lst = list(msg) 
    key_lst = sorted(list(key)) 
    col = len(key) 
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len) 
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col]  
              for i in range(0, len(msg_lst), col)]
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_idx]) 
        cipher += ''.join([row[curr_idx]  
                          for row in matrix]) 
        k_idx += 1
    return cipher
def decrypt(cipher_txt): 
    msg = "" 
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher_txt)) 
    msg_lst = list(cipher_txt) 
    col = len(key) 
    row = int(math.ceil(msg_len / col)) 
    key_lst = sorted(list(key))
    dec_cipher = [] 
    for _ in range(row): 
        dec_cipher += [[None] * col] 
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
        for j in range(row): 
            dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
            msg_indx += 1
        k_indx += 1
    try: 
        msg = ''.join(sum(dec_cipher, [])) 
    except TypeError: 
        raise TypeError("This program cannot", 
                        "handle repeating words.") 
    null_count = msg.count('_') 
    if null_count > 0: 
        return msg[: -null_count] 
    return msg

while True:
    choice = int(input("Enter 1 for encryption and 2 for decryption: "))
    if(choice==1):
        msg = input("Enter the message to be encrypted: ")
        key = input("Enter the key: ")
        cipher = encrypt(msg)
        print("Encrypted Message: {}". 
               format(cipher))
        break
    elif(choice==2):
        cipher_txt=input("Enter the message to be decrypted: ")
        key=input("Enter the key: ")
        msg = decrypt(cipher_txt)
        print("Decrypted Message: {}".format(msg))
        break
    else:
        print("Enter a valid entry")