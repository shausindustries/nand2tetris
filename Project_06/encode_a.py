instr = str(input())
value = int(instr[1:])

val = str(bin(value)[2:].zfill(15))

if (instr[0] == '@'):
  print('0' + val)
else :
  print('1' + val)
