from operator import itemgetter

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        self._view.ddyear.options.clear()
        self._view.ddcountry.options.clear()
        self._view.ddyear.options.append(ft.dropdown.Option(f"2015"))
        self._view.ddyear.options.append(ft.dropdown.Option(f"2016"))
        self._view.ddyear.options.append(ft.dropdown.Option(f"2017"))
        self._view.ddyear.options.append(ft.dropdown.Option(f"2018"))
        listaNazioni=self._model.ottieniNazioni()
        for nazione in listaNazioni:
            self._view.ddcountry.options.append(ft.dropdown.Option(f"{nazione}"))





    def handle_graph(self, e):
        anno=self._view.ddyear.value
        nazione=self._view.ddcountry.value
        if anno=="" or anno==None or anno=="Anno":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Seleziona un anno"))
            self._view.update_page()
            return
        if nazione=="" or nazione==None or nazione=="Nazione":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Seleziona una Nazione"))
            self._view.update_page()
            return

        self._model.creaGrafo(nazione, anno)

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {len(self._model._grafo.nodes())}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero archi: {len(self._model._grafo.edges())}"))

        self._view.update_page()








    def handle_volume(self, e):
        self._view.txtOut2.controls.clear()
        dizRetailerVolume = {}
        for vertice in self._model._grafo.nodes():
            listaVicini = list(self._model._grafo.neighbors(
                vertice))  # devo trasformarla in una lista il contenitore di vicini ottenuti con metodo neighbors
            dizRetailerVolume[vertice] = 0  # in elenco si vuole tutti i retailers anche quelli con volume nullo
            for vicino in listaVicini:
                dizRetailerVolume[vertice] += self._model._grafo[vertice][vicino]['weight']

        DizRetailersCodeName = self._model.ottineiDizRetailersCodeName()
        # per stampare il nome e no il codice del retail....dovuto fin ora lavorare col codice perchè quello c'era il tabella go_daily_sales
        # e non il nome

        # voglio elenco retailers per volume decrescente quindi devo ordinare dizionare sui valori....
        # non si puo fare, allora dizionario che mi è stato utile per formare struttura dati, visto che facile chiamare coppie
        # chiave valore data una chiave, ora lo trasformo in una lista di tuple facile da ordinare
        listaTupleRetailerVolume = sorted(dizRetailerVolume.items())
        # e ordino quella lista di tuple in base a valore in posizione 1 delle tuple
        listaTupleRetailerVolume.sort(key=itemgetter(1),
                                      reverse=True)  # reverse perche voglio ordine decr, dal piu alto al piu basso
        for tupla in listaTupleRetailerVolume:
            self._view.txtOut2.controls.append(ft.Text(f"{DizRetailersCodeName[tupla[0]]}-->{tupla[1]}"))

        DizRetailersCodeName = self._model.ottineiDizRetailersCodeName()

        self._view.update_page()


    def handle_path(self, e):
        pass
