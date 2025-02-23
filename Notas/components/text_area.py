import reflex as rx

class FormInputState(rx.State):
    form_data: dict = {}
    view_data_note: list = []
    count: int = 0

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        self.count += 1
        for register in self.form_data:
            self.view_data_note.append(register)
        print(self.view_data_note.values())

def form_input1():
    return rx.card(
        rx.vstack(
            rx.heading("crear notas"),
            rx.form.root(
                rx.hstack(
                    rx.input(
                        name="input",
                        placeholder="Ingresa el texto...",
                        type="text",
                        required=True,
                    ),
                    rx.button("Enviar", type="submit"),
                    width="100%",
                ),
                on_submit=FormInputState.handle_submit,
                reset_on_submit=True,
            ), 
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell(""),
                    ),
                ),
            rx.table.body(
                rx.table.row(
                    #Mustra la informacion de la nota en pantalla
                    rx.table.row_header_cell(f"{FormInputState.form_data.values()}"),
                ),
            ),
    width="100%",
            ),
    width="100%",
        ),
    ),
    align_items="left",
    width="100%",



