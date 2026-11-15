instr = str(input())
ip = {}

if instr[0] == '@':
  ip.update({'Type':'A','Value':f'{instr[1:]}'})
  print(ip)
else:
  if "=" in instr:
    dest,comp = instr.split("=",1)
    ip.update({'Type':'C','Dest':f'{dest}','Comp':f'{comp}','Jump':'None'})
    print(ip)
  else :
    comp,jump = instr.split(';',1)
    ip.update({'Type':'C','Dest':'None','Comp':f'{comp}','Jump':f'{jump}'})
    print(ip)
