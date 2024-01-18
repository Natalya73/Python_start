matrix = []
with open('m.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        matrix.append(row)
if len(matrix) ==3 and len(matrix[0]) == 5:
    if (matrix[0][0] == '*' and 
        matrix[0][1] != '*' and 
        matrix[0][2] != '*' and 
        matrix[0][3] != '*' and 
        matrix[0][4] == '*' and 
        matrix[1][0] == '*' and 
        matrix[1][1] == '*' and 
        matrix[1][2] != '*' and 
        matrix[1][3] == '*' and 
        matrix[1][4] == '*' and 
        matrix[2][0] == '*' and 
        matrix[2][1] != '*' and 
        matrix[2][2] == '*' and 
        matrix[2][3] != '*' and 
        matrix[2][4] == '*'):
        print("True")
    else:
        print("False")
else:
    print("Error")

        



    
