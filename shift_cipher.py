def encrypt(text, key): 
    res = "" 
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            res += chr((ord(char)-65+key)%26+65) 
        else: 
            res += chr((ord(char)-97+key)%26+97) 
    return res
def decrypt(text, key):
    res = ""
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            res+=chr((ord(char)-65-key)%26+65)
        else:
            res+=chr((ord(char)-97-key)%26+97)
    return res
while True:
	choice = int(input("Enter 1 for encryption and 2 for decryption: "))
	if(choice==1):
	    text = input("Enter the text to be encrypted: ")
	    key = int(input("Enter the key (a number): "))
	    print ("Cipher-text: ", encrypt(text, key))
	    break
	elif(choice==2):
	    text = input("Enter the text to be decrypted: ")
	    key = int(input("Enter the key (a number): "))
	    print ("Plain-text: ", decrypt(text, key))
	    break
	else:
    		print("Invalid input!")
