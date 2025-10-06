import reflex as rx
from typing import Optional


def avatar(
    src: Optional[str] = None,
    alt: str = "",
    fallback: Optional[str] = None,
    class_name: str = "",
    **props,
):
    base_classes = "relative flex size-8 shrink-0 overflow-hidden rounded-full"

    if src:
        content = rx.image(
            src=src,
            alt=alt,
            data_slot="avatar-image",
            class_name="aspect-square size-full object-cover",
        )
    elif fallback:
        content = rx.box(
            fallback,
            data_slot="avatar-fallback",
            class_name="bg-[var(--muted)] flex size-full items-center justify-center rounded-full text-sm font-medium",
        )
    else:
        content = rx.box()

    return rx.box(
        content,
        data_slot="avatar",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )
