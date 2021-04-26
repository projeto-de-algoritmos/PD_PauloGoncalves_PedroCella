# Import

# Contexto
print('Bem-vindo ao NOMEDOTRABALHO, seu funcionamento se baseia em uma central que recebe uma lista de crimes cometidos e utilizando de Programação Dinâmica estabelece uma prioridade de atendimentos, além disso utiliza-se também de Interval Partitioning para saber a quantidade de viaturas que estarão em serviço no dia.')

#Crimes
print('Dentre os Crimes que podem ser cometidos estão:\n1- Furto de veículos\n2- Roubo a instituição financeira\n3- Roubo de veículo\n4- Roubo de carga\n5- Tentativa de Homicídio\n6- Tráfico de drogas\n7- Latrocínio\n8- Homicídio doloso\n9- Sequestro\n10- Vandalismo\n11- Dano ao patrimônio público')

print('Seu objetivo é estabelecer o peso de cada crime, para que o algoritmo possa fornecer a prioridade às viaturas')

crimes = ['Furto de veículos', 'Roubo à instituição financeira', 'Roubo de veículo', 'Roubo de carga', 'Tentativa de Homicídio', 'Tráfico de drogas', 'Latrocínio', 'Homicídio doloso', 'Sequestro', 'Vandalismo', 'Dano ao patrimônio público']

porcentagem = []

for i in crimes:
    valor = int(input(f"O valor para o crime {i} é: "))
    porcentagem.append(valor)
    
# Programação Dinâmica

# Resultado Final