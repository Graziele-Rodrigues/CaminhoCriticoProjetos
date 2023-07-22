from weightedGraph import WeightedGraph
import pandas as pd


class Functions:
    def __init__(self, file_path: str):
        self.table = pd.read_csv(file_path)
        self.graph = WeightedGraph(len(self.table["Código"]) + 2, adj_list=[])
        self.make_weightedgraph()

    def print_table(self):
        return self.table

    # ideia para montar o grafo: le o codigo da linha e depois procura na coluna de dependencias
    # se algum depende dele e faz a conexão
    def make_weightedgraph(self):
        # corrige os vazios para funcionar a indexação
        self.table["Dependências"] = self.table["Dependências"].fillna('NaN')
        # le o codigo por matéria
        for c in range(len(self.table["Código"])):
            # olha a linha c e o codigo dela
            cod = self.table["Código"][c]
            # procura se alguma das materias tem dep
            dep = self.table[self.table["Dependências"].str.contains(cod)]
            for i in dep.index:
                # cria a aresta no grafo com o peso 1
                self.graph.add_directed_edge(c + 1, i+1, 1)
            self.graph.add_directed_edge(c + 1, self.graph.node_count - 1, 1)
            if self.table["Dependências"][c] == 'NaN':
                self.graph.add_directed_edge(0, c+1, 0)
                
    def critical(self, path_critical: list):
        path_critical.remove(0)
        path_critical.remove(self.graph.node_count - 1)
        tempo = 0
        for i in path_critical:
            print('- ', self.table['Nome'][i-1])
            tempo = tempo+1

        print("Tempo Mínimo: ", tempo)
