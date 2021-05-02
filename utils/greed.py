
import trabalho as T
import numpy as np

class pahtJobs:
    def __init__(self) -> None:
        self.jobs = []
        self.total = 0


class greed:
    def __init__(self, ListaDeTarefas:list) -> None:
        self.listaDeTarefas = ListaDeTarefas
        self.final = []

    def intervalParti(self) -> int:
        """
        Função para poder retornar qual o minimo para poder fazer todas as tarefas.
        """
        self.listaDeTarefas.sort(key=lambda x: x.comeco)

        conjTarefas = np.array([self.listaDeTarefas[0].final], dtype="float")
        
        for currJob in self.listaDeTarefas[1::]:

            result = np.where(conjTarefas <= currJob.comeco)

            if result[0].size:
                conjTarefas[result[0][0]] = currJob.final
            else:
                conjTarefas = np.append(conjTarefas, currJob.final)
    
        return len(conjTarefas)

    def computeP(self, index) -> int:
        """
        Função para retornar o indice, da maior tarefa que é compativel com o indice inicial.
        """
        for i in range(index, -1, -1): # TODO: Busca Binaria, para poder achar.
            if self.listaDeTarefas[i].final <= self.listaDeTarefas[index].comeco:
                return i
        return None

    def intervalSchWei(self):

        for k in range(0, self.intervalParti()): # For para poder repetir X quantidades de vezes nas quais vão ser necessarias, para terminat todas as tarefas.
            self.listaDeTarefas.sort(key=lambda x: x.final)
            caminhosPossiveis = [] 

            for i in range(0, len(self.listaDeTarefas)): # Inicialização
                caminhosPossiveis.append(pahtJobs())
            
            # Set da primeira escolha sendo o primeiro trabalho.
            caminhosPossiveis[0].total = self.listaDeTarefas[0].prioridade
            caminhosPossiveis[0].jobs.append(self.listaDeTarefas[0])

            for i in range(1, len(self.listaDeTarefas)):

                tmpTotal = self.listaDeTarefas[i].prioridade # A prioridade temporaria
                indexJob = self.computeP(i) # Pegando o maior trabalho compativel, com o trabalho I.

                if indexJob != None: # Caso ache algum trabalho, adicione na prioridade temporaria.
                    tmpTotal += caminhosPossiveis[indexJob].total

                if tmpTotal > caminhosPossiveis[i - 1].total: # Caso a nova prioridade seja maior que a escolha anterior.
                    caminhosPossiveis[i].total = tmpTotal

                    if indexJob != None: 
                        caminhosPossiveis[i].jobs = caminhosPossiveis[indexJob].jobs

                    caminhosPossiveis[i].jobs.append(self.listaDeTarefas[i])

                else: # Se não, a nova escolha continua sendo a mesma que a anterior.
                    caminhosPossiveis[i] = caminhosPossiveis[i - 1]

            for i, obj in enumerate(caminhosPossiveis[len(self.listaDeTarefas) - 1].jobs): # Retirando as tarefas ja escolhidas.
                self.listaDeTarefas.pop(self.listaDeTarefas.index(obj))

            self.final.append(caminhosPossiveis[len(self.listaDeTarefas) - 1].jobs)

        return self.final # Return [[tarefa, tarefa], [tarefa], [tarefa, tarefa], [tarefa, tarefa]]
        

g = greed([T.trabalho(0, 15, 15, "A"), T.trabalho(2, 16, 10,"B"),  T.trabalho(2, 17,10, "C"), T.trabalho(2, 18,10, "D"), T.trabalho(18, 22, 10, "E"), T.trabalho(18, 22,10, "F"), T.trabalho(14, 20, 27, "G"), T.trabalho(18, 20,10, "H"), T.trabalho(18, 20,10, "I"), T.trabalho(20, 21,10, "J"), T.trabalho(21, 22,10, "J"), T.trabalho(22, 23,10, "J"), T.trabalho(23, 24,10, "J"), T.trabalho(24, 25,10, "J")])

print(g.intervalParti())
print(g.intervalSchWei())
