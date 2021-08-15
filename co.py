import sys

A=["add","sub",'mul','xor','or','and']
B=['mov','rs','ls']#all type b commands have $ in them
C=['movr','div','not','cmp']
D=['ld','st']
E=['jmp','jlt','jgt']
F=['hlt']
oc={'add':'00000','sub':'00001','mov':'00010','movr':'00011','ld':'00100','st':'00101','mul':'00110','div':'00111','rs':'01000','ls':'01001','xor':'01010','or':'01011','and':'01100','not':'01101','cmp':'01110','jmp':'01111','jlt':'10000','jgt':'10001','hlt':"10011"}
addrs={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110','FLAGS':'111'}
type=''
data=[]
final_output=[]
def regOf(a):
    if(a in addrs and a.lower() != "flags"):
        return(str(addrs[a.lower()]))
    else:
        return 0
    
def convertBinary(a):
    bnr = bin(a).replace('0b','')
    x = bnr[::-1] 
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return(bnr)
def print_a(operation, para_a, para_b, para_c, line_no):
    res = oc[operation] + "00" #add r3 r2 r1
    for i in para_a, para_b, para_c:
        t = regOf(i)
        res += t
    final_output.append(res)
def print_b(operation, para_a, imm, line_no):
    res = oc[operation]
    t = regOf(para_a, line_no)
    res += t
    res += convertBinary(imm)
    final_output.append(res)
def print_c(operation, para_a, para_b, line_no):
    res = oc[operation] + "00000"
    for i in para_a, para_b:
        t= regOf(i, line_no)
        res += t
    final_output.append(res)
def print_d(operation,para_a,m,line_no):
    res=oc[operation]
    t=regOf(para_a,line_no)
    if t:
        res+=t
    else:
        return
    res+=m
    final_output.append(res)
def print_e(operation,m,line_no):
    res=oc[operation]+"000"
    res+=m
    final_output.append(res)

def print_f(operation,line_no):
    res =oc[operation]+"00000000000"    
    final_output.append(res)

file = sys.stdin.read()
for i in file:
    k=i.split()
    if len(k)==0:
        continue                        #ignores empty lines
    data.append(k)

#print(data)
lno=0
for i in (data):
    a=i[0]
    if(a not in oc.keys()):
        print("error: invalid instruction")
        break

            
    if "hlt" not in data[-1] or "hlt" not in data:
        print('error: hlt not found')
        break
    else:
        pass
    if a in A:
         print_a(a, i[1], i[2], i[3],lno)
    elif "$" in i or a in B:
        print_b(a,i[1],int(i[2][1:]),lno)
    elif a in C:
        print_c(a,i[1],i[2],lno)
    elif a in D:
        print_d(a,i[1],i[2],lno)
    elif a in E:
        print_e(a,i[1],lno)
    elif a in F:
        print_f(a,lno)
    else:
        print("error:invalid instruction")
    lno+=1
else:
    sys.stdout.write(final_output)
    
    
    
        

    

