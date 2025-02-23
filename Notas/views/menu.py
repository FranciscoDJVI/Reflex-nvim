import  reflex as rx

class DropdownMenu(rx.State):
    num_opens: int = 0
    opened: bool = False

    @rx.event
    def count_opens(self, value: bool):
        self.opened = value
        self.num_opens += 1


def dropdown_menu():
    return rx.flex(
        rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    "Options", variant="soft", size="2"
                ),
            ),
            rx.menu.content(
                rx.menu.item("Editar", shortcut="⌘ E"),
                rx.menu.item("Duplicar", shortcut="⌘ D"),
                rx.menu.separator(),
                rx.menu.item("Archivar", shortcut="⌘ N"),
                rx.menu.separator(),
                rx.menu.item(
                    "Eliminar", shortcut="⌘ ⌫", color="red"
                ),
            ),
            on_open_change=DropdownMenu.count_opens,
        ),
        direction="column",
        spacing="3",
    )
