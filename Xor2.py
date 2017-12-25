# -*- coding: utf-8 -*-
from sage.all import *
from os import urandom

X = GF(2).polynomial_ring().gen()

def ntopoly(npoly):
  return sum(c*X**e for e, c in enumerate(Integer(npoly).bits()))

def polyton(poly):
  return sum(int(poly[i])*(1 << i) for i in xrange(poly.degree() + 1))

def p(n):
  return polyton((ntopoly(n)**2)%P)

def str2num(s):
  return int(s.encode('hex'), 16)

P = 0x10000000000000000000000000000000000000000000000000000000000000425L
P = ntopoly(P)

fake_secret1 = "I_am_not_a_secret_so_you_know_me"
fake_secret2 = "feeddeadbeefcafefeeddeadbeefcafe"

with open('ciphertext','r') as f:
  c = f.readlines()
ctxt1 = int(c[0],16)
ctxt2 = int(c[1],16)
ctxt3 = int(c[2],16)
key2 = ctxt2 ^ str2num(fake_secret1)
key3 = ctxt3 ^ str2num(fake_secret2)

ps = key3 ^ p(key2) # p(seed)
pk = key2 ^ ps # p(key1)
m = p(ctxt1) ^ pk # p(secret)

for x in range(255):
  m = p(m)

print 'flag{%s}' % hex(m)[2:-1].decode('hex')
