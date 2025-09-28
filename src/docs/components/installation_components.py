import reflex as rx


# Used in --show_code(python_version_check_example)--
def python_version_check_example():
    return rx.markdown("```bash\npython3 --version\n```")


# Used in --show_code(install_reflex_example)--
def install_reflex_example():
    return rx.markdown("```bash\npip3 install reflex\n```")


# Used in --show_code(reflex_version_check_example)--
def reflex_version_check_example():
    return rx.markdown("```bash\nreflex --version\n```")


# Used in --show_code(create_reflex_app_example)--
def create_reflex_app_example():
    return rx.markdown("```bash\nreflex init\n```")
