x = 0
def random_player(player_id : int, board : [int]) -> int:
    possible_pit_id = random.randint(0,5)
    x = possible_pit_id
    return possible_pit_id

#Mimic the other player's moves
def my_ai1(player_id : int, board : [int]) -> int:

        return 12-x

#Try the first 3 spots closest to the store. If they are empty, randomly picks a spot.
def my_ai2(player_id : int, board : [int]) -> int:
    if board[10] != 0:
        possible_pit_id = 10
        return possible_pit_id
    elif board[11] != 0:  
        possible_pit_id = 11
        return possible_pit_id
    elif board[12] != 0:  
        possible_pit_id = 12
        return possible_pit_id
    else:
        possible_pit_id = random.randint(7,12)

        return possible_pit_id

#Try all the spots that are closes to the store firs, without any randomness
def my_ai3(player_id : int, board : [int]) -> int:
    if board[12] != 0:
        possible_pit_id = 12
        return possible_pit_id
    elif board[11] != 0:  
        possible_pit_id = 11
        return possible_pit_id
    elif board[10] != 0:  
        possible_pit_id = 10
        return possible_pit_id
    elif board[9] != 0:  
        possible_pit_id = 9
        return possible_pit_id
    elif board[8] != 0:  
        possible_pit_id = 8
        return possible_pit_id
    else:
        possible_pit_id = 7

        return possible_pit_id

def my_ai3_reversed(vplayer_id : int, board : [int]) -> int:
    if board[5] != 0:
        possible_pit_id = 5
        return possible_pit_id
    elif board[4] != 0:  
        possible_pit_id = 4
        return possible_pit_id
    elif board[3] != 0:  
        possible_pit_id = 3
        return possible_pit_id
    elif board[2] != 0:  
        possible_pit_id = 2
        return possible_pit_id
    elif board[1] != 0:  
        possible_pit_id = 1
        return possible_pit_id
    elif board[0] != 0:  
        possible_pit_id = 0
        return possible_pit_id
 
