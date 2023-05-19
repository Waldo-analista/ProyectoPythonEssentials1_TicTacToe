from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')



def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    try:
        ingreso=input('Ingresa número entero entre 1 a 9: ')
        if ingreso=='q':
            return 'q'
        numero_ingresado=int(ingreso)
        if numero_ingresado>0 and numero_ingresado<10:
            diccionario={1:[0,0],2:[0,1],3:[0,2],
                 4:[1,0],5:[1,1],6:[1,2],
                 7:[2,0],8:[2,1],9:[2,2]}
            existe=False
            for row in board:
                if numero_ingresado in row:
                    existe=True
                    break
            if existe==True:
                i,j=diccionario[numero_ingresado]
                board[i][j]='O'
                return board
            else:
                print('Lugar no esta disponible para ingresar. Ingresa otro')
                return enter_move(board)
        else:
            print('Has ingresado un número no el rango de 1 a 9, cotas inclusive')
            return enter_move(board)

    except ValueError:
        print('Has ingresado un caracter no numérico')
        return enter_move(board)

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    lista=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]!='O' and board[i][j]!='X':
                lista.append((i,j))
    return lista



def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    ganador=None
    if sign=='X':
        ganador='Computador'
    if sign=='O':
        ganador='Tú(humano)'
    ganar=[[sign,sign,sign]]
    board_traspuesta=[[board[j][i] for j in range(3)] for i in range(3)]
    board_diagonal=[[ board[i][i] for i in range(3)],[board[i][2-i] for i in range(3)]]
    for i in board:
        if i in ganar:
            return f'El ganador es: {ganador}'
    for i in board_traspuesta:
        if i in ganar:
            return f'El ganador es: {ganador}'
    for i in board_diagonal:
        if i in ganar:
            return f'El ganador es: {ganador}'
    if len(make_list_of_free_fields(board))==0:
        return 'No hay más espacios disponibles. Juego Terminado no ha ganado nadie'
    else:
        return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    if board==[[1,2,3],[4,5,6],[7,8,9]]:
        return [[1,2,3],[4,'X',6],[7,8,9]]
    else:
        lista_campos_vacios=make_list_of_free_fields(board)
        tamaño=len(lista_campos_vacios)
        try:
            lugar= randrange(tamaño)
            posicion=lista_campos_vacios[lugar]
            i,j=posicion
            board[i][j]='X'
            return board
        except ValueError:
            return board

#Las lineas de abajo me sirvieron para probar cada funcion de manera AISLADA
#display_board([[1,2,3],[4,5,6],[7,8,9]])
#print(enter_move([['O', 2, 3], [4, 5, 6], [7, 8, 9]]))
#print(make_list_of_free_fields([['O', 'O', 3], ['X', 5, 6], ['O', 'O', 'X']]))
#print(victory_for([['O', 'O', 'O'], [4, 5, 6], [7, 8, 9]],'O'))
#print(draw_move([[1,'X','X'],['X','X','X'],['X','X','X']]))
board=[[1,2,3],[4,5,6],[7,8,9]]
while True:
    if board==[[1,2,3],[4,5,6],[7,8,9]]:
        print('Ha comenzado el juego del Gato')
        print("El computador usa la marca 'X' y el usuario(tu) usas la marca 'O'")
        print('Ingresa q para salir en cualquier momento del juego')
    board=draw_move(board)
    display_board(board)
    result=victory_for(board,'X')
    if result:
        print(result)
        input()
        break

    board=enter_move(board)
    if board=='q':
        print('Has salido del programa')
        break
    result1=victory_for(board,'O')
    if result1:
        print(result1)
        print('El Tablero Final es el siguiente:')
        display_board(board)
        input()
        break
    display_board(board)
