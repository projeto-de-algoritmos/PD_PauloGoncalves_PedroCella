# Import
from utils import greed
from utils import trabalho as T
# Contexto
print('Bem-vindo ao NOMEDOTRABALHO, seu funcionamento se baseia em uma central que recebe uma lista de crimes cometidos e utilizando de Programação Dinâmica estabelece uma prioridade de atendimentos, além disso utiliza-se também de Interval Partitioning para saber a quantidade de viaturas que estarão em serviço no dia.')

print('\nSeu objetivo é estabelecer a duração de um crime, começo e fim, bem como a prioridade que aquele crime detém e descrever qual é aquele tipo do crime para que o algoritmo possa fornecer a quantidade de viaturas que deverão estar em serviço e quais crimes cada uma deverá ser responsável')


#Usuário

print('Para utilizar basta escolher:\n1- Inserir crimes\n2- Utilizar crimes já registrados\n3- Sair do programa')
escolha = int(input('Insira sua escolha: '))

while(escolha > 3 or escolha < 1):
    print(escolha)
    #Escolha errada
    if escolha > 3 or escolha < 1:
        print('Desculpe o valor inserido não é um valor aceito pelo sistema.')
        print('Os valores aceitos são:\n1- Inserir crimes\n2- Utilizar crimes já registrados\n3- Sair do programa')
        escolha = int(input('Insira sua escolha novamente: '))

#Escolha 1 #TODO Verificar o que devera ser inserido
if escolha == 1:
    qtdCrimes = int(input(('Insira a quantidade de crimes que deseja registrar: ')))

    for i in range(qtdCrimes):
        print('Registro ', i)
        viatura = greed.greed([T.trabalho(
        int(input('Começo do crime: ')),
        float(input('Final do crime: ')),
        float(input('Prioridade do crime: ')),
        input('Tipo de crime: '))])
        print('\n')

#Escolha 2
elif escolha == 2:
    print('Dentre os Crimes que podem ser cometidos e que foram registrados estão:\n1- Furto de veículos\n2- Roubo a instituição financeira\n3- Roubo deveículo\n4- Roubo de carga\n5- Tentativa de Homicídio\n6- Tráfico de drogas\n7- Latrocínio\n8- Homicídio doloso\n9- Sequestro\n10- Vandalismo\n11- Dano ao patrimônio público')

    viatura = greed.greed([T.trabalho(0, 15, 15, "Furto de veículos"), T.trabalho(2, 16, 10,"Roubo à instituição financeira"),  T.trabalho(2, 17,10, "Roubo deveículo"), T.trabalho(2, 18,10, "Roubo de carga"), T.trabalho(18, 22, 10, "Tentativa de Homicídio"), T.trabalho(18, 22,10, "Tráfico de drogas"), T.trabalho(14, 20, 27, "Latrocínio"), T.trabalho(18, 20,10, "Homicídio doloso"), T.trabalho(18, 20,10, "Sequestro"), T.trabalho(20, 21,10, "Vandalismo"), T.trabalho(21, 22,10, "Dano ao patrimônio público")])

    print('Quantidade de viaturas necessarias:' , viatura.intervalParti())
    viatura.intervalSchWei()

    for index, lista in enumerate(viatura.final):
        print(f"Viatura {index+1} - ", end = "")
        for j in lista:
            print(j.nome, end=" ")
        print()

else:
    print('Obrigado por usar nosso algoritmo! Até logo! :)')

    # Programação Dinâmica

    # for i in crimes:
    #     print('Tipo de Crime: ' + i)
    #     viatura = greed.greed([T.trabalho(
    #     int(input('Começo do crime: ')),
    #     float(input('Final do crime: ')),
    #     float(input('Prioridade do crime: ')),
    #     i)])
    #     print('\n')

    # teste = greed.greed([T.trabalho(0, 15, 15, "A"), T.trabalho(2, 16, 10,"B"),  T.trabalho(2, 17,10, "C"), T.trabalho(2, 18,10, "D"), T.trabalho(18, 22, 10, "E"), T.trabalho(18, 22,10, "F"), T.trabalho(14, 20, 27, "G"), T.trabalho(18, 20,10, "H"), T.trabalho(18, 20,10, "I"), T.trabalho(20, 21,10, "J"), T.trabalho(21, 22,10, "J"), T.trabalho(22, 23,10, "J"), T.trabalho(23, 24,10, "J"), T.trabalho(24, 25,10, "J")])



    # g.intervalParti()

    # print(viatura.intervalParti())
    # print(viatura.intervalSchWei())

    # Resultado Final
    # print('Quantidade de viaturas necessarias:' , teste.intervalParti())
    # teste.intervalSchWei()

   

    # for index, lista in enumerate(teste.final):
    #     print(f"{index} - ", end = "")
    #     for j in lista:
    #         print(j.nome, end=" ")
    #     print()

   