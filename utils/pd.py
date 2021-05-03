from utils import trabalho as T
import numpy as np

class pahtJobs:
    def __init__(self) -> None:
        self.jobs = []
        self.total = 0.0


class pd:
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

            for i in self.listaDeTarefas:
                print(str(k) + " "+i.nome)

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
            
        for index, lista in enumerate(self.final):
            print(f"Viatura {index+1} - ", end = "")
            for j in lista:
                print(j.nome, end=" ")
            print()

        return self.final # Return [[tarefa, tarefa], [tarefa], [tarefa, tarefa], [tarefa, tarefa]]
        
