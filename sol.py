def make_chocolate(small, big, goal):
    # Use as many big bars as possible
    max_big_bars = min(big, goal // 5)
    remaining_weight = goal - max_big_bars * 5

    # Check if the remaining weight can be covered by small bars
    if remaining_weight <= small:
        return remaining_weight
    else:
        return -1
    
'''
The code calculates how many big bars can be used (as each big bar is 5 kilos), 
then checks how much weight is left after using those big bars. 
If the remaining weight can be covered by the available small bars, it returns that number. 
If not, it returns `-1`.
'''