import reflex as rx

def delete_button(text: str) -> rx.Component:
    return rx.button(text, color_scheme="cyan", variant="classic")
