from reflex.experimental import ClientStateVar

# Var holding component library value
component_library = ClientStateVar.create("component_library", "Base UI")

# Var holding the current theme
theme = ClientStateVar.create("theme", "neutral")

# Var holding the current theme
font_family = ClientStateVar.create("font_family", "Inter")
