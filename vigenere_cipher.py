def generate_key(string, key): 
    key=key.upper()
    key = list(key) 
    if (len(string) == len(key)): 
        return(key) 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i%len(key)]) 
    return("".join(key)) 
def encryption(string, key): 
    cipher_text = []
    pl_text=string.upper()
    for i in range(len(pl_text)):
        x = (ord(pl_text[i])+ord(key[i]))%26
        x += ord('A') 
        cipher_text.append(chr(x))
        if i!=0:
            cipher_text[i]=cipher_text[i].lower()
    return ("" . join(cipher_text))
def decryption(cipher_text, key): 
    pl_text = [] 
	  cipher_text=cipher_text.upper()
	  for i in range(len(cipher_text)):
		    x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
		    x += ord('A') 
		    pl_text.append(chr(x))
		    if i!=0:
			      pl_text[i]=pl_text[i].lower()
    return("".join(pl_text))
while True:
    choice=int(input("Enter 1 for encryption and 2 for decryption: "))
	  if(choice==1):
		    string = input("Enter the word to be encrypted: ")
		    key = input("Enter your key: ")
		    generated_key = generate_key(string, key) 
		    cipher_text = encryption(string,generated_key) 
		    print("Cipher-Text:", cipher_text)
		    break 
    elif(choice==2):
		    string = input("Enter the word to be decrypted: ")
		    key = input("Enter your key: ")
		    generated_key = generate_key(string, key)
		    plain_text = decryption(string, generated_key)
		    print("Plain-text:", plain_text)
		    break
    else:
        print("Invalid entry!")
