import reflex as rx

tailwind_config = {
    "plugins": ["@tailwindcss/typography"],
    "theme": {
        "extend": {
            "colors": {
                "background": "var(--background)",
                "foreground": "var(--foreground)",
                "card": "var(--card)",
                "card-foreground": "var(--card-foreground)",
                "popover": "var(--popover)",
                "popover-foreground": "var(--popover-foreground)",
                "primary": "var(--primary)",
                "primary-foreground": "var(--primary-foreground)",
                "secondary": "var(--secondary)",
                "secondary-foreground": "var(--secondary-foreground)",
                "muted": "var(--muted)",
                "muted-foreground": "var(--muted-foreground)",
                "accent": "var(--accent)",
                "accent-foreground": "var(--accent-foreground)",
                "destructive": "var(--destructive)",
                "destructive-foreground": "var(--primary-foreground)",
                "border": "var(--border)",
                "input": "var(--input)",
                "ring": "var(--ring)",
                "chart-1": "var(--chart-1)",
                "chart-2": "var(--chart-2)",
                "chart-3": "var(--chart-3)",
                "chart-4": "var(--chart-4)",
                "chart-5": "var(--chart-5)",
                "sidebar": "var(--sidebar)",
                "sidebar-foreground": "var(--sidebar-foreground)",
                "sidebar-primary": "var(--sidebar-primary)",
                "sidebar-primary-foreground": "var(--sidebar-primary-foreground)",
                "sidebar-accent": "var(--sidebar-accent)",
                "sidebar-accent-foreground": "var(--sidebar-accent-foreground)",
                "sidebar-border": "var(--sidebar-border)",
                "sidebar-ring": "var(--sidebar-ring)",
                "pattern-ui": "var(--pattern-ui)",
                "pattern-lab": "var(--pattern-lab)",
            },
            "borderRadius": {
                "DEFAULT": "var(--radius)",
            },
        }
    },
}

config = rx.Config(
    app_name="buridan_ui",
    telemetry=False,
    show_built_with_reflex=False,
    tailwind=tailwind_config,
)
