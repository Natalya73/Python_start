import sys
# receive command line args
args = sys.argv[1:] 
# if there are args from command line
if args:
#convert the arg into int
    iterations = int(args[0])
# iterate according to iterations
    try:
        for i in range(iterations):
# receiving the input
            line = input()
            if not line:
                break
            elif line[0] == '0' and line[1] == '0' and line[2] == '0' and line[3] == '0' and line[4] == '0' and line[5] !='0' and len(line) == 32:
                print(line.strip())
    except EOFError:
        print("End of file")
else:
    print("Specify a number for iterations")
