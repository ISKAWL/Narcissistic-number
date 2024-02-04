while True:
    string = str( input( "enter Q or q for quit: " ) )
    if string == 'q':
        break
    elif string == 'Q':
        break                    #enter q/Q for quit 
    else:
        Power_of_power = 3
        for i in range(100, 999):
            bit = i % 10         #get the bit of i
            Ten_bits = (i % 100) // 10 #get the Ten_bits of i
            Hundred = i // 100   #get the hundred of i
            if bit**3 + Ten_bits**3 + Hundred**3 == i :
                print( "Narcissistic-number is: " + str(i) )
        