import reflex as rx


def background_v4():
    return rx.box(
        rx.box(
            background_size="20px 20px",
            background_image="radial-gradient(circle, hsl(0, 0%, 39%) 1px, transparent 1px), radial-gradient(circle, hsl(0, 0%, 45%) 1px, transparent 1px)",
            mask="linear-gradient(to bottom, hsl(0, 0%, 0%, 0.5), hsl(0, 0%, 0%, 0))",
            width="100%",
            height="65vh",
        ),
        rx.center(
            rx.heading("Buridan UI", size="7", weight="bold", z_index="20"),
            position="absolute",
            top="50%",
            left="50%",
            transform="translate(-50%, -50%)",
        ),
        width="100%",
        height="65vh",
        position="relative",
    )
