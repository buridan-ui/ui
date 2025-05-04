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
    app_name="buridan_ui",
    tailwind=tailwind_config,
    show_built_with_reflex=False,
)
