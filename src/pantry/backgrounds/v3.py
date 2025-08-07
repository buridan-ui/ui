import reflex as rx


def background_v3():
    return rx.box(
        rx.box(
            background_size="18px 18px",
            background_image=f"radial-gradient(circle, {rx.color('indigo', 7)} 1px, transparent 1px), radial-gradient(circle, {rx.color('indigo', 10)} 1px, transparent 1px), radial-gradient(circle, {rx.color('indigo', 12)} 1px, transparent 1px)",
            mask="radial-gradient(50% 100% at 50% 100%, hsl(0, 0%, 0%, 1), hsl(0, 0%, 0%, 0))",
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
