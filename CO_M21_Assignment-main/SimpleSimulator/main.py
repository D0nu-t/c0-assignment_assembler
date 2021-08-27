import sys
instructions = []
opcode_dic={'00000':'add','00001':'sub','00010':'movi','00011':'movr','00100':'ld','00101':'st','00110':'mul','00111':'div','01000':'rs','01001':'ls','01010':'xor','01011':'or','01100':'and','01101':'not','01110':'cmp','01111':'jmp','10000':'jlt','10001':'jgt',"10011":'hlt'}
reg_dic={'000':0,'001':0,'010':0,'011':0,'100':0,'101':0,'110':0,'111':0}
pc=0
def decimalToBinary(t, b):
    n= bin(t).replace("0b", "")
    while len(n)<b:
        n="0"+n
    return n
def loadData():
    while True:
        s = input()
        if s=="":
            break
        instructions.append(s)

def defineMemory():
    SIZE = 256
    global memory 
    memory=[]
    for a in range(SIZE):
        memory.append("0000000000000000")

    i=0
    for instruction in instructions:
        memory[i] = instruction
        i += 1

pc = 00000000
halted = False
def executionEngine(code):
    global halted
    global pc
    global reg_1,reg_2,reg_3,reg_4,reg_5,reg_6,reg_7
    reg_1,reg_2,reg_3,reg_4,reg_5,reg_6,reg_7=0,0,0,0,0,0,0
    val=0
    address=0
    imm=0
    #code=str(code)
    op="hlt"
    try:
        op=opcode_dic[code[0:5]]
    except:
        pass
    if op == "add":
        reg_1, reg_2, reg_3=code[7:10],code[10:13],code[13:16] 
        reg_dic[reg_1]=reg_dic[reg_2]+reg_dic[reg_3]
        t = reg_dic[reg_1]
        if t>65535:
            reg_dic[reg_1] = 0

    elif op == "sub":
        reg_1, reg_2, reg_3=code[7:10],code[10:13],code[13:16]  
        if reg_dic[reg_3]<reg_dic[reg_2]:
            reg_dic[reg_1]=reg_dic[reg_2]-reg_dic[reg_3]
        else:
            reg_dic[reg_1]=0
    elif op == "movi":
        reg_1,val=code[5:8], code[8:16]
        t = int(val, base=2)
        reg_dic[reg_1]=t
   
    elif op == "movr":
        reg_1,reg_2=code[10:13],code[13:16]
        reg_dic[reg_1]=reg_dic[reg_2]
    
    elif op == "rs":
        reg_1, imm = code[5:8], int(code[8:16],2)
        t=reg_dic[reg_1]
        t >> imm
        reg_dic[reg_1]=t
    
    elif op == "ls":
        reg_1, imm=code[5:8], int(code[8:16],2)
        t=reg_dic[reg_1]
        t << imm
        reg_dic[reg_1]=t

   
    elif op == "xor":
        reg_1,reg_2,reg_3=code[7:10],code[10:13],code[13:16]
        reg_dic[reg_1]=reg_dic[reg_2]^reg_dic[reg_3]
    
    elif op == "or":
        reg_1, reg_2, reg_3=code[7:10],code[10:13],code[13:16]
        reg_dic[reg_1]=reg_dic[reg_2]|reg_dic[reg_3]
    
    elif op == "and":
        reg_1, reg_2, reg_3=code[7:10],code[10:13],code[13:16]
        reg_dic[reg_1]=reg_dic[reg_2]&reg_dic[reg_3]
    
    elif op == "not":
        reg_1,reg_2=code[10:13],code[13:16]
        temp=~reg_dic[reg_2]
        if(temp>0):
            reg_dic[reg_1]=temp
    
    elif op == "ld":
        
        a,b=code[5:8],code[8:16]
        x = decimalToBinary(int(b),8)
        a = memory[x]
    elif op == "st":
        
        a,b=code[5:8],code[8:16]
        x = int(b, base=2)
        memory[x] = a
    
    elif op == "mul":
        reg_1,reg_2,reg_3=code[7:10],code[10:13],code[13:16]
        reg_dic[reg_1]=reg_dic[reg_2]*reg_dic[reg_3]
        t = reg_dic[reg_1]
        if t>65535:
            reg_dic[reg_1] = 0

    elif op == "div":
        reg_1 ,reg_2=code[10:13],code[13:16]
        reg_3=reg_dic[reg_1]
        r4=reg_dic[reg_2] 
        reg_dic["000"]= reg_3//r4       
        reg_dic["001"]= reg_3%r4
    elif op == "cmp":
        a,b=code[10:13],code[13:16]
        re1 = reg_dic[a]
        re2 = reg_dic[b]
        reg_1 = int(re1)
        reg_2 = int(re2)
        if reg_1 > reg_2:
            reg_dic['111']=="0000000000000010"
        elif reg_1<reg_2:
            reg_dic['111']=="0000000000000100"
        else: 
            reg_dic['111']=="0000000000000001"
    elif op == "jmp":
        address=code[8:16]
         
        pc=address
    elif op == "jlt":
        address=code[8:16]
         
        if reg_dic['111']=="0000000000000100":
            pc = int(address, base=2)
    elif op == "jgt":
        address=code[8:16]
         
        if reg_dic['111']=="0000000000000010":
            pc = int(address, base=2)   
    elif op == "je":
        address=code[8:16]
         
        if reg_dic['111']=="0000000000000001":
            pc = int(address, base=2)
    if op == "hlt":
        halted=True
        return 
loadData()
defineMemory()
def main():
    global pc
    global halted
    loadData()
    defineMemory()
    count = 0
    for i in memory:
        count+=1
        if i[0:5]=="10011":
            break
    print(count)

    for i in range(count):     
        for data in  memory:
            executionEngine(data)
        #complete the execution engine code
        print(decimalToBinary(pc, 8) + " ")
        print(decimalToBinary(reg_dic['000'],16) + " ")
        print(decimalToBinary(reg_dic['001'],16) + " ")
        print(decimalToBinary(reg_dic['010'],16) + " ")
        print(decimalToBinary(reg_dic['011'],16) + " ")
        print(decimalToBinary(reg_dic['100'],16) + " ")
        print(decimalToBinary(reg_dic['101'],16) + " ")
        print(decimalToBinary(reg_dic['110'],16) + " ")
        print(decimalToBinary(reg_dic['111'],16) + " ")
        print("\n")
        pc+=1
        count +=1
    for i in memory:
         print(i)

if __name__ == "__main__":
    main()