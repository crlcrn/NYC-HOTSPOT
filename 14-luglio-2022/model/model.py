import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._nodi = []

    def build_graph(self, borgo):
        self._grafo.clear()
        self._nodi = DAO.get_nodi(borgo)

        self._grafo.add_nodes_from(self._nodi)

        archi = DAO.get_archi(borgo)
        for n1, n2, peso in archi:
            self._grafo.add_edge(n1, n2, weight = peso)

    def get_archi_superiore_media(self):

        if self._grafo is None or self._grafo.number_of_edges() == 0:
         return []

        somma_pesi = 0
        numero_archi = 0

        for u,v in self._grafo.edges:
            peso = self._grafo[u][v]['weight']
            somma_pesi += peso
            numero_archi += 1

        media = somma_pesi / numero_archi

        archi_filtrati = []
        for u, v in self._grafo.edges:
            peso = self._grafo[u][v]['weight']
            if peso > media:
                archi_filtrati.append((u,v,peso))


        archi_ordinati = sorted(archi_filtrati, key=lambda arco: arco[2], reverse=True)

        return media, archi_ordinati

    def getDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)