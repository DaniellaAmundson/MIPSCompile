def main():
        fp=open("mips_funct.txt","r")
        gp=open("mips_opcodes.txt","r")
        hp=open("mips_registers.txt","r")
        
        registers={}
        opcodes={}
        function={}
        labeldecimal={}
        Line=[]
        label=[]
        
        asm("Lab7_file3.asm",Line,label)
        label2decimal(labeldecimal,label)
        dec2bin(label2decimal, 5)
        

        while True:
            line = fp.readline()
            if line == "":
                break
            line=line.strip()
        
            value=line.split()

            function[value[0]]=str(value[1])


        

        while True:
            line = gp.readline()
            if line == "":
                 break
            line=line.strip()
        
            value=line.split()

            opcodes[value[0]]=str(value[1])
        
        
        while True:
            line = hp.readline()
            if line == "":
                break
            line=line.strip()
        
            value=line.split()
            dec = int(value[1])
            binary = dec2bin(dec, 5)

            registers[value[0]]=str(binary)

        
def asm(name,Line,label):
    op=open(name,"r")
    while True:
        line= op.readline()
        
        if line== "":
            break
        line = line.replace("\t", "")
        line = line.replace("\\t", "")
        line = line.replace("\r", "")
        line = line.strip()
        if line == "":
            pass
        elif line[0] =="#":
            pass
        elif "#" in line:
            pound =  line.split("#")
            line =pound[0]
            Line.append(line)
            
        elif line[0] == ".":
            pass
        elif line [0] == "\n":
            pass 
        elif "syscall" in line:
            pass
        elif ":" in line:
            column=line.split(":")
            line=column[0]
            label.append(line)
        else:
            Line.append(line)
                                   
    
def label2decimal(labeldecimal,label):
    
    labeldecimal[0]=40000
    
    for i in range(1,5):
        labeldecimal[i]=labeldecimal[i-1]+40

    for i in labeldecimal:
            print i, labeldecimal[i]
            
        
def dec2bin(label2decimal,registerSize):
    breakdown = abs(decimal)
    
    regNeed = 0
    binaryResult = ""
    while True: 
        if breakdown == 0:
            break
        rem = breakdown % 2
        breakdown = breakdown / 2
        binV.append(rem)
    regNeed = registerSize - len(binV)
    for i in range(regNeed): 
        binV.append(0)
    
    if decimal < 0: 
        twosComp()
    binV.reverse()

    for i in range(len(binV)):
        binaryResult += str(binV[i])
    return(binaryResult) 


def twosComp():
    count = 0
    for i in range(len(binV)):
        if binV[i] + 1 == 2: 
            binV[i] = 0
        else:
            binV[i] = 1

    while True:
        if binV[count] == 0: 
            binV[count] = 1
            break
        else:
            binV[count] == 1
            binV[count] = 0
        count += 1
    return()


        
main()
