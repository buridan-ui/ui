import reflex as rx

import src.comps.ui.stylesheet as themes
import src.hooks as hooks
from src.docs.library.base_ui.components.base.button import button
from src.docs.library.base_ui.components.base.dialog import dialog
from src.docs.library.base_ui.components.base.select import select
from src.docs.library.base_ui.icons.hugeicon import hi
from src.docs.style import render_codeblock

THEME_OPTIONS = [
    ("Hematite", "فيْروز", "gray"),
    ("Feyrouz", "فيْروز", "blue"),
    ("Yaqout", "يَاقوت", "red"),
    ("Zumurrud", "زُمُرُّد", "green"),
    ("Kahraman", "كَهْرَمان", "amber"),
    ("Amethyst", "أَمِيثِسْت", "purple"),
]

THEME_MAP = {
    "gray": themes.GRAY,
    "blue": themes.BLUE,
    "purple": themes.PURPLE,
    "red": themes.RED,
    "green": themes.GREEN,
    "amber": themes.AMBER,
}


def theme_buttons():
    return rx.el.div(
        rx.el.div(
            select.root(
                select.trigger(
                    select.value(),
                    hi(
                        "Add01Icon",
                        class_name="size-4 transition-transform duration-50 ease-in-out group-aria-[expanded=true]:rotate-45",
                    ),
                    class_name="w-[150px] flex items-center justify-between group rounded-lg px-2 py-1.5",
                ),
                select.portal(
                    select.positioner(
                        select.popup(
                            select.group(
                                select.group_label("Theme"),
                                *[
                                    select.item(
                                        select.item_text(theme_class.capitalize()),
                                        select.item_indicator(
                                            hi("Tick02Icon", class_name="size-4")
                                        ),
                                        value=theme_class.capitalize(),
                                        class_name="w-full flex flex-row items-center justify-between",
                                        on_click=hooks.current_theme.set_value(
                                            theme_class
                                        ),
                                    )
                                    for _, __, theme_class in THEME_OPTIONS
                                ],
                            ),
                            class_name="w-[150px]",
                        ),
                        side_offset=4,
                        align_item_with_trigger=True,
                    ),
                ),
                name="theme_select",
                default_value=hooks.current_theme.value.to(str).capitalize(),
            ),
            dialog(
                trigger=button(
                    hi("Copy01Icon", class_name="size-4"),
                    class_name="cursor-pointer flex flex-row items-center size-8 rounded-lg",
                    variant="outline",
                    size="sm",
                ),
                title=hooks.current_theme.value.to(str).capitalize(),
                description="Copy and paste the following code into your CSS file.",
                content=rx.el.div(
                    rx.match(
                        hooks.current_theme.value.to(str),
                        *[
                            (
                                theme_name,
                                render_codeblock(
                                    theme_value, "markup", True, True, True
                                ),
                            )
                            for theme_name, theme_value in THEME_MAP.items()
                        ],
                    ),
                    class_name="!w-full",
                    on_mount=rx.call_script(
                        """
                        const code = document.querySelector("code");

                        // Check if swatches already exist
                        const existingSwatches = code.querySelectorAll("span[data-color-swatch]");

                        if (existingSwatches.length === 0) {
                            Array.from(code.childNodes).forEach((node, index) => {
                                // Check if it's a text node
                                if (node.nodeType === Node.TEXT_NODE) {
                                    const text = node.textContent;
                                    const match = text.match(/oklch\\([^)]+\\)/);

                                    if (match) {
                                        const colorText = match[0];
                                        const matchIndex = text.indexOf(match[0]);

                                        // Split the text node
                                        const beforeText = text.substring(0, matchIndex);
                                        const afterText = text.substring(matchIndex);

                                        // Create new text nodes
                                        const beforeNode = document.createTextNode(beforeText);
                                        const afterNode = document.createTextNode(afterText);

                                        // Create swatch
                                        const swatch = document.createElement("span");
                                        swatch.setAttribute("data-color-swatch", "true");
                                        swatch.style.backgroundColor = colorText;
                                        swatch.style.width = "0.8em";
                                        swatch.style.height = "0.8em";
                                        swatch.style.display = "inline-block";
                                        swatch.style.marginRight = "0.5em";
                                        swatch.style.borderRadius = "3px";
                                        swatch.style.border = "1px solid rgba(0,0,0,0.2)";
                                        swatch.style.verticalAlign = "middle";

                                        // Replace original node with: beforeText + swatch + afterText
                                        code.insertBefore(beforeNode, node);
                                        code.insertBefore(swatch, node);
                                        code.insertBefore(afterNode, node);
                                        code.removeChild(node);
                                    }
                                } else if (node.nodeType === Node.ELEMENT_NODE && !node.classList.contains('linenumber')) {
                                    const text = node.textContent;
                                    const match = text.match(/oklch\\([^)]+\\)/);

                                    if (match && !node.dataset.swatchAdded) {
                                        const colorText = match[0];
                                        const matchIndex = text.indexOf(match[0]);

                                        // For element nodes, we'll use innerHTML manipulation
                                        const beforeText = text.substring(0, matchIndex);
                                        const afterText = text.substring(matchIndex);

                                        const swatch = document.createElement("span");
                                        swatch.setAttribute("data-color-swatch", "true");
                                        swatch.style.backgroundColor = colorText;
                                        swatch.style.width = "0.8em";
                                        swatch.style.height = "0.8em";
                                        swatch.style.display = "inline-block";
                                        swatch.style.marginRight = "0.5em";
                                        swatch.style.borderRadius = "3px";
                                        swatch.style.border = "1px solid rgba(0,0,0,0.2)";
                                        swatch.style.verticalAlign = "middle";

                                        node.textContent = beforeText;
                                        node.appendChild(swatch);
                                        node.appendChild(document.createTextNode(afterText));
                                        node.dataset.swatchAdded = "true";
                                    }
                                }
                            });
                        }
                        """
                    ),
                ),
                class_name="!w-full md:!max-w-[42rem] bg-background !h-[80vh] !overflow-hidden",
            ),
            class_name=(
                "w-full flex flex-row flex-wrap gap-4 items-center "
                "justify-center md:justify-end px-8"
            ),
        ),
    )
