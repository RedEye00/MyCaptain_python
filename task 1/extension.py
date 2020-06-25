s=input("Input the Filename: ")
a=0
ex=""
for i in range(len(s)):
    if s[i]==".":
        a=i
        break;
if s[i+1]=='c':
    if i+2!=len(s):
        ex="c++"
    else:
        ex="c"
elif s[i+1]=='p':
    ex="python"
else:
    ex="text"
print("The extension of the file is:'"+ex+"'")