# Import
from utils.greed import greed
from utils import trabalho as T
# Contexto
print('Bem-vindo ao NOMEDOTRABALHO, seu funcionamento se baseia em uma central que recebe uma lista de crimes cometidos e utilizando de Programação Dinâmica estabelece uma prioridade de atendimentos, além disso utiliza-se também de Interval Partitioning para saber a quantidade de viaturas que estarão em serviço no dia.')

#Crimes
print('Dentre os Crimes que podem ser cometidos estão:\n1- Furto de veículos\n2- Roubo a instituição financeira\n3- Roubo de veículo\n4- Roubo de carga\n5- Tentativa de Homicídio\n6- Tráfico de drogas\n7- Latrocínio\n8- Homicídio doloso\n9- Sequestro\n10- Vandalismo\n11- Dano ao patrimônio público')

print('\nSeu objetivo é estabelecer o horário a duração de um crime, começo e fim, bem como a prioridade que aquele crime detém, para que o algoritmo possa fornecer as informações necessárias às viaturas')

crimes = ['Furto de veículos', 'Roubo à instituição financeira', 'Roubo de veículo', 'Roubo de carga', 'Tentativa de Homicídio', 'Tráfico de drogas', 'Latrocínio', 'Homicídio doloso', 'Sequestro', 'Vandalismo', 'Dano ao patrimônio público']

print('\n')

# Programação Dinâmica

for i in crimes:
    print('Tipo de Crime: ' + i)
    viatura = greed([T.trabalho(
    int(input('Começo do crime: ')),
    float(input('Final do crime: ')),
    float(input('Prioridade do crime: ')),
    i)])
    print('\n')

# g = greed([T.trabalho(0, 15, 15, "A"), T.trabalho(2, 16, 10,"B"),  T.trabalho(2, 17,10, "C"), T.trabalho(2, 18,10, "D"), T.trabalho(18, 22, 10, "E"), T.trabalho(18, 22,10, "F"), T.trabalho(14, 20, 27, "G"), T.trabalho(18, 20,10, "H"), T.trabalho(18, 20,10, "I"), T.trabalho(20, 21,10, "J"), T.trabalho(21, 22,10, "J"), T.trabalho(22, 23,10, "J"), T.trabalho(23, 24,10, "J"), T.trabalho(24, 25,10, "J")])

print(viatura.intervalParti())
print(viatura.intervalSchWei())

# Resultado Final