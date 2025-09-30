# Buridan UI Contribution Guide

Thank you for your interest in contributing to Buridan UI! This guide will help you understand how to add components, routes, exports, and other features to the project.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- Basic knowledge of Reflex and React

### Setting Up Development Environment

1. Fork the repository and clone it to your local machine
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install reflex
   ```

### Development Mode

Buridan UI has a development mode that allows you to work on specific components without loading the entire library. Use the provided `dev.sh` script:

```bash
# Work on specific components
./dev.sh components sidebar cards

# Work on specific charts
./dev.sh charts line bar

# Work on both components and charts
./dev.sh both sidebar line

# Work on pro components
./dev.sh pro table

# Disable development mode (load everything)
./dev.sh off
```

## Project Structure

- `buridan_ui/`: Main package directory
  - `pantry/`: UI components organized by category (cards, sidebars, etc.)
  - `charts/`: Chart components (bar, line, pie, etc.)
  - `pro/`: Pro components for paid/premium features
  - `static/`: Static routes and metadata
  - `export.py`: Manages dynamic export of components
  - `templates/`: Base templates and layouts

## Adding New Components

### 1. Creating a Component

Components are organized by category (e.g., sidebars, cards) and version number.

1. Identify the category for your component
2. Create a new version file in the appropriate directory:

```python
# Example: buridan_ui/pantry/sidebars/v3.py

import reflex as rx

def sidebar_v3():
    """A sidebar component - version 3."""
    return rx.box(
        # Your component implementation
        rx.text("Sidebar v3"),
        # Component content
    )
```

### 2. Register the Component in Export Configuration

Update the `ExportConfig` class in `export.py` to include your new component version:

```python
# For a new version of an existing component:
self.COMPONENTS = {
    "sidebars": {"versions": range(1, 4), "func_prefix": "sidebar"},  # Update range to include your version
    # Other components...
}

# For a completely new component category:
self.COMPONENTS = {
    # Existing components...
    "new_category": {"versions": range(1, 2), "func_prefix": "new_category"},
}
```

### 3. Add Route and Metadata

1. Add a route to the appropriate route collection in `static/routes.py`:

```python
PantryRoutes = [
    # Existing routes...
    {"name": "New Category", "path": "/pantry/new-category", "dir": "new_category"},
]
```

### 4. Update Metadata

The metadata for components is managed through a script. To update metadata after adding new components:

1. Temporarily comment out the three export generation lines at the end of `export.py`:
   ```python
   # Comment these lines out temporarily
   # pro_exports_config = generate_pro_exports()
   # pantry_exports_config = generate_pantry_exports()
   # charts_exports_config = generate_chart_exports()
   ```

<<<<<<< HEAD
2. In `src/static/scripts.py`, run the `get_directory_meta_data()` function.
=======
2. In `src/static/scripts.py`, run the `get_directory_meta_data()` function. 
>>>>>>> origin/main
This updates `src/static/meta.py` with new metadata for all files and folders.

3. Make sure to uncomment the export generation lines after you run the script.


## Adding Charts

The process for adding charts is similar to adding components:

1. Create your chart in `buridan_ui/charts/[chart_type]/v[number].py`
2. Update the chart configuration in `export.py`
3. Add routes and metadata for your chart

```python
# Example: buridan_ui/charts/new_chart/v1.py
import reflex as rx

def new_chart_v1():
    """A new chart type - version 1."""
    # Chart implementation
    return rx.recharts.line_chart(
        # Chart configuration
    )
```

## Adding Pro Components

Pro components follow a similar pattern but go in the `pro/` directory:

1. Create your component in `buridan_ui/pro/[component_type]/v[number].py`
2. Update the PRO configuration in `export.py`
3. Add routes and metadata for your pro component

## Testing Your Changes

1. Run the development server with your specific component:
   ```bash
   ./dev.sh components your_component
   ```

2. Visit `http://localhost:3000` to see your component in action

3. Verify that your component renders correctly and works as expected

## Submitting Your Contribution

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/new-component
   ```

2. Commit your changes with clear, descriptive commit messages

3. Push your branch to your fork:
   ```bash
   git push origin feature/new-component
   ```

4. Create a pull request to the main repository

5. In your PR description, include:
   - A clear description of what you added
   - Screenshots if applicable
   - Any special considerations or notes for reviewers

## Best Practices

### Component Design

- Follow existing component patterns for consistency
- Use responsive design principles
- Comment your code, especially complex logic
- Provide reasonable default values for all props

### Naming Conventions

- Component functions: `[component_type]_v[version]` (e.g., `sidebar_v1`)
- Directory names: plural form for categories (e.g., `sidebars`, `cards`)
- File names: `v[version].py` for version files

### Code Style

- Follow PEP 8 guidelines
- Use type hints where possible
- Format your code with Black before submitting

## Troubleshooting

### Common Issues

- **KeyError for a component**: Make sure your component is properly registered in the export configuration and has corresponding metadata
- **Component not showing up**: Verify that the route is correctly added and the component is exported properly
- **Development mode not working**: Check that your component name in the dev script matches the directory name exactly

If you encounter issues not covered here, please open an issue on the repository.

## Need Help?

If you need assistance or have questions about contributing, please:
- Open an issue on the repository
- Reach out to the maintainers
- Check existing documentation and examples

Thank you for contributing to Buridan UI!
