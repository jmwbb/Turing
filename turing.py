tape = [0,0,0,0,0,0,1]
head = 0
state = 0
states = [[[1,0,0],[0,1,"H"]],[[0,1,1],[0,1,0]]]
hold = 0
def nts(x):
        if(x==0):
                return "<"
        if(x==1):
                return ">"
def stateformat():
        print(" 0 | 1\n-------\n A | D\n B | E\n C | F\n[[A,B,C],[D,E,F]]")
def prstatetest(x):
        print(" 0 | 1  " * len(x))
        print("------- " * len(x))
        print(" ", end="")
        for n in range(0,len(x)):
                print(str(x[n][0][0]) + " | " + str(x[n][1][0]) + "   ", end="")
        print("\n ", end="")
        for n in range(0,len(x)):
                print(nts(x[n][0][1]) + " | " + nts(x[n][1][1]) + "   ", end="")
        print("\n ", end="")
        for n in range(0,len(x)):
                print(str(x[n][0][2]) + " | " + str(x[n][1][2]) + "   ", end="")
def increment():
        global head, state, hold, tape
        if(head >= len(tape)):
                for n in range(head-len(tape)+1):
                        tape.append(0)
        elif(head == -1):
                tape.insert(0,0)
                head = 0
        hold = tape[head]
        tape[head] = states[state][hold][0]
        if states[state][hold][1] == 0:
                head -= 1
        else:
                head += 1
        state = states[state][hold][2]
def run(x,m):
        global tape, head, state
        state = 0
        tape = x
        head = m
        while state != "H":
                print("  " + str(tape) + str(state))
                print("   " + " " * head * 3 + "^")
                increment()
        print("  " + str(tape) + " >> HALT")
        print("   " + " " * head * 3 + ">...")
def runf(x,m,n):
        global tape, head, state
        state = 0
        tape = x
        head = 0
        for y in range(n):
                if(state != "H"):
                        increment()
                        print("  " + str(tape) + str(state))
                        print(" " * head * 3 + "^")
                else:
                        print("  " + str(tape) + " >> HALT")
                        print("   " + " " * head * 3 + ">...")
                        break
        if(state != "H"):
                print("  " + str(tape) + " >> TIMED OUT")
                print("   " + " " * head * 3 + ">...")
