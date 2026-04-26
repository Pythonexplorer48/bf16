format PE64 DLL
entry _
include 'INCLUDE/win64a.inc'
section '.text' code readable executable
_:mov eax,1
ret
c:cvtsd2ss xmm0,xmm0
movd eax,xmm0
shr eax,16
ret
r:shl ecx,16
movd xmm0,ecx
cvtss2sd xmm0,xmm0
ret
a:mov eax,ecx
and eax,32767
ret
n:mov eax,ecx
xor eax,32768
ret
x:mov eax,ecx
xor eax,edx
ret
macro V o{shl ecx,16
shl edx,16
movd xmm0,ecx
movd xmm1,edx
o xmm0,xmm1
movd eax,xmm0
shr eax,16
ret}
p:V addss
s:V subss
m:V mulss
v:V divss
f:shl ecx,16
shl edx,16
movd xmm0,ecx
movd xmm1,edx
divss xmm0,xmm1
roundss xmm0,xmm0,1
movd eax,xmm0
shr eax,16
ret
data export
export 'bf16_dev.dll',_,'_',c,'c',r,'r',a,'a',n,'n',x,'x',p,'p',s,'s',m,'m',v,'v',f,'f'
end data