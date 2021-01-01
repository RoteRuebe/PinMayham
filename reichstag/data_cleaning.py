f = open("ZA8013_Wahldaten.csv")
lines = f.readlines()
f.close()

cells = []
for I in lines:
    isOdd=False
    J=""
    for char in I:
        if char=='"':
            isOdd = not isOdd
        # int("7300continue
        if char=="," and isOdd:
            char = ""
            continue
        J+=char
    tmp = J.split(",")
    cells.append(tmp)
    
cells = cells[1:]
    
final = {}

def add_lines (number, line1, line2):
    line1 = list(line1)
    nline = range(len(line1))
    
    for I in nline:
        if line2[I+6] == "-9":
            pass
        else:
            line1[I] += int(line2[I+5].replace('"',''))
        
    return tuple(nline)

def prepare_line (number, line):
    keys = []
    
    for I in range(len(line)):
        if I < 6:
            pass
        else:
            value = int(line[I].replace('"',''))
            if value == -9:
                keys.append(0)
            else:
                keys.append(value)
    
    return {number:tuple(keys)}

for I in cells:
    number = int(I[139].replace('"',''))
    
    if number == 0:
        pass
    else:
        if I[139] in final.keys():
            final[I[139]] = add_lines( number,final[I[139]],I[:39] ) 
        else:
            final.update( prepare_line(number,I[:39]) )
                        
print(final)