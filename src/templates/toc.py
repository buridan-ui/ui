import reflex as rx
from typing import List, Dict


def _create_markdown_toc_links(toc_data: List[Dict]) -> rx.Component:
    """Create markdown TOC links."""
    if not toc_data:
        return rx.el.div()

    return rx.el.div(
        *[
            rx.el.a(
                entry["text"],
                href=f"#{entry['id']}",
                class_name=f"cursor-pointer text-sm font-regular hover:underline no-underline{' pl-4' if entry['level'] > 1 else ''}",
            )
            for entry in toc_data
        ],
        class_name="flex flex-col w-full gap-y-2",
    )


def _create_external_tool_links(url: str):
    """Create links for viewing documentation in external tools."""

    # Shared JavaScript for generating AI chat prompts
    ai_prompt_script = """
        const currentPage = window.location.href.split(/[?#]/)[0];  // remove ? and #
        const markdownFile = currentPage.endsWith('/')
            ? currentPage.slice(0, -1) + '.md'
            : currentPage + '.md';
        const prompt = `I'm looking at this documentation markdown file: ${markdownFile}
Help me understand how to use it. Be ready to explain concepts, give examples, or help debug based on it.`;
        const encodedPrompt = encodeURIComponent(prompt);
    """

    # Shared style classes
    link_classes = "cursor-pointer text-sm font-regular no-underline flex flex-row items-center gap-x-2"
    button_classes = link_classes + " bg-transparent border-0 p-0 text-left"

    def link_item(icon_light, icon_dark, text, href):
        """Standard link (used for Markdown view)."""
        return rx.el.a(
            rx.image(
                src=rx.color_mode_cond(icon_light, icon_dark), class_name="size-4"
            ),
            rx.el.p(text, class_name="font-medium"),
            href=href,
            target="_blank",
            rel="noopener noreferrer",
            class_name=link_classes,
        )

    def button_item(icon_light, icon_dark, text, on_click_script):
        """Button version for JS-based tools (ChatGPT, Claude, Reflex)."""
        return rx.el.button(
            rx.image(
                src=rx.color_mode_cond(icon_light, icon_dark), class_name="size-4"
            ),
            rx.el.p(text, class_name="font-medium"),
            class_name=button_classes,
            on_click=rx.call_script(on_click_script),
        )

    return rx.el.div(
        # Markdown view link (true link)
        link_item(
            icon_light="/svg/markdown/md_light.svg",
            icon_dark="/svg/markdown/md_dark.svg",
            text="View as Markdown",
            href=f"/{url}.md",
        ),
        # ChatGPT (opens new tab, no URL change)
        button_item(
            icon_light="/svg/openai/ai_light.svg",
            icon_dark="/svg/openai/ai_dark.svg",
            text="Open in ChatGPT",
            on_click_script=ai_prompt_script
            + """
                const chatUrl = `https://chat.openai.com/?q=${encodedPrompt}`;
                window.open(chatUrl, "_blank");
            """,
        ),
        # Claude
        button_item(
            icon_light="/svg/claude/claude_light.svg",
            icon_dark="/svg/claude/claude_dark.svg",
            text="Open in Claude",
            on_click_script=ai_prompt_script
            + """
                const claudeUrl = `https://claude.ai/new?q=${encodedPrompt}`;
                window.open(claudeUrl, "_blank");
            """,
        ),
        # Reflex Build
        button_item(
            icon_light="/svg/reflex/reflex_light.svg",
            icon_dark="/svg/reflex/reflex_dark.svg",
            text="Open Reflex Build",
            on_click_script=ai_prompt_script
            + """
                const reflexUrl = `https://build.reflex.dev/`;
                window.open(reflexUrl, "_blank");
            """,
        ),
        class_name="flex flex-col w-full gap-y-2",
    )


def table_of_content(url: str, toc_data: List[Dict]):
    """
    Render table of contents.

    Args:
        toc_data: List of dicts with 'text', 'id', 'level' keys
    """

    return rx.el.div(
        rx.scroll_area(
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "External Tools",
                        color=rx.color("slate", 12),
                        class_name="text-sm font-bold pb-2",
                    ),
                    _create_external_tool_links(url),
                    class_name="w-full flex flex-col",
                ),
                rx.el.div(
                    rx.el.label(
                        "Table of Content",
                        color=rx.color("slate", 12),
                        class_name="text-sm font-bold pb-2",
                    ),
                    _create_markdown_toc_links(toc_data),
                    class_name="w-full flex flex-col",
                ),
                class_name="flex flex-col w-full h-full p-4 gap-y-6",
            ),
            class_name="flex flex-col gap-y-4 [&_.rt-ScrollAreaScrollbar]:mt-[2rem] [&_.rt-ScrollAreaScrollbar]:mb-[2rem]",
        ),
        class_name="hidden lg:block max-w-[18rem] w-full sticky top-12 h-[calc(100vh-3rem)] shrink-0",
    )
