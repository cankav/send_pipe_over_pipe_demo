from multiprocessing import Process
from multiprocessing import Pipe

def f1(child_end):
  while True:
    msg = child_end.recv()
    msg = msg.recv()
    print msg
    msg.send( 'ok' )

child, parent = Pipe()
Process( target=f1, args=(child,) )

c1, p1 = Pipe()
parent.send( c1 )
c1.send( 'slm' )

print p1.recv()
print 'done'
