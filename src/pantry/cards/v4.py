import reflex as rx


def card_v4():
    return rx.box(
        rx.box(
            color=rx.color("gray", 4),
            class_name=(
                "w-full h-12 "
                + "col-start-2 row-span-full row-start-1 bg-[size:10px_10px] bg-fixed bg-[image:repeating-linear-gradient(315deg,currentColor_0,currentColor_1px,_transparent_0,_transparent_50%)]"
            ),
        ),
        rx.divider(),
        rx.box(
            color=rx.color("gray", 4),
            class_name=(
                "w-full h-64 "
                + "col-start-2 row-span-full row-start-1 bg-[size:10px_10px] bg-fixed bg-[image:repeating-linear-gradient(315deg,currentColor_0,currentColor_1px,_transparent_0,_transparent_50%)]"
            ),
        ),
        rx.divider(),
        rx.box(
            color=rx.color("gray", 4),
            class_name=(
                "w-full h-12 "
                + "col-start-2 row-span-full row-start-1 bg-[size:10px_10px] bg-fixed bg-[image:repeating-linear-gradient(315deg,currentColor_0,currentColor_1px,_transparent_0,_transparent_50%)]"
            ),
        ),
        class_name=(
            "w-full max-w-[35em] "
            + "flex flex-col p-4 gap-y-2 "
            + "rounded-md border border-dashed border-gray-600 "
        ),
    )
