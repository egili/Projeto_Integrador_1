            
def define_used_transport():
    print('\n+----------------------------------------------+')
    print("| Qual o meio de transporte você usou hoje?:   |")
    print('+----------------------------------------------+')
    print("| [1] transporte público (ônibus, metrô, trem) |")
    print("| [2] Bicicleta                                |")
    print("| [3] Caminhada                                |")
    print("| [4] Carro (combustível fóssil)               |")
    print("| [5] Carro elétrico                           |")
    print("| [6] Carona compartilhada                     |")
    print("+----------------------------------------------+")

    while True:
        try:
            transport = int(input("\n > "))  
        
        except ValueError:
            print('[ Opção inválida! Informe um número entre 1 e 6. ]')
        
        else:
            if 1 <= transport <= 6:
                return transport
            else:    
                print('[ Opção inválida! Informe um número entre 1 e 6. ]')