enkripsi={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,' ':' ',',':','}

hasil={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',
24:'x',25:'y',26:'z'}
pembuka='SELAMAT DATANG'
print('~'.center(60,'~'))
print(pembuka.center(56))
print('~'.center(60,'~'))
print('masukkan kata untuk dienkripsi:')
print('#catatan:gunakan tanda_sebagai pengganti spasi')
kata=input()
word=kata.replace(' ','-')
print('jumlah pergeseran:')
x=int(input())
n=len(word)
result=''
print('HASIL ENKRIPSI:')
while n>0 :
	if word[-n] in enkripsi:
		akhir=enkripsi[word[-n]]+x
		while akhir>26:
			akhir=akhir-26
		result+=hasil[akhir]
	else:
		result+=word[-n]
	n=n-1
output=result.replace('-',' ')
print(output)