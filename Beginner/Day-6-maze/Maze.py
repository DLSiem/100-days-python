def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
def right_is_clear():
    turn_right()
    if front_is_clear():
        turn_left()
        return True
    else:
        turn_left()
        return False
    

while not at_goal():
    
    if front_is_clear() and not right_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
        if not front_is_clear():
            turn_left()
            move()
     
    
        
        
        
        
        
        
        
    
    
     
        
    



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
