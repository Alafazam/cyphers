# this function decrypts a ceaser cipher using brute force



def main():
	f = open('ceaser_output.txt','r')
	text = f.read()
	f.close()
	f_ans = ''
	for x in range(0,25):
		ans = decrypt(x,text)
		print ans
		f_ans += ans			
	d = open('ceaser_brute_result.txt','w')
	d.write(f_ans)
	d.close()


def decrypt(key,text):
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
	return ans
	# print text + " got decrypted from " + ans	



if __name__ == '__main__':
    main()