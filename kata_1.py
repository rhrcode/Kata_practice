# start  kata
def lovefunc( flower1, flower2 ):
    
    
    if flower1 % 2 == 0:
        parf1 = True
    else:
        parf1 = False
        
    if flower2 % 2 == 0:
        parf2 = True
    else:
        parf2 = False
    
    if parf1 == True and parf2 == False or parf1 == False and parf2 == True:
        return True
    else:
        return False
    
# end kata
numero_1 = int(input("cuantos petalos tiene su trebol: " ))
numero_2 = int(input("cuantos petalos tiene su trebol: " ))
amor =lovefunc(numero_1,numero_2)

if amor == True:
    print("Estan enamorados")
else:
    print("No Funcionara")