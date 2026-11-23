import json as J,os
from urllib.request import*
V=os.getenv('MAKEFUN_ENV_URL')
W=dict(zip('PNBRQK.',(100,320,330,500,900,20000,0)))
KN=[-21,-19,-12,-8,8,12,19,21]
DG=[-11,-9,9,11];ST=[-10,-1,1,10];DS=DG+ST
DT={'N':KN,'B':DG,'R':ST,'Q':DS,'K':DS}
CM=[15]*120;CM[91]=13;CM[98]=14;CM[21]=7;CM[28]=11
PT={p:[0]*120 for p in'PNBRQK'}
for i in range(120):
 f=i%10-1;r=9-i//10;v=7-max(abs(2*f-7),abs(2*r-7))
 for p,k,j in zip('PNBRQK',(2,9,7,3,2,-6),(8,0,0,0,0,0)):PT[p][i]=W[p]+k*v+j*r
IB=('         \n'*2+' rnbqkbnr\n'+' pppppppp\n'+' ........\n'*4+' PPPPPPPP\n'+' RNBQKBNR\n'+'         \n'*2)
IP=(IB,15,-1,95,25,0,6400);n=0;L=12e4;MA=2e4;tt={}
A=Exception
def atk(b,q):
 if 'p' in(b[q-9],b[q-11]):return 1
 if any(b[q+d]=='n' for d in KN):return 1
 for d in DS:
  t=q
  while b[t+d]=='.':t+=d
  u=b[t+d]
  if u=='k'and t==q or u=='q'or u in'br'and(d in DG)==(u=='b'):return 1
 return 0
def gen(P,q=0):
 b,c,e,kw,kb,s,mt=P;ms=[]
 for i,p in enumerate(b):
  if p=='P':
   for o in(-10,-20,-11,-9):
    t=i+o;ok=b[t]=='.' and(o==-10 or o==-20 and 80<i<89 and b[i-10]=='.') or o in(-11,-9) and(b[t].islower() or t==e)
    if ok and(not q or t<30 or b[t]!='.' or t==e):ms+=[i|t<<7|z<<14 for z in(5,4,3,2)] if t<30 else[i|t<<7]
  elif p in'NBRQK':
   for d in DT[p]:
    t=i
    while 1:
     t+=d;u=b[t]
     if u in' \n' or u.isupper():break
     if u!='.' or not q:ms.append(i|t<<7)
     if p in'NK' or u!='.':break
   if not q and p=='K' and not atk(b,i):
    for k,r,d,x in((1,98,2,97),(2,91,-2,92)):
     if c&k and b[i+d//2]==b[i+d]==b[x]=='.' and b[r]=='R' and not atk(b,i+d//2) and not atk(b,i+d):ms.append(i|(i+d)<<7)
 return ms
def mk(P,m):
 b,c,e,kw,kb,s,mt=P;f=m&127;t=(m>>7)&127;p=(m>>14)&7;pc=b[f];vc=b[t];u=t;cap=vc
 if pc=='P' and t==e and vc=='.':u=t+10;cap=b[u]
 np='NBRQ'[p-2] if p else pc;F=list(b);F[f]='.';F[t]=np;d=PT[np][t]-PT[pc][f]
 if u!=t:F[u]='.'
 if pc=='K' and abs(t-f)==2:
  v=1 if t>f else -1;q=98 if v>0 else 91;F[t-v]=F[q];F[q]='.';d+=PT['R'][t-v]-PT['R'][q]
 b2=''.join(F);kw2=t if pc=='K' else kw
 if atk(b2,kw2):return None
 if cap!='.':cu=cap.upper();d+=PT[cu][119-u];mt-=W[cu]*(cap in'nbrq')
 if p:mt+=W[np]-100
 c2=c&CM[f]&CM[t];c2&=12 if pc=='K' else 15;c2=(c2&8)>>3|(c2&4)>>1|(c2&2)<<1|(c2&1)<<3
 e2=129-f if pc=='P' and t==f-20 else -1
 return(b2[::-1].swapcase(),c2,e2,119-kb,119-kw2,-(s+d),mt)
def om(P,ms,t=0):
 b=P[0];ms.sort(key=lambda m:-W[b[(m>>7)&127].upper()])
 if t in ms:ms.remove(t);ms.insert(0,t)
 return ms
def qs(P,a,B):
 global n;n+=1
 if n>L:raise A
 b,c,e,kw,kb,s,mt=P;z=atk(b,kw)
 if not z:
  w=s+(6400-mt)*14*(PT['K'][kb]-PT['K'][kw])//38400
  if w>=B:return B
  if w>a:a=w
 ms=om(P,gen(P,1-z));l=0
 for m in ms:
  if not(P2:=mk(P,m)):continue
  l+=1;w=-qs(P2,-B,-a)
  if w>=B:return B
  if w>a:a=w
 if z and l==0:return -MA
 return a
def sr(P,z,a,B):
 global n;n+=1
 if n>L:raise A
 b,c,e,kw,kb,s,mt=P
 if z==0:return qs(P,a,B)
 t=tt.get(b,0);w=atk(b,kw);X=-MA;l=0;m2=0
 for m in om(P,gen(P),t):
  if not(P2:=mk(P,m)):continue
  l+=1;q=-sr(P2,z-1,-B,-a)
  if q>X:X=q;m2=m
  if q>a:a=q
  if a>=B:break
 if l==0:return -MA if w else 0
 if len(tt)>100000:tt.clear()
 tt[b]=m2
 return X
def rt(P):
 global n;ms=[m for m in gen(P) if mk(P,m)]
 if not ms:return None
 ms=om(P,ms);B=ms[0];z=1;n=0
 while 1:
  try:
   a=-MA;C=ms[0]
   for m in ms:
    q=-sr(mk(P,m),z-1,-MA,-a)
    if q>a:a=q;C=m
   B=C;ms.remove(B);ms.insert(0,B);z+=1
  except A:break
 return B
def uci(m):
 f=m&127;t=(m>>7)&127;p=(m>>14)&7;z=''.join(chr(96+x%10)+chr(58-x//10) for x in(f,t));return z+'nbrq'[p-2] if p else z
def fU(u):
 f,t=[4-int(u[i+1])*10+ord(u[i]) for i in(0,2)];p='nbrq'.index(u[4])+2 if len(u)==5 else 0;return f|t<<7|p<<14
def cv(m):return 119-(m&127)|(119-((m>>7)&127))<<7|m&7<<14
def post(q,y):
 z=Request(V+q,data=J.dumps(y).encode())
 with urlopen(z) as r:return J.load(r)
while(g:=post('/game',{}))['status']!='done':
 while g['status']=='your_move':
  P=IP
  for j,u in enumerate(g['moves']):m=fU(u);P=mk(P,cv(m) if j&1 else m)
  m=rt(P);z=uci(cv(m) if len(g['moves'])&1 else m) if m else ''
  g=post('/move',{'game':g['game'],'move':z})
