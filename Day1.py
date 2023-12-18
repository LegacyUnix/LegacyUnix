def firstdigit(s):
  i=0
  l=len(s)
  while i < l:
   c=s[i]
   if str.isdigit(c) :
      return c
   i=i+1
  print ("no digits in " + s)

def lastdigit(s):
  i=-1
  l=len(s) * -1
  while i >= l:
   c=s[i]
   if str.isdigit(c) :
      return c
   i=i-1
  print ("no digits in " + s)

def firstdigitq2(s):
  i=0
  l=len(s)
  while i < l:
   c=s[i]
   if str.isdigit(c) :
      return c
   q = speltDigit(s[i:])
   if (q >= 0):
       return q
   i=i+1
  print ("no digits in " + s)

def lastdigitq2(s):
  i=-1
  l=len(s) * -1
  while i >= l:
   c=s[i]
   if str.isdigit(c) :
      return c
   q = speltDigit(s[i:])
   if (q >= 0):
       return q
   i=i-1
  print ("no digits in " + s)

def speltDigit(s):
 sd = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
 d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 sd3 = ["one", "two", "six"]
 sd4 = ["zero", "four", "five", "nine"]
 sd5 = ["three", "seven", "eight"]
 s3 = s[:3]
 s4 = s[:4]
 s5 = s[:5]
 if s3 in sd3: 
  i = sd.index(s3)
  print ("3: ", i, d[i])
  return d[i]
 if s4 in sd4:
  i = sd.index(s4)
  print ("4: ", i, d[i])
  return d[i]
 if s5 in sd5:
  i = sd.index(s5)
  print ("5: ", i, d[i])
  return d[i]
 return -1

 
 
 
def q1(filename):
 answer=0
 with(open(filename, encoding="utf-8")) as f:
  for line in f:
   #print (" f: " + firstdigit(line) + " l: " + lastdigit (line))
   calib= int(firstdigit(line) + lastdigit(line))
   #print(calib)
   answer = answer + calib
 print ("answer is ",  answer)

def q2(filename):
 answer=0
 with(open(filename, encoding="utf-8")) as f:
  for line in f:
   #print (" f: " + firstdigit(line) + " l: " + lastdigit (line))
   calib= int(str(firstdigitq2(line)) + str(lastdigitq2(line)))
   print(calib)
   answer = answer + calib
 print ("answer is ",  answer)
