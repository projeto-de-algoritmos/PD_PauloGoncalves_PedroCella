from numpy.lib.function_base import select
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

        # linhas, colunas = (self.intervalParti(), len(ListaDeTarefas) + 1)
        # self.jobs = [[T.trabalho(0,0,0)] * colunas] * linhas
        

    def intervalParti(self) -> int:
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
        esq = 0
        dire = index - 1

        while esq <= dire:
            meio = np.right_shift(dire + esq, 1) # Divisão por 2 fazendo bit sift para a direita 1x

            if self.listaDeTarefas[meio].final <= self.listaDeTarefas[index].comeco:
                if self.listaDeTarefas[meio + 1].final <= self.listaDeTarefas[index].comeco:
                    esq = meio + 1
                else:
                    return meio
            else:
                dire = meio - 1

        return None
    
    def intervalSchWei(self):

        # for k in 
        self.listaDeTarefas.sort(key=lambda x: x.final)
        caminhosPossiveis = []
        
        for i in range(0, len(self.listaDeTarefas)):
            caminhosPossiveis.append(pahtJobs())

        caminhosPossiveis[0].total = self.listaDeTarefas[0].prioridade
        caminhosPossiveis[0].jobs.append(self.listaDeTarefas[0])

        for i in range(1, len(self.listaDeTarefas)):
            tmpTotal = self.listaDeTarefas[i].prioridade
            indexJob = self.computeP(i)

            if indexJob != None:
                tmpTotal += caminhosPossiveis[indexJob].total
            
            if tmpTotal > caminhosPossiveis[i - 1].total and indexJob != None:
                caminhosPossiveis[i].total = tmpTotal

                caminhosPossiveis[i].jobs = caminhosPossiveis[indexJob].jobs
                caminhosPossiveis[i].jobs.append(self.listaDeTarefas[i])
            else:
                caminhosPossiveis[i] = caminhosPossiveis[i - 1]

            
        for i in caminhosPossiveis[8].jobs:
            print(i.nome)
            self.listaDeTarefas.pop(self.listaDeTarefas.index(i))
        print(self.listaDeTarefas)

g = greed([T.trabalho(0, 15, 15, "A"), T.trabalho(2, 16, 10,"B"),  T.trabalho(2, 17,10, "C"), T.trabalho(2, 18,10, "D"), T.trabalho(18, 20,10, "E"), T.trabalho(18, 20,10, "F"), T.trabalho(16, 20, 27, "G"), T.trabalho(18, 20,10, "H"), T.trabalho(18, 20,10, "I")])


g.intervalSchWei()
