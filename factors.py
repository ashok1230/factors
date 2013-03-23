class factor:
    def __init__(self,number):
	self.i=number
	i=2
	while self.i>=i:
	     if self.i%i==0:
		print i,
		self.i/=i
		i=2
		continue
	     i+=1

factor(100)
