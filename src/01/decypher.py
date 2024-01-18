import sys
args = sys.argv[1:] 
if args:
    string = args[0]
    string0 = (string.split())
    string2 = zip(*string0)
    string3 = next(string2)
    string4 = "".join(string3)
    print(string4.strip())
else:
    print("Specify an argument")
