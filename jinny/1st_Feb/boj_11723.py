import sys
S = 1 << 21
for _ in range(int(sys.stdin.readline())):
    input_cal = sys.stdin.readline().rstrip()
    if input_cal == "all":
        S = 0b111111111111111111111
    elif input_cal == "empty":
        S = 0
    else:
        set_cal, str_x = input_cal.split()
        x = int(str_x)-1
        if set_cal == "add":
            S = S | (1 << x)
        elif set_cal == "remove":
            S2 = S ^ (1 << x)
            S = S & S2
        elif set_cal == "check":
            if S & (1 << x):
                print(1)
            else:
                print(0)
        else:
            S = S ^ (1 << x)