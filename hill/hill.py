# import utils
import sys
def gcd(x,y):
    while y:
        (x, y) = (y, x%y)
    return abs(x)
def invertible(matrix):
    determinant = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    return gcd(determinant, 26) == 1
def inverse_matrix(matrix):
    if not invertible(matrix):
        return "Non invertible matrix"
    result = [i[:] for i in matrix]
    result[0][0] = matrix[1][1]
    result[1][1] = matrix[0][0]
    result[1][0] = (-matrix[1][0]) % 26
    result[0][1] = (-matrix[0][1]) % 26
    return result
def main():
	operation  = sys.argv[1]	
	print 'operation is ' + operation + 'ion'
	kt = open ( 'hill_key.txt' , 'r')
	key = [ map(int,line.split(' ')) for line in kt ]
	if operation == 'encrypt':
		f = open('hill_input.txt','r')
		text = f.read()
		f.close()
		ans = encrypt(text,key)
		w = open('hill_output.txt','w')
		w.write(ans)
		w.close()
		print "plain text was "+text
		print "cypher text is "+ans
	elif operation == 'decrypt':
		f = open('hill_input.txt','r')
		text = f.read()
		f.close()
		ans = decrypt(text,key)
		print ans
		w = open('hill_output.txt','w')
		w.write(ans)
		w.close()
		print "cypher text was "+text
		print "plain text is "+ans

	# print sys.argv
def encrypt(message, matrix, encryption=True):
    message = message.lower()

    if len(message) % 2 != 0:
        message = message + 'x'


    if not invertible(matrix):
        return "Non invertible matrix"

    couple = [list(message[i*2:(i*2)+2]) for i in range(0, len(message)/2)]
    result = [i[:] for i in couple]    
    if not encryption:
        matrix = inverse_matrix(matrix)
    for i, c in enumerate(couple):
        if c[0].isalpha() and c[1].isalpha():
            result[i][0] = chr(((ord(c[0])-97) * matrix[0][0] + (ord(c[1])-97) * matrix[0][1]) % 26 + 97)
            result[i][1] = chr(((ord(c[0])-97) * matrix[1][0] + (ord(c[1])-97) * matrix[1][1]) % 26 + 97)
    return "".join(["".join(i) for i in result])
def decrypt (cypher, matrix):
    return encrypt(cypher, matrix, False)
if __name__ == '__main__':
	main()
    # Point of entry in execution mode
    # print encrypt("Vivement les vacances !", [[11, 3], [8, 7]])
    # print decrypt(encrypt("Vivement les vacances !", [[11, 3], [8, 7]]), [[11, 3], [8, 7]])
