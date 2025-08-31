import reflex as rx
from reflex.plugins.shared_tailwind import TailwindConfig

tailwind_config = TailwindConfig(
    plugins=["@tailwindcss/typography"],
    theme={
        "extend": {
            "colors": {
                "background": "var(--background)",
                "foreground": "var(--foreground)",
            },
        }
    },
)

config = rx.Config(
    app_name="src",
    plugins=[rx.plugins.TailwindV4Plugin(config=tailwind_config)],
    show_built_with_reflex=False,
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)
