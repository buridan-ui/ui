import reflex as rx
from buridan_ui.export import export_app

app = rx.App(
    stylesheets=["css/globals.css"],
    head_components=[
        rx.script(
            src="https://gc.zgo.at/count.js",
            custom_attrs={
                "data-goatcounter": "https://buridan-ui.goatcounter.com/count",
            },
        )
    ],
)
export_app(app)
