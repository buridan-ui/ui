import reflex as rx
from ..button.button import button
from .drawer import (
    drawer_root,
    drawer_trigger,
    drawer_overlay,
    drawer_portal,
    drawer_content,
    drawer_title,
)


def drawer_demo():
    return drawer_root(
        drawer_trigger(
            button("Open Drawer", variant="outline"),
            as_child=True,
        ),
        drawer_portal(
            drawer_overlay(
                class_name="fixed inset-0 bg-black/40",
            ),
            drawer_content(
                rx.box(
                    rx.box(
                        class_name="mx-auto w-12 h-1.5 flex-shrink-0 rounded-full bg-gray-300 mb-8",
                        aria_hidden="true",
                    ),
                    rx.box(
                        drawer_title(
                            "Drawer for React.",
                            class_name="font-medium mb-4 text-gray-900",
                        ),
                        rx.text(
                            "This component can be used as a Dialog replacement on mobile and tablet devices. You can read about why and how it was built ",
                            rx.el.a(
                                "here",
                                href="https://emilkowal.ski/ui/building-a-drawer-component",
                                target="_blank",
                                class_name="underline",
                            ),
                            ".",
                            class_name="text-gray-600 mb-2",
                        ),
                        rx.text(
                            "This one specifically is the most simplest setup you can have, just a simple drawer with a trigger.",
                            class_name="text-gray-600 mb-2",
                        ),
                        class_name="max-w-md mx-auto",
                    ),
                    class_name="p-4 bg-white rounded-t-[10px] flex-1",
                ),
                # Footer
                rx.box(
                    rx.box(
                        rx.el.a(
                            "GitHub",
                            rx.html(
                                """<svg fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="16" aria-hidden="true" class="w-3 h-3 ml-1">
                                    <path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"></path>
                                    <path d="M15 3h6v6"></path>
                                    <path d="M10 14L21 3"></path>
                                </svg>"""
                            ),
                            href="https://github.com/emilkowalski/vaul",
                            target="_blank",
                            class_name="text-xs text-gray-600 flex items-center gap-0.25",
                        ),
                        rx.el.a(
                            "Twitter",
                            rx.html(
                                """<svg fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="16" aria-hidden="true" class="w-3 h-3 ml-1">
                                    <path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"></path>
                                    <path d="M15 3h6v6"></path>
                                    <path d="M10 14L21 3"></path>
                                </svg>"""
                            ),
                            href="https://twitter.com/emilkowalski_",
                            target="_blank",
                            class_name="text-xs text-gray-600 flex items-center gap-0.25",
                        ),
                        class_name="flex gap-6 justify-end max-w-md mx-auto",
                    ),
                    class_name="p-4 bg-gray-100 border-t border-gray-200 mt-auto",
                ),
                class_name="bg-gray-100 flex flex-col rounded-t-[10px] mt-24 h-fit fixed bottom-0 left-0 right-0 outline-none",
            ),
        ),
    )
