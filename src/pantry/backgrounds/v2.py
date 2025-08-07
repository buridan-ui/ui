import reflex as rx


def background_v2():
    return rx.center(
        rx.heading("Buridan UI", size="8", weight="bold", z_index="10"),
        background_size="100px 100px",
        background_image="linear-gradient(hsl(0, 0%, 39%) 1px, transparent 1px), linear-gradient(to right, transparent 99%, hsl(0, 0%, 39%) 100%)",
        mask="radial-gradient(50% 100% at 50% 50%, hsl(0, 0%, 0%, 1), hsl(0, 0%, 0%, 0))",
        width="100%",
        height="65vh",
    )
