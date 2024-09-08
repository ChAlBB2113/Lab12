import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodi=[]
        self._archi=[]
        self._grafo=nx.Graph()

    def ottieniNazioni(self):
        return DAO.ottieniNazioni()

    def ottineiDizRetailersCodeName(self):
        return DAO.ottineiDizRetailersCodeName()

    def creaGrafo(self, nazione, anno):
        self._nodi.clear()
        self._archi.clear()
        self._grafo.clear()

        self._nodi=DAO.ottieniNodi(nazione)
        self._grafo.add_nodes_from(self._nodi)

        self._archi=DAO.ottieniArchi(nazione, anno)
        for tupla in self._archi:
            self._grafo.add_edge(tupla[0], tupla[1], weight=tupla[2])

