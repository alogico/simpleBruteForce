def brutal ():
    for i in range(0,1000):
        password=(f'{i:03}')
        if int(password) is 199 :
            print ('you got it')
            break
        else:
             print ('nope')


brutal()
