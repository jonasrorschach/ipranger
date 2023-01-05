'''
Idéia, medir a distância de IPV4 disponíveis em cada região do mundo, com a tese de tentar
medir quantos endereços disponíveis existem em cada país
'''



i = 0
x = 0
z = 0
y = 0

new_ip = [i, x, z, y]

while i < 256:
    
    while x < 256:
        

        while y < 256:

            while z < 256:
            
                print(new_ip)
               
                z += 1
                new_ip = [i, x, y, z]


            print(new_ip)
            
            y += 1
            z = 0
            new_ip = [i, x, y, z]
        
        print(new_ip)
        
        x += 1
        new_ip = [i, x, y, z]
        y = 0

    print(new_ip)
    new_ip = [i, x, y, z]
    i += 1
    x = 0


