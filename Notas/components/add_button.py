import reflex as rx

def add_button(text: str) -> rx.Component:
    return rx.button(
        text,
        color_scheme="cyan",
        variant="classic",
        #on_click=view_info  # asigna la función de manejo de clic
    )

