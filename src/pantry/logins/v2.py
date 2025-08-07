import reflex as rx


def login_button(name: str, *args, **kwargs) -> rx.button:
    return rx.button(
        *args,
        name,
        **kwargs,
        **{
            "flex": "1",
            "cursor": "pointer",
            "variant": "surface",
            "color_scheme": "gray",
        },
    )


def logins_v2():
    return rx.vstack(
        rx.vstack(
            rx.heading("Create an account", size="5", weight="bold"),
            rx.text(
                "Enter your email below to create your account",
                font_size="12px",
                weight="medium",
                color_scheme="gray",
            ),
            width="100%",
            spacing="1",
            align="center",
        ),
        rx.hstack(
            login_button("GitHub", rx.icon(tag="github", size=15)),
            login_button("Mail", rx.icon(tag="mail", size=15)),
            width="100%",
        ),
        rx.hstack(
            rx.divider(width="30%"),
            rx.text("OR CONTINUE WITH", font_size="10px", color_scheme="gray"),
            rx.divider(width="30%"),
            width="100%",
            align="center",
            justify="center",
            padding="5px 0px",
        ),
        rx.form(
            rx.vstack(
                rx.el.input(
                    placeholder="something@email.com",
                    class_name=(
                        "p-2 w-full "
                        + "text-sm "
                        + "rounded-md bg-transparent border border-gray-500/40 "
                        + "focus:outline-none focus:border-blue-500 shadow-sm"
                    ),
                    name="input",
                ),
                rx.el.input(
                    placeholder="password",
                    class_name=(
                        "p-2 w-full "
                        + "text-sm "
                        + "rounded-md bg-transparent border border-gray-500/40 "
                        + "focus:outline-none focus:border-blue-500 shadow-sm"
                    ),
                    name="password",
                    type="password",
                ),
                rx.button(
                    "Create Account",
                    width="100%",
                    cursor="pointer",
                    variant="surface",
                    color_scheme="gray",
                    type="submit",
                ),
                width="100%",
            ),
            on_submit=lambda data: rx.toast(
                f"You submitted the following data: {rx.Var.create(data).to_string()}"
            ),
        ),
        rx.text(
            "By clicking continue, you agree to our ",
            rx.text("Terms of Service", as_="u"),
            " and ",
            rx.text("Privacy Policy", as_="u"),
            ".",
            font_size="11px",
            color_scheme="gray",
            text_align="center",
            padding="5px 0px",
        ),
        width="100%",
        max_width="21em",
        height="100%",
        justify="center",
        align="center",
    )
