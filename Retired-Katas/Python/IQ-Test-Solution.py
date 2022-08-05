def iq_test(numbers):
    set = numbers.split()
    even = 0
    odds = 0
    position = 0
    
    for i in range(0, len(set)):
        if(int(set[i]) % 2 == 0):
            even = even + 1
        else:
            odds = odds + 1
    
    if (odds > even):
        for i in range(0, len(set)):
            if (int(set[i]) % 2 == 0):
                position = i+1
    else:
        for i in range(0, len(set)):
            if (int(set[i]) % 2 != 0):
                position = i+1
    return position
    #your code here