import hashlib
import os
import time
import random
import sys



def get_arg(arg_name):
  index = 0
  for i in sys.argv:
    if(arg_name in i):
      return sys.argv[index+1]
    index+=1


characters = open("characters.txt","r").read().splitlines()
if(get_arg("-hash")):
  hash = get_arg("-hash")
else:
  hash = input("[HASH] Give a hash >>> ")
print("[READY] Ready to crack hash '" + hash+"'")
input()
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