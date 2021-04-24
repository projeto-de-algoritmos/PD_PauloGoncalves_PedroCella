import trabalho as T
import numpy as np

class greed:
    def __init__(self, ListaDeTarefas:list) -> None:
        self.listaDeTarefas = ListaDeTarefas
        self.jobs = np.full((self.intervalParti(ListaDeTarefas), len(ListaDeTarefas)), -1, dtype="int32")
        

    def intervalParti(self, ListaDeTarefas: list) -> int:
        ListaDeTarefas.sort(key=lambda x: x.comeco)

        conjTarefas = np.array([ListaDeTarefas[0].final], dtype="float")
        
        for currJob in ListaDeTarefas[1::]:

            result = np.where(conjTarefas <= currJob.comeco)

            if result[0].size:
                conjTarefas[result[0][0]] = currJob.final
            else:
                conjTarefas = np.append(conjTarefas, currJob.final)
                
        return len(conjTarefas)


    def intervalSchWei(self, ListaDeTarefas: list):
        raise NotImplemented



g = greed([T.trabalho(0, 15, "Ola"), T.trabalho(2, 16, "A"),  T.trabalho(2, 17, "A"), T.trabalho(2, 18, "A"), T.trabalho(18, 20, "A"), T.trabalho(18, 20, "A"), T.trabalho(18, 20, "A"), T.trabalho(18, 20, "A"), T.trabalho(18, 20, "A")])


print(g.intervalParti(g.listaDeTarefas))