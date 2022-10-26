import hashlib
import os
import time
import random

print(hashlib.md5("Bertta".encode()).hexdigest())
input()


characters = open("characters.txt","r").read().splitlines()
hash="71319e2cba8ef95cac7647527a3291f2"
import itertools
chars = open("characters.txt","r").read().replace("\n","")
chars = ''.join(random.sample(chars,len(chars)))
def foo(l,index):
     yield from itertools.product(*([l] * index))

index = 1
prosessing = True
strating_time = time.time()
while prosessing:
  for x in foo(chars,index):
        passwd=''.join(x)
        print(passwd)
        if(hashlib.md5(passwd.encode()).hexdigest() == hash):
          print("Password is: "+passwd)
          print("Time used: "+str(time.time() - strating_time)+" seconds")
          open("pass.txt","w+").write("the password is: "+passwd)
          os.sys.exit(0)
          
  index += 1