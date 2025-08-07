import reflex as rx


def blip():
    return rx.box(
        width="10px",
        height="10px",
        border_radius="10px",
        background=rx.color("blue"),
        position="absolute",
        left="-5px",
    )


def wrapper(
    title: str,
    instructions: str,
    components: list[rx.Component] = [],
    **kwargs,
):
    return rx.hstack(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    blip(),
                    rx.text(
                        title,
                        size="1",
                        weight="medium",
                        color=rx.color("slate", 11),
                    ),
                    align="center",
                ),
                rx.text(
                    instructions,
                    size="3",
                    weight="bold",
                    color=rx.color("slate", 12),
                ),
                spacing="1",
            ),
            *components,
        ),
        width="100%",
        align="start",
        justify="start",
        padding_left="15px",
        border_radius="0px 5px 5px 0px",
        **kwargs,
    )


def timeline_v1():
    return rx.vstack(
        rx.vstack(
            rx.box(
                wrapper(
                    "2023 - Present",
                    "Web Designer & Web Developer",
                    [
                        rx.text(
                            "The company has high expectations, and by using OKRs (Objectives and Key Results), there is a mutual understanding of expectations and performance. This framework not only aligns individual and team goals with the company's strategic vision but also fosters accountability and transparency throughout the organization.Regular check-ins and progress updates ensure that everyone stays on track, allowing for timely adjustments when necessary. The collaborative nature of setting OKRs encourages open communication, enabling team members to share insights and challenges.",
                            size="1",
                        ),
                    ],
                ),
                position="relative",
            ),
            rx.box(
                wrapper(
                    "2021 - 2023",
                    "Senior Software Engineer at Mailchimp",
                    [
                        rx.text(
                            "This is an excellent company and they reward their employees. It's becoming a big company but it's still private, so the culture is as good as it gets at 1,000+ employees if you ask me. Managers are still adapting to the growth I think, but everyone has to. Great place to work. ",
                            size="1",
                        ),
                    ],
                ),
                position="relative",
            ),
            rx.box(
                wrapper(
                    "2021 - 2021",
                    "Junior Software Engineer at Slack",
                    [
                        rx.text(
                            "Work in Slack is one of the beautiful experience I can do in my entire life. There are a lot of interesting thing to learn and manager respect your time and your personality.",
                            size="1",
                        ),
                    ],
                ),
                position="relative",
            ),
            width="100%",
            border_left=f"1px solid {rx.color('gray', 5)}",
            spacing="7",
        ),
        width="100%",
        max_width="40em",
        align="center",
        justify="start",
        padding="24px 12px",
        overflow="auto",
    )
