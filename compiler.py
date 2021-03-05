import copy

table = {
    "jez": "JUMPZ",
    "jmp": "JUMP",
    "jlz": "JUMPN"
}

instructions = [
    "add",
    "sub",
    "take",
    "put",
    "input",
    "output",
    "jmp",
    "jez",
    "jlz",
]

#translate a command to HRMA
def translate(command,args):
    output = []
    if command == "instanciate":
        variables[args[1]] = args[0]

    if command == "take":
        if args[0] == "input":
            output.append("INBOX")
        else:
            output.append(f"COPYFROM {args[0]}")

    elif command == "put":
        if len(args) == 1:
            return translate(command,["hand",args[0]])

        if args[0] == "input":
            output.append("INBOX")
        elif args[0] != "hand":
            output.append(f"COPYFROM {args[0]}")
        elif args[0] == "hand": 
            pass

        if args[1] == "output":
            output.append("OUTBOX")
        elif args[1] != "hand":
            output.append(f"COPYTO {args[1]}")
        elif args[1] == "hand":
            pass

    elif command == "increment":
        if args[0] in variables:
            output.append(f"BUMPUP {args[0]}")
        else:
            output.append(f"BUMPUP {args[0]}")

    elif command == "decrement":
        if args[0] in variables:
            output.append(f"BUMPDN {args[0]}")
        else:
            output.append(f"BUMPDN {args[0]}")

    elif command == "add":
        output.append("ADD "+args[0])

    elif command == "sub":
        output.append("SUB "+args[0])

    elif command in table:
        output.append(table[command] + " " + args[0])

    else:
        output.append(line)

    return output

#translate straight from a line
def translate_line(line):
    if ">" in line:
        command = "instanciate"
        args = [line[:line.find(">")], \
                line[line.find(">")+1:]]
    elif "=" in line:
        command = "put"
        args = [line[:line.find("=")],\
                line[line.find("=")+1:]]
    elif "++" in line:
        command = "increment"
        args = [line[:line.find("++")]]
    elif "--" in line:
        command = "decrement"
        args = [line[:line.find("--")]]
    else:
        if "(" not in line and line[:3] in table.keys():
            command = line[:3]
            args = [line[3:]]
        else:
            command = line[:line.find("(")]
            args = line[line.find("(")+1:line.find(")")].split(",")

    for i, e in enumerate(args):
        if "[" in e:
            var = e[e.find("[")+1:e.find("]")]
            if var in variables:
                args[i] = f"[{variables[var]}]"

        elif e in variables:
            args[i] = variables[args[i]]

    return translate(command,args)

while True:
    with open("C:\\Users\\Yannick\\HRM\\input.txt","rt") as f:
        text = f.readlines()
    print(text)
    #format text
    new_text = []
    for line in text:
        if line.replace(" ","") not in ["","\n"]:
            new_text.append(line.replace("\n",""))
    text = new_text

    #instanciate variables / assign value
    variables = {}
    code = []
    print(variables)

    for line in text:
        for i in translate_line(line.replace(" ","")):
            code.append(i)

    code = "\n".join(code)

    print("translating done")

    with open("C:\\Users\\Yannick\\HRM\\output.txt","wt") as f:
        f.write(code)

    input("recompile?")