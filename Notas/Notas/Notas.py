import reflex as rx

#PAGES
from pages.home import home
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index()-> rx.Component:
    return rx.contaiiner(
            home()
    )
app = rx.App()
app.add_page(index)
