#!/usr/bin/env python3

import math

N = 1000 # nodes on Memex
S = 2 # cpu cores per server
I = .1 # wild guess
T = 300 # wild guess
C = 3 # standard replication factor
IS = N * S * I
f = math.factorial

def nCr(n, r):
	f = math.factorial
	return f(n) // f(r) // f(n-r)

def stirlingF(n,k):
	if n==k or k==1:
		return 1

	SUM = 0
	for j in range(0, k+1):
		SUM += ((-1)**(k-j))*nCr(k,j)*(j**n)
	return (1/f(k))*SUM

def plocality(k, T):
	# do the math
	ISCk = nCr(IS, k)
	#print(ISCk)
	SUM = 0
	for i in range(k,T+1):
		TCi = nCr(T,i)
		#print(TCi)
		Sik = stirlingF(i,k)
		#print(Sik)
		g2 = f(k)*((N-IS)**(T-i))
		#print(g2)
		SUM += (TCi*Sik*g2) / (N**T)
		#print(SUM)
	#print(ISCk*SUM)
	return ISCk*SUM

for i in range(0,50):
	print (i, plocality(i, 50))