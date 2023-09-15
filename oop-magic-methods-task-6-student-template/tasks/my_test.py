from task import *

os.chdir('home1')
print(os.getcwd())

with Cd('/etc1') as f:
    # open('new1.txt', 'w')
    pass

print(os.getcwd())
