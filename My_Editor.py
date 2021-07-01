import time


def rand(intMax,intMin=0):
	random=int(time.time()*1000)
	random %= intMax
	ct=time.time()
	st ="".join(str(ct).split("."))
	l=[]
	ds=int(st)
	while len(str(ds))>1:
		ds=sum(int(i)for i in str(ds))
	final=ds+random*ds
	while intMin+final>intMax:
		final//=2
	return final

x=int(input())
print(rand(x))