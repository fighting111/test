for hundreds in range(1,10):
    for tens in range(0,10):
        for ones in range(0,10):
            x = hundreds*100 + tens*10 + ones
            if x == hundreds**3 + tens**3 + ones**3:
                print(x)
