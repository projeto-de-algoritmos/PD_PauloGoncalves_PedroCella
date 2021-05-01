from numpy.lib.function_base import select
import trabalho as T
import numpy as np

class greed:
    def __init__(self, ListaDeTarefas:list) -> None:
        self.listaDeTarefas = ListaDeTarefas
        self.jobs = np.full((self.intervalParti(), len(ListaDeTarefas) + 1), T.trabalho(0,0,0), dtype="object")
        self.jobs[:,-1] = 0

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
        testE = []
        testD = []
    

        for i in self.listaDeTarefas:
            testE.append(i.final)
            testD.append(i.comeco)

        
        # print(f"{self.listaDeTarefas[index].nome} {index} - {esq + (dire - esq) // 2} {testD} {testE}")


        while esq <= dire:
            meio = np.right_shift(dire + esq, 1)

            if self.listaDeTarefas[meio].final <= self.listaDeTarefas[index].comeco:
                if self.listaDeTarefas[meio + 1].final <= self.listaDeTarefas[index].comeco:
                    esq = meio + 1
                else:
                    return meio
            else:
                dire = meio - 1

        return None
    
    def intervalSchWei(self):

        for k in range(0, self.intervalParti()):
            self.listaDeTarefas.sort(key=lambda x: x.final)
            
            self.jobs[k, 0] = self.listaDeTarefas[0]
            self.jobs[k, -1] = self.listaDeTarefas[0].prioridade

            for i in range(1, len(self.listaDeTarefas)):

                tmpJob = self.listaDeTarefas[i]
                self.jobs[k, -1] = self.listaDeTarefas[i].prioridade

                P = self.computeP(i)
                if P:
                 self.jobs[k, -1] += self.jobs[k, P].prioridade




g = greed([T.trabalho(0, 15, 15, "A"), T.trabalho(2, 16, 10,"B"),  T.trabalho(2, 17,10, "C"), T.trabalho(2, 18,10, "D"), T.trabalho(18, 20,10, "E"), T.trabalho(18, 20,10, "F"), T.trabalho(18, 20,27, "G"), T.trabalho(18, 20,10, "H"), T.trabalho(18, 20,10, "I")])


g.intervalSchWei()
