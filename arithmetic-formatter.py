def arithmetic_arranger(problems, bol):
    if(len(problems) > 5):
        return print("Error: There are too many problems")
    split_problems = []
    for x in problems:
        split_problems.append(x.split(" "))
    # return split_problems
    operands = []
    sign = []
    for m in range(len(split_problems)):
        for n in split_problems[m]:
            if(n.isnumeric()):
                operands.append(n)
            elif (n == "+" or n == "-"):
                sign.append(n)
            else:
                return print(
                    "Error: You cannot input something that is not numerical or that is not one of the following operators: + or -")
    # return f"The list of operands is :{operands}\nThe list of operators is:{sign}"
    op1 = []
    op2 = []
    for op in range(len(operands)):
        if(op % 2 == 0):
            op1.append(operands[op])
        else:
            op2.append(operands[op])
    print(op1)
    print(op2)

    for i in range(len(op1)):
        mx = 0
        if(len(op1[i]) >= len(op2[i])):
            mx = len(op1[i])
            print(f"{int(op1[i]):>{mx+2}}", end="    ")
        else:
            mx = len(op2[i])
            print(f"{int(op1[i]):>{mx+2}}", end="    ")
    print("")

    for j in range(len(op1)):
        mx = 0
        if(len(op1[j]) >= len(op2[j])):
            mx = len(op1[j])
            print(f"{sign[j]}{int(op2[j]):>{mx+1}}", end="    ")
        else:
            mx = len(op2[j])
            print(f"{sign[j]}{int(op2[j]):>{mx+1}}", end="    ")
    print("")

    for k in range(len(op1)):
        mx = 0
        if(len(op1[k]) >= len(op2[k])):
            mx = len(op1[k])
            print(f"{'-'*(mx+2)}", end="    ")
        else:
            mx = len(op2[k])
            print(f"{'-'*(mx+2)}", end="    ")
    print("")

    for l in range(len(op1)):
        mx = 0
        if(len(op1[l]) >= len(op2[l])):
            mx = len(op1[l])
            if(bol == True):
                if(sign[l] == "+"):
                    print(f"{(int(op1[l]) + int(op2[l])):>{mx+2}}", end="    ")
                else:
                    print(f"{(int(op1[l]) - int(op2[l])):>{mx+2}}", end="    ")
            else:
                continue
        else:
            mx = len(op2[l])
            if(bol == True):
                if(sign[l] == "+"):
                    print(f"{(int(op1[l]) + int(op2[l])):>{mx+2}}", end="    ")
                else:
                    print(f"{(int(op1[l]) - int(op2[l])):>{mx+2}}", end="    ")
            else:
                continue


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
