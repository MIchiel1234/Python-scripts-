import os
from subprocess import *

#run child script 1
p = Popen([r'acountfraud.py', "ArcView"], shell=True, stdin=PIPE, stdout=PIPE)
output = p.communicate()


#run child script 2
p = Popen([r'locationfraud.py', "ArcView"], shell=True, stdin=PIPE, stdout=PIPE)
output = p.communicate()


#run child script 3
p = Popen([r'timefraud.py', "ArcView"], shell=True, stdin=PIPE, stdout=PIPE)
output = p.communicate()



#run child script 4
p = Popen([r'C:\calculatefraud.py', "IDLE"], shell=True, stdin=PIPE, stdout=PIPE)
output = p.communicate()

