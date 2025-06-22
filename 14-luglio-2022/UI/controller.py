import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):

        borgo = DAO.get_borgo()
        for b in borgo:
            self._view.dropdown_borgo.options.append(ft.dropdown.Option(f'{b}'))

        self._view.update_page()

    def handle_crea_grafo(self, e):

        borgo = self._view.dropdown_borgo.value

        self._model.build_graph(borgo)

        nNodes, nEdges = self._model.getDetails()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text(f"Grafo correttamente creato. Il grafo ha {nNodes} nodi e {nEdges} archi."))


        self._view.update_page()

    def handle_analisi_archi(self, e):
        risultato = self._model.get_archi_superiore_media()
        self._view.txt_result.controls.clear()

        if risultato is None:
            self._view.create_alert("Il grafo non contiene archi.")
            return

        media, archi = risultato
        self._view.txt_result.controls.append(ft.Text(f"Peso medio: {media:.2f}"))

        for u, v, peso in archi:
            self._view.txt_result.controls.append(
                ft.Text(f"{u} - {v}  |  Peso: {peso:.2f}")
            )

        self._view.update_page()
