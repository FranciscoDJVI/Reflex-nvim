import  reflex as rx

#Components
from components.tittle import principal_tittle
from components.text_area import form_input1

#Views
from views.menu import dropdown_menu

@rx.page("/", title="Home", description="Welcome to home page.")
def home() -> rx.Component:
    return rx.container(
        rx.text(
        dropdown_menu(),
        principal_tittle("Mis notas xpress")),
        form_input1(),
)
