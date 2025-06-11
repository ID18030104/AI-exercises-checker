matrix_string = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""


matrix = []
lines = matrix_string.strip().split('\n')
for line in lines:
    matrix.append(list(line))

print("Matrice 2D:")
for row in matrix:
    print(row)


decoded_message = ""
num_cols = len(matrix[0])  

for col in range(num_cols):
   
    for row in range(len(matrix)):
        char = matrix[row][col]
        
        
        if char.isalpha():
            decoded_message += char
        else:
            
            if decoded_message and decoded_message[-1] != ' ':
                decoded_message += ' '


decoded_message = decoded_message.strip()

print(f"\nMessage décodé: '{decoded_message}'")