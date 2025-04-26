import reflex as rx


def card_v3():
    return rx.box(
        rx.box(
            color=rx.color("gray", 4),
            class_name=(
                # Dimesnions
                "w-full h-64 "
                # Placeholder Background
                + "col-start-2 row-span-full row-start-1 bg-[size:10px_10px] bg-fixed bg-[image:repeating-linear-gradient(315deg,currentColor_0,currentColor_1px,_transparent_0,_transparent_50%)]"
            ),
        ),
        rx.divider(),
        rx.box(
            color=rx.color("gray", 4),
            class_name=(
                # Dimesnions
                "w-full h-12 "
                # Placeholder Background
                + "col-start-2 row-span-full row-start-1 bg-[size:10px_10px] bg-fixed bg-[image:repeating-linear-gradient(315deg,currentColor_0,currentColor_1px,_transparent_0,_transparent_50%)]"
            ),
        ),
        class_name=(
            # Dimesnions
            "w-full max-w-[35em] "
            # Layout
            + "flex flex-col p-4 gap-y-2 "
            # Appearance
            + "rounded-md border border-dashed border-gray-600 "
        ),
    )
