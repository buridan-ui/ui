import reflex as rx


def card_v1():
    return rx.box(
        rx.box(
            color=rx.color("gray", 4),
            class_name=(
                "w-full h-full "
                + "col-start-2 row-span-full row-start-1 bg-[size:10px_10px] bg-fixed bg-[image:repeating-linear-gradient(315deg,currentColor_0,currentColor_1px,_transparent_0,_transparent_50%)]"
            ),
        ),
        class_name=(
            "w-full h-72 max-w-[35em] "
            + "p-4 "
            + "rounded-md border border-dashed border-gray-600 "
        ),
    )
