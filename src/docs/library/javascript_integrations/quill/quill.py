import reflex as rx


def quill_stylesheet():
    return rx.el.link(
        href="https://cdn.jsdelivr.net/npm/quill@2.0.3/dist/quill.snow.css",
        rel="stylesheet",
    )


def quill_custom_font():
    return rx.el.link(
        href="https://fonts.googleapis.com/css?family=Aref+Ruqaa|Mirza|Roboto",
        rel="stylesheet",
    )


def quill_lib():
    return rx.script(src="https://cdn.jsdelivr.net/npm/quill@2.0.3/dist/quill.js")


def quill_init():
    return rx.script(
        """
        setTimeout(function() {
            const quill = new Quill('#quill-editor', {
                theme: 'snow',
                placeholder: 'When Mr. Bilbo Baggins of Bag End announced that he would shortly be celebrating his eleventy-first birthday with a party of special magnificence, there was much talk and excitement in Hobbiton.',
            });
        }, 1000);
    """
    )
