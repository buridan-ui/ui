import reflex as rx


def background_v1():
    return rx.center(
        rx.heading("Buridan UI", size="8", weight="bold"),
        background_size="20px 20px",
        background_image="radial-gradient(circle, hsl(0, 0%, 39%) 1px, transparent 1px)",
        mask="radial-gradient(50% 100% at 50% 50%, hsl(0, 0%, 0%, 1), hsl(0, 0%, 0%, 0))",
        width="100%",
        height="65vh",
    )
