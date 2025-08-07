import reflex as rx

tailwind_config = {
    "plugins": ["@tailwindcss/typography"],
    "theme": {
        "extend": {
            "colors": {
                "background": "var(--background)",
                "foreground": "var(--foreground)",
                "border": "var(--border)",
                "pattern-ui": "var(--pattern-ui)",
                "pattern-lab": "var(--pattern-lab)",
            },
        }
    },
}

config = rx.Config(
    telemetry=False,
    app_name="src",
    tailwind=tailwind_config,
    plugins=[rx.plugins.TailwindV3Plugin()],
    show_built_with_reflex=False,
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)
