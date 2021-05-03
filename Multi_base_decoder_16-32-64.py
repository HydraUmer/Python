import base64

#file path
f = open("encodedflag.txt","r") 
flag = f.read()

#print(flag)

res = ''

#base 16 
for i in range(0, 5):      
    res = base64.b16decode(flag)
    flag = res

#base 32
for i in range(0, 5):
    res = base64.b32decode(flag)
    flag = res

#base 64
for i in range(0, 5):
    res = base64.b64decode(flag)
    flag = res

print(res)
f.close()
