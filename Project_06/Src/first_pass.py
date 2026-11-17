sym_tab = {'SP':'0','LCL':'1','ARG':'2','THIS':'3','THAT':'4','SCREEN':'16384','KBD':'24576','R0':'0','R1':'1','R2':'2','R3':'3','R4':'4','R5':'5','R6':'6','R7':'7','R8':'8','R9':'9'
           ,'R10':'10','R11':'11','R12':'12','R13':'13','R14':'14','R15':'15'}
asm = ["@START","0;JMP","@10","D=A","(START)","@20","D=A"]
addr_counter = 0
for symb in asm: 
    if symb[0] == '(':   
        label = (symb.split("(",1)[1].split(")",1)[0])
        if label in sym_tab:
            continue
        else:
            sym_tab[label] = str(addr_counter) 
    else:
        addr_counter +=1

print(sym_tab)