import sys,random,json

def main():
	operation  = sys.argv[1]	
	print 'operation is ' + operation + 'ion'
	if operation == 'encrypt':
		key = genrate_key()
		f = open('mono_key.txt','w')
		dd =''
		for x in key:
			dd +=str(unichr(x+97))
		f.write(dd)
		f.close()
		encrypt(key)
	elif operation == 'decrypt':
		f = open('mono_key.txt','r')
		key = f.read()
		decrypt(key)
	# print sys.argv



def encrypt(key):
	f = open('mono_input.txt','r')
	text = f.read()
	f.close()
	ans =''
	for ch in text:
		a = ord(ch)
		if a > 64 and a < 91:
			ans+= str(chr(key[a-65]+65))
		elif a > 96 and a < 123:
			ans +=chr(key[a-97]+97)
		else:
			ans +=ch	
	f = open('mono_output.txt','w')
	f.write(ans)
	f.close()
	print 'done'


def decrypt(key):
	revkey = [ i for i in range(26)]
	x=0
	while x<26:
		revkey[ord(key[x])-97] = x
		x = x + 1 
	f = open('mono_output.txt','r')
	text = f.read()
	f.close()
	ans =''
	for ch in text:
		a = ord(ch)
		if a > 64 and a < 91:
			ans+= str(unichr(revkey[a-65]+65))
		elif a > 96 and a < 123:
			ans+= str(unichr(revkey[a-97]+97))
		else:
			ans +=ch	

	f = open('mono_output_de.txt','w')
	f.write(ans)
	f.close()
	print 'done'




def genrate_key():
	myList=[ i for i in range(26)]
	random.shuffle(myList)
	# for x in myList:
		# print str(unichr(x+97))
	return myList





if __name__ == '__main__':
	main()