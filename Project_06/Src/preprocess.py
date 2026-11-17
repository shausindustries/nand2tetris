asm = []
with open("code.asm","r") as f:
    for line in f:
        if '//' in line[0:2]:
            continue
        else:
            if '//' in line:
                ic = line.split("//",1)[0]
                line = ic.strip()
                asm.append(line)
            elif line.strip():
                asm.append(line.strip('\n'))
print(asm)
