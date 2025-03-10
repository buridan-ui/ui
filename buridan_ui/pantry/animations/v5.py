import asyncio
from random import randint

import reflex as rx

number_list: list[str] = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
]


class Numbers(rx.State):
    is_disabled: bool = False

    one: str = "_"
    two: str = "_"
    three: str = "_"
    four: str = "_"

    five: str = "_"
    six: str = "_"
    seven: str = "_"
    eight: str = "_"

    nine: str = "_"
    ten: str = "_"
    eleven: str = "_"
    twelve: str = "_"

    async def show_number(self, place_name: str):
        for _ in range(35):
            number = str(randint(0, 9))
            setattr(self, place_name, number)
            yield
            await asyncio.sleep(0.061)

    async def run_numbers(self):
        self.is_disabled = True
        yield
        tasks = [self.show_number(number) for number in number_list]

        for _ in range(35):
            await asyncio.gather(*[task.__anext__() for task in tasks])
            yield

        self.is_disabled = False


def animation_v5():
    return rx.hstack(
        rx.hstack(
            *[rx.heading(getattr(Numbers, number)) for number in number_list[:4]]
        ),
        rx.hstack(
            *[rx.heading(getattr(Numbers, number)) for number in number_list[4:8]]
        ),
        rx.hstack(
            *[rx.heading(getattr(Numbers, number)) for number in number_list[8:12]]
        ),
        rx.button(
            "Run",
            top="-24px",
            right="-12px",
            cursor="pointer",
            position="absolute",
            loading=Numbers.is_disabled,
            radius="none",
            on_click=Numbers.run_numbers,
            variant="surface",
            size="1",
        ),
        font_size="15px",
        width="100%",
        height="30vh",
        align="center",
        justify="center",
        position="relative",
        wrap="wrap",
        spacing="6",
    )
