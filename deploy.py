import pexpect
import sys


user='admin'
name='10.121.10.93'
pw='\n'

child = pexpect.spawn('telnet ' + name)
child.logfile = sys.stdout
child.delaybeforesend = 2
child.expect('[lL]ogin.*')
child.sendline(user)
child.expect('[pP]assword.*')
child.sendline(pw)


child.expect('#')
child.sendline('tftp get 10.121.10.88 vr vr-m rtr03.cfg force')

child.expect('#')
child.sendline('load script rtr03.cfg')
child.expect(pexpect.EOF)
child.after

child.close()
