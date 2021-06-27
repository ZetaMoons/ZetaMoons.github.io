# Use the range

range(3)

# exemplo de loop

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])
    
 # exemplo de loop for

for i in range(0, 8):
    print(i)


# exemplo de loop for via lista

for year in dates:  
    print(year)   
    
# Usar for loop para mudar uma lista

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])
    
    
# Loop por lista e numerar a lista

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)
    
    
# Exemplo de loop while

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")


# escreva um for loop usando a função range com os numeros -5,5
for i in range(-5, 6):
    print(i)
    
    
# Imprima os elementos da seguinte lista: Gêneros = ['rock', 'R&B', 'trilha sonora', 'R&B', 'soul', 'pop']
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)
    
    
# digite um for loop que imprima a seguinte lista: squares=['red', 'yellow', 'green', 'purple', 'blue']
squares=['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)
    
    
# Escreva um loop while para exibir os valores da classificação de uma lista de reprodução de álbum armazenada na lista PlayListRatings. 
Se a pontuação for inferior a 6, saia do loop. 
A lista PlayListRatings é fornecida por: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]
while(i < len(PlayListRatings) and Rating >= 6):
    Rating = PlayListRatings[i]
    print(Rating)
    i = i + 1
    
# Escreva um loop while para copiar as strings 'laranja' dos quadrados da lista para a lista new_squares. 
Pare e saia do loop se o valor na lista não for 'laranja':
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while( i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
    print(new_squares)
