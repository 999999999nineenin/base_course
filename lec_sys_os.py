import sys, os

a=1
print(os.getcwd())

#os.system('echo hi!')
i=2
#while a!=0:
    #i*=999
    #print(i)
#os.system('python lec_sys_os.py')

print('Python version is:', sys.version)
print(sys.path)
print(sys.platform)

print(dir(sys))