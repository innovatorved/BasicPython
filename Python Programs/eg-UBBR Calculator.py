while True : 
    print ('UBBR Calculator')
    baud_rate = int(input ('Enter baudrate : '))
    f_osc = int(input ('Enter Ferquency : '))
    ubbr = (f_osc/(16*baud_rate))-1
    print ('UBBR value in decimal is : ', ubbr)
