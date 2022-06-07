# Vernom Cypher code
myPad = (6, 2, 10, 4, 3, 1, 7)

#Plain Text Message
myMessage = 'Everton1878!'

#Removing the uppercase
myMessage = myMessage.lower()

#Removing the spaces & special characters
myMessage =''.join(c for c in myMessage if c.isalpha())

#Declairing Variables - X is for pad position - enc is for encrypted text
x=-1
enc=""
encryptedMessage=""
#Looping through the message to encrypt
for i in myMessage:
	x=x+1 #adding 1 each itteration, starts at zero
	enc=ord(i)+myPad[x] # math operator adding the sum of message ord and pad position
	#print (chr(enc)) #taking the numbers and using chr to print the corrisponding letters
	encryptedMessage=encryptedMessage+(chr(enc))
	
print ('Everton1878!=',encryptedMessage)



y=-1
dec=""
decryptedMessage=""
#Looping through the message to encrypt
for i in encryptedMessage:
	y=y+1 #adding 1 each itteration, starts at zero
	dec=ord(i)-myPad[y] # math operator adding the sum of message ord and pad position
	#print (chr(enc)) #taking the numbers and using chr to print the corrisponding letters
	decryptedMessage=decryptedMessage+(chr(dec))
	
print ('Evertonfc1878!',decryptedMessage)
