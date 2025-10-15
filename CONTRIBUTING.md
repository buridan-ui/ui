# Buridan UI Contribution Guide

Thank you for your interest in contributing to Buridan UI! This guide will help you understand how to add new components and documentation to the project.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- Basic knowledge of Reflex

### Setting Up Development Environment

1.  Fork the repository and clone it to your local machine.
2.  Install [uv](https://github.com/astral-sh/uv) if you don't have it already. It is a fast Python package installer.
    ```bash
    pip install uv
    ```
3.  Create a virtual environment and install dependencies:
    ```bash
    uv venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    uv pip install -e .
    ```
4.  Set up pre-commit hooks to automatically format your code.
    ```bash
    pre-commit install
    ```

## Project Structure

The project is organized as follows:

-   `src/`: The main source directory for the application.
    -   `components/`: Core UI components and wrappers for the documentation site itself.
    -   `docs/`: Contains the logic for parsing and generating documentation.
        -   `library/`: **This is where component source code lives.** Components are organized into subdirectories by category (e.g., `components`, `charts`).
    -   `hooks.py`: Global client-side state management.
    -   `routes.py`: Dynamically generates documentation routes from markdown files.
    -   `templates/`: Contains the main layouts for the website (sidebar, navbar, etc.).
    -   `utils/`: Shared utility functions.
    -   `views/`: High-level page components, like the main landing page.
    -   `src.py`: The main Reflex application entry point.
-   `docs/`: Contains the markdown files for the documentation pages. Each subdirectory corresponds to a section in the sidebar.

## Adding New Components

The process for adding new components is streamlined to keep code and documentation in sync.

### 1. Create the Component File

1.  Identify the correct category for your component under `src/docs/library/`. Common categories are `components`, `charts`, and `wrapped_components`. If a new category is needed, create a new subdirectory.
2.  Create a new Python file for your component (e.g., `src/docs/library/components/my_component/my_component.py`) and a file for examples (`.../my_component/examples.py`).
3.  Write your component as a Python function that returns a `reflex.Component`. It's best practice to create multiple functions in the `examples.py` file to showcase different variations of your component.

**Example Component (`.../my_component/my_component.py`):**

```python
import reflex as rx

def my_component(*children, **props):
    return rx.box(
        "My new component!",
        *children,
        **props
    )
```

**Example for Docs (`.../my_component/examples.py`):**

```python
import reflex as rx
from .my_component import my_component

def my_component_demo():
    return my_component()

def my_component_with_style():
    return my_component(style={"border": "1px solid red"})
```

### 2. Create the Documentation Page

1.  Create a new markdown file in the corresponding `docs/` subdirectory. For example, `docs/components/my_component.md`.
2.  Add frontmatter to the top of the file to configure its title and order in the sidebar.

    ```yaml
    ---
    title: My Component
    order: 10
    ---
    ```

### 3. Display the Component in Docs

Use the custom markdown commands to render your component and its code. The parser automatically discovers any function in the `src/docs/library/` directory.

-   To show a live demo and its complete file source code:
    `--demo_and_code_single_file(my_component_demo)--`

-   To show a live demo and only the source code of the specific function:
    `--demo_and_single_function(my_component_with_style)--`

-   To show only the source code of a function:
    `--show_code_with_language([my_component_demo, 'python'])--`

-   To render a component directly without code:
    `--my_component_demo--`

**Example Markdown (`docs/components/my_component.md`):**

    ---
    title: My Component
    order: 10
    ---

    # My Component

    This is a great new component.

    ## Basic Example

    --demo_and_single_function(my_component_demo)--

    ## Styled Example

    Here is a component with a style.

    --demo_and_single_function(my_component_with_style)--

    ## Full Source Code

    You can also view the full source code of the module.

    --full_source_page_of_component(my_component_demo)--

The routing and sidebar navigation will be updated automatically based on the new markdown file.

## Testing Your Changes

1.  Run the development server:
    ```bash
    reflex run
    ```
2.  Visit `http://localhost:3000` and navigate to your new documentation page to see your component in action.
3.  Verify that your component renders correctly and works as expected.

## Submitting Your Contribution

1.  Create a new branch for your feature:
    ```bash
    git checkout -b feature/new-component
    ```
2.  Commit your changes with clear, descriptive commit messages.
3.  Push your branch to your fork:
    ```bash
    git push origin feature/new-component
    ```
4.  Create a pull request to the main repository.
5.  In your PR description, include:
    -   A clear description of what you added.
    -   Screenshots if applicable.
    -   Any special considerations or notes for reviewers.

## Best Practices

### Component Design

-   Follow existing component patterns for consistency.
-   Use responsive design principles.
-   Comment your code, especially complex logic.
-   Provide reasonable default values for all props.

### Naming Conventions

-   Component files and functions should use `snake_case`.
-   Directory names for component categories should be plural (e.g., `components`, `charts`).

### Code Style

-   Follow PEP 8 guidelines.
-   Use type hints where possible.
-   Format your code with `black` and `ruff`. The pre-commit hooks should handle this automatically.

## Troubleshooting

### Common Issues

-   **Component not found in markdown**: Ensure your component function is located within the `src/docs/library/` directory and that you are using the correct function name in the markdown command.
-   **Component not showing up**: Verify that the route is correctly generated by checking the `docs/` path and the frontmatter in your `.md` file.
-   **Styling issues**: The project uses Tailwind CSS. Check `tailwind.config.js` and existing components for styling conventions.

If you encounter issues not covered here, please open an issue on the repository.

## Need Help?

If you need assistance or have questions about contributing, please:
- Open an issue on the repository.
- Reach out to the maintainers.
- Check existing documentation and examples.

Thank you for contributing to Buridan UI!