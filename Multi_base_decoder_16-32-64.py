import base64

#files
f = open("encodedflag.txt","r")
flag = f.read()

#print(flag)

res = ''

for i in range(0, 5):
    res = base64.b16decode(flag)
    flag = res

for i in range(0, 5):
    res = base64.b32decode(flag)
    flag = res

for i in range(0, 5):
    res = base64.b64decode(flag)
    flag = res

print(res)
f.close()