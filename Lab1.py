A='abc'
B='xyz'
C='123'

def assign_string(alphabet):
    while True:
        s=input(f"Input a sring of the alphabet {alphabet}: ")
        if all(character in alphabet for character in s):
            return s
        else:
            print("The string is invalid, try again")
            
s1=assign_string(A)
s2=assign_string(B)
s3=assign_string(C)            

def concatenate(s1, s2):
    return s1 + s2
    
    
def reverse(s):
   return s[::-1]   

def replace(s, sub, new_sub):
    index = s.find(sub)
    if index != -1:
        return s[:index] + new_sub + s[index+len(sub):]
    else:
        return s

def length(s):
   return len(s)       
   
concatenateResult=concatenate(s1,s2)
print(concatenateResult)

reverseResult=reverse(A)
print(reverseResult)

replaceResult=replace(s1,A,B)
print(replaceResult)

lengthResult=length(A)
print(lengthResult)

l1 = '0123456789'
l2 = 'abcdefghijk'
l3 = 'x1y1x2y2x3y3x4y4x5y5'

def assign_string(alphabet):
    while True:
        s=input(f"Input a sring of the alphabet {alphabet}: ")
        if all(character in alphabet for character in s):
            return s
        else:
            print("The string is invalid, try again")
            
s4=assign_string(l1)
s5=assign_string(l2)
s6=assign_string(l3)   

def concat(s4, s5):
    return s4 + s5
    
def repeat(s, n):
    return s * n

def reverse(s):
    return s[::-1]
    
def extract(s, i, j):
    return s[i-1:j]

def replace(s, sub, new_sub):
    index = s.find(sub)
    if index != -1:
        return s[:index] + new_sub + s[index+len(sub):]
    else:
        return s

repeatResult=repeat(s4,4)

extractResult=extract(s6,3,10)
