import hashlib
import os
import time
import random
import sys
import itertools
import sys
import requests
import time

WORDLIST = ""

def get_arg(arg_name):
    index = 0
    for i in sys.argv:
        if arg_name in i:
            return sys.argv[index + 1]
        index += 1

if(sys.argv[1].lower() == "help"):
  print("""
  PASSCRACKER

==============
  ARGUMENTS
==============
[-wordlist <file>]: Choose a wordlist to use
[-hash]: Give the hash to crack
[-rockyou]: Download rockyou.txt and use that
[-test <text>]: Give a password that will be translated to MD5 and use that as cracking hash.
  """)
  sys.exit(0)
characters = open("characters.txt", "r").read().splitlines()
if get_arg("-hash"):
    hash = get_arg("-hash")
elif get_arg("test"):
    hash = hashlib.md5(get_arg("test").encode()).hexdigest()
else:
    hash = input("[HASH] Give a hash >>> ")
if get_arg("-wordlist"):
    WORDLIST = get_arg("-wordlist")
elif get_arg("-rockyou"):
  #Download
  link = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
  file_name = "rockyou.txt"
  with open(file_name, "wb") as f:
      print("Downloading %s" % file_name)
      response = requests.get(link, stream=True)
      total_length = response.headers.get('content-length')

      if total_length is None: # no content length header
          f.write(response.content)
      else:
          dl = 0
          total_length = int(total_length)
          for data in response.iter_content(chunk_size=4096):
              dl += len(data)
              f.write(data)
              done = int(50 * dl / total_length)
              sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
              sys.stdout.flush()
  WORDLIST = "rockyou.txt"
chars = open("characters.txt", "r").read().replace("\n", "")
chars = "".join(chars)


def foo(l, index):
    yield from itertools.product(*([l] * index))


print("[READY] Ready to crack hash '" + hash + "'")
input()


index = 1
prosessing = True
strating_time = time.time()
while prosessing:
  if WORDLIST != "":
      for x in open(WORDLIST, "r", encoding="ISO-8859-1").readlines():
          passwd = x.replace("\n", "")
          sys.stdout.write("\r[TESTING]: %s" % (passwd) ) 
          sys.stdout.flush()
        #  time.sleep(0.001)
          if hashlib.md5(passwd.encode()).hexdigest() == hash:
              print("Password is: " + passwd)
              print("Time used: " + str(time.time() - strating_time) + " seconds")
              open("pass.txt", "w+").write("the password is: " + passwd)
              os.sys.exit(0)
  else:
      for x in foo(chars, index):
          passwd = "".join(x)
          sys.stdout.write("\r[TESTING]: %s" % (passwd) ) 
          sys.stdout.flush()
      #    time.sleep(0.001)
          if hashlib.md5(passwd.encode()).hexdigest() == hash:
              print("Password is: " + passwd)
              print("Time used: " + str(time.time() - strating_time) + " seconds")
              open("pass.txt", "w+").write("the password is: " + passwd)
              os.sys.exit(0)

  index += 1
