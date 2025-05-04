import reflex as rx
from buridan_ui.export import export_app

app = rx.App(stylesheets=["css/globals.css"])
export_app(app)
