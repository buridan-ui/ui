import reflex as rx
from typing import Optional
from reflex.vars import Var
from src.utils.twmerge import cn


def avatar(
    src: Optional[str] = None,
    alt: str = "",
    fallback: Optional[str] = None,
    class_name: str | Var = "",
    **props,
):
    base_avatar = "relative flex size-8 shrink-0 overflow-hidden rounded-full"
    image_styles = "aspect-square size-full object-cover"
    fallback_styles = (
        "bg-[var(--muted)] flex size-full items-center justify-center "
        "rounded-full text-sm font-medium"
    )

    if src:
        content = rx.image(
            src=src,
            alt=alt,
            data_slot="avatar-image",
            class_name=image_styles,
        )
    elif fallback:
        content = rx.el.div(
            fallback,
            data_slot="avatar-fallback",
            class_name=fallback_styles,
        )
    else:
        content = rx.el.div()

    return rx.el.div(
        content,
        data_slot="avatar",
        class_name=cn(base_avatar, class_name),
        **props,
    )
