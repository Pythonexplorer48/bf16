from cffi import FFI
import os
i=FFI()
i.cdef("uint16_t c(double);double r(uint16_t);uint16_t a(uint16_t);uint16_t n(uint16_t);uint16_t x(uint16_t,uint16_t);uint16_t p(uint16_t,uint16_t);uint16_t s(uint16_t,uint16_t);uint16_t m(uint16_t,uint16_t);uint16_t v(uint16_t,uint16_t);uint16_t f(uint16_t,uint16_t);")
l=i.dlopen(os.path.join(os.path.dirname(__file__),"bf16.dll"))
class bfloat16:
 __slots__='d',
 def __init__(s,v):s.d=l.c(float(v))
 def __abs__(s):return t(l.a(s.d))
 def __neg__(s):return t(l.n(s.d))
 def __add__(s,o):return t(l.p(s.d,g(o)))
 def __sub__(s,o):return t(l.s(s.d,g(o)))
 def __mul__(s,o):return t(l.m(s.d,g(o)))
 def __truediv__(s,o):return t(l.v(s.d,g(o)))
 def __xor__(s,o):return t(l.x(s.d,g(o)))
 def __floordiv__(s,o):return t(l.f(s.d,g(o)))
 def __lt__(s,o):return float(s)<float(o)
 def __le__(s,o):return float(s)<=float(o)
 def __gt__(s,o):return float(s)>float(o)
 def __ge__(s,o):return float(s)>=float(o)
 def __eq__(s,o):return float(s)==float(o)
 def __ne__(s,o):return float(s)!=float(o)
 def is_integer(s):return float(s).is_integer()
 def conjugate(s):return s
 def as_integer_ratio(s,*a):return float(s).as_integer_ratio()
 def hex(s):return float(s).hex()
 @classmethod
 def fromhex(c,h):return bfloat16(float.fromhex(h))
 def __float__(s):return l.r(s.d)
 def __repr__(s):return str(float(s))
 __str__=__repr__
def g(o):return o.d if hasattr(o,'d')else l.c(float(o))
def t(v):
 n=bfloat16.__new__(bfloat16)
 n.d=v
 return n