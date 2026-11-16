def preprocessor(asm):
    with open("Pong.asm","r") as f:
        for line in f:
            if '//' in line[0:2]:
                continue
            else:
                if '//' in line:
                    line = line.split("//",1)[0].strip()
                    asm.append(line)
                elif line.strip():
                    asm.append(line.strip('\n').strip())
    return asm

def first_pass(sym_tab,asm):
    addr_counter = 0
    for symb in asm: 
        if symb[0] == '(':   
            label = (symb.split("(",1)[1].split(")",1)[0])
            sym_tab[label] = str(addr_counter) 
        else:
            addr_counter +=1
    return sym_tab

def var_alloc(sym_tab,asm,vc):
    while(vc < 16384):
        for var in asm:
            if var[0] == '@':
                ref = var[1:]
                if ref in sym_tab or ref.isdigit() :
                    continue
                else:
                    sym_tab[f'{ref}'] = vc
                    vc += 1
            else: continue
        return sym_tab,vc
                
def second_pass(st,ase,var_c,mc):
    for c in ase:
        if c[0] == '(':
            continue
        elif c[0] == '@':
            ref = c[1:]
            if ref in st or ref.isdigit():
                mc.append(encoder(c,st))
            else:
                var_alloc(st,ase,var_c)
                mc.append(encoder(c,st))
        else:
            mc.append(encoder(c,st))
                

def encoder(ins,sym_tab):
    des = {'M':'001','D':'010','MD':'011','DM':'011','A':'100','AM':'101','MA':'101','AD':'110','DA':'110','AMD':'111','ADM':'111','DAM':'111','DMA':'111','MDA':'111','MAD':'111'}
    jum = {'JGT':'001','JEQ':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'}
    com ={'0':'0101010','1':'0111111','-1':'0111010','D':'0001100','A':'0110000','!D':'0001101',
          '!A':'0110001','-D':'0001111','-A':'0110011','D+1':'0011111','A+1':'0110111','D-1':'0001110',
          'A-1':'0110010','D+A':'0000010','D-A':'0010011','A-D':'0000111','D&A':'0000000','D|A':'0010101',
          'M':'1110000','!M':'1110001','-M':'1110011','M+1':'1110111','M-1':'1110010','D+M':'1000010','D-M':'1010011',
          'M-D':'1000111','D&M':'1000000','D|M':'1010101'}
    
    if (ins[0] == '@'):
        if ins[1:].isdigit():
            value = int(ins[1:])
            val = str(bin(value)[2:].zfill(15))
            return '0' + val
        else:
            if ins[1:] in sym_tab:
                value = int(sym_tab[f"{ins[1:]}"])
                val = str(bin(value)[2:].zfill(15))
                return '0' + val
    else :
        if "=" in ins:
            if ";" in ins:
                jump = ins.split(";",1)[1]
                dest,comp = ins.split("=",1)
                if dest in des:
                    if comp in com:
                        if jump in jum:
                            return '111' + com[comp] + des[dest] + jum[jump]
                        else:
                            return "Invalid Jump !"
                    else:
                        return "Invalid Comp !"
                else:
                    return "Invalid Dest !"
            else:
                dest,comp = ins.split("=",1)
                if dest in des:
                    if comp in com:
                        return '111' + com[comp] + des[dest] + '000'
                    else:
                        return "Invalid Comp !"
                else:
                    return "Invalid Dest !"
        else:
            if ";" in ins:
                comp,jump = ins.split(';',1)
                if comp in com:
                    if jump in jum:
                        return '111' + com[comp] + '000' + jum[jump] 
                    else:
                        return "Invalid Jump !"
                else:
                    return "Invalid Comp !"
            else: 
                comp = ins
                return '111' + com[comp] + '000' + '000'

symbols = {'SP':'0','LCL':'1','ARG':'2','THIS':'3','THAT':'4','SCREEN':'16384','KBD':'24576','R0':'0','R1':'1','R2':'2','R3':'3','R4':'4','R5':'5','R6':'6','R7':'7','R8':'8','R9':'9'
           ,'R10':'10','R11':'11','R12':'12','R13':'13','R14':'14','R15':'15'}
pp_asm = []
machine = []

var_counter = 16
preprocessor(pp_asm)
first_pass(symbols,pp_asm)
second_pass(symbols,pp_asm,var_counter,machine)

with open ("Pong.hack", "w") as f:
    for mc in machine:
        f.write(f"{mc}\n")