import flet as ft

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page setup
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT

        # controller placeholder
        self._controller = None

        # UI elements
        self._title = None
        self.dropdown_borgo = None
        self.btn_crea_grafo = None
        self.btn_analisi_archi = None
        self.txt_result = None

    def load_interface(self):
        # Titolo aggiornato
        self._title = ft.Text("Esame WiFi", color="blue", size=24)
        self._page.controls.append(self._title)

        # Dropdown Borgo B
        self.dropdown_borgo = ft.Dropdown(
            label="Borgo B",
            width=200,
            options=[]  # verranno aggiunte dinamicamente dal controller
        )

        # Pulsante Crea Grafo
        self.btn_crea_grafo = ft.ElevatedButton(
            text="Crea Grafo",
            on_click=self._controller.handle_crea_grafo
        )

        # Pulsante Analisi Archi
        self.btn_analisi_archi = ft.ElevatedButton(
            text="Analisi Archi",
            on_click=self._controller.handle_analisi_archi
        )

        row1 = ft.Row(
            [self.dropdown_borgo, self.btn_crea_grafo, self.btn_analisi_archi],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self._controller.fillDD()
        self._page.controls.append(row1)

        # Lista risultati
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
