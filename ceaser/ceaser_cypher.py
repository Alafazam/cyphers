import sys


# arg 1 is key
# arg 2 is encrpt or decrypt
key = 0

def main():
	key = int(sys.argv[1])
	print 'key is '+ str(key)
	operation  = sys.argv[2]
	print 'operation is ' + operation + 'ion'
	if operation == 'encrypt':
		encrypt(key)
	elif operation == 'decrypt':
		decrypt(key)
	# print sys.argv



def encrypt(key):
	f = open('ceaser_input.txt','r')
	text = f.read()
	length = len(text)
	x=0
	ans =''
	while x<length:
		alp = text[x]
		t = ord(alp)
		if t>64 and t<91:
			t = ((t - 65 + key)%26)+65
		elif t>96 and t<123:
			t = ((t - 97 + key)%26)+97
		ans= ans + str(unichr(t))
		x = x+1
		# print str(unichr(t))
	d = open('ceaser_output.txt','w')
	d.write(ans+'\n')
	d.close()
	f.close()
	print text + " got encrypted to " + ans	
	
def decrypt(key):
	f = open('ceaser_output.txt','r')
	text = f.read()
	length = len(text)
	x=0
	ans =''
	while x<length:
		alp = text[x]
		t = ord(alp)
		if t>64 and t<91:
			t = ((t - 65 - key)%26)+65
		elif t>96 and t<123:
			t = ((t - 97 - key)%26)+97
		ans= ans + str(unichr(t))
		x = x+1
		# print str(unichr(t))
	d = open('ceaser_input.txt','w')
	d.write(ans+'\n')
	d.close()
	f.close()
	print text + " got decrypted from " + ans	



if __name__ == '__main__':
    main()