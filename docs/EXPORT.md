# Buridan UI Export System Documentation

A comprehensive guide to understanding and modifying the Buridan UI export system.

## Overview

The export system is a modular, configuration-driven architecture that dynamically generates routes, components, and pages for the Buridan UI application. It supports three main component types:

- **Pantry Components** - UI components in `buridan_ui/pantry/`
- **Chart Components** - Chart visualizations in `buridan_ui/charts/`

## Architecture

### Core Classes

```
ExportConfig          → Centralized configuration and settings
├── ComponentConfig   → Individual component/chart configuration
├── RouteConfig       → Static route configuration
└── Development mode  → Environment-based filtering

SourceRetriever       → Source code retrieval strategies
├── get_pantry_source()
└── get_chart_source()

ExportFactory         → Creates export functions
├── create_pantry_export()
└── create_chart_export()

ExportGenerator       → Generates collections of exports
├── generate_pantry_exports()
└── generate_chart_exports()

RouteManager          → Handles route filtering
└── filter_routes()

ApplicationExporter   → Main orchestrator
└── export_app()     → Entry point
```

## Configuration

### Adding New Components

#### 1. Pantry Components

```python
# In ExportConfig._init_configurations()
self.COMPONENTS = {
    "your_component": ComponentConfig(
        versions=range(1, 4),  # Versions 1, 2, 3
        func_prefix="your_component",  # Function name prefix
        flexgen_url="https://...",  # Optional FlexGen URL
    ),
    # ... existing components
}
```

#### 2. Chart Components

```python
# In ExportConfig._init_configurations()
self.CHARTS = {
    "your_chart": ComponentConfig(
        versions=[1, 2, 5],  # Specific versions
        func_prefix="your_chart",
        flexgen_url="https://...",
        has_api_reference=True,  # Generates API docs
    ),
    # ... existing charts
}
```

### Adding Static Routes

```python
# In ExportConfig._init_getting_started_routes()
from your_module import your_component

self.STATIC_ROUTES = [
    RouteConfig(
        path="/your-path",
        component=your_component,
        title="Your Page Title - Buridan UI"
    ),
    # ... existing routes
]
```

## File Structure Requirements

### Component Files

Your component files must follow this structure:

```
buridan_ui/pantry/your_component/
├── v1.py
├── v2.py
└── v3.py
```

Each version file must export a function:

```python
# buridan_ui/pantry/your_component/v1.py
def your_component_v1():
    return rx.div("Your component content")
```

### Function Naming Convention

- **File**: `v{version}.py`
- **Function**: `{func_prefix}_v{version}`

Examples:
- File: `v1.py` → Function: `card_v1()`
- File: `v2.py` → Function: `barchart_v2()`

## Development Mode

### Environment Variables

```bash
# Enable development mode
export BURIDAN_DEV_MODE=true

# Select specific components (comma-separated)
export BURIDAN_COMPONENTS=cards,buttons,forms

# Select specific charts
export BURIDAN_CHARTS=bar,line,pie

```

### Development Mode Behavior

- **No selections**: All components included
- **Specific selections**: Only selected items included
- **Mixed selections**: Only items from selected categories included
- **Category exclusion**: If other categories are selected, unselected categories are excluded

## Usage Examples

### Basic Usage

```python
# In your main app file
from buridan_ui.export_system import export_app

app = rx.App()
export_app(app)  # This handles everything
```

### Route Filtering (if needed elsewhere)

```python
from buridan_ui.export_system import filter_routes

# Filter routes based on dev settings
filtered_routes = filter_routes(your_routes_list)
```

## Customization

### Custom Grid Layouts

```python
# In ExportConfig._init_configurations()
self.GRID_CONFIGS = {
    "your_component": {
        "columns": 2,
        "spacing": "4",
        # Any responsive_grid parameters
    }
}
```

### Custom Source Retrieval

If you need special source handling:

```python
# In SourceRetriever class
@staticmethod
def get_custom_source(directory: str, filename: str) -> str:
    """Custom source retrieval logic."""
    # Your custom logic here
    return source_code
```

Then modify the appropriate factory method to use it.

### Custom Export Logic

For special export requirements:

```python
# In ExportFactory class
@staticmethod
def create_custom_export(directory: str, config: ComponentConfig, version: int) -> Callable:
    """Create custom export function."""
    # Your custom export logic
    pass
```

## Common Tasks

### Adding a New Component Type

1. **Add configuration** in `ExportConfig._init_configurations()`
2. **Add filtering logic** in `ExportConfig` (should_include_* method)
3. **Add source retrieval** in `SourceRetriever` (if different from existing)
4. **Add export factory method** in `ExportFactory`
5. **Add generator method** in `ExportGenerator`
6. **Update route management** in `ApplicationExporter._add_dynamic_routes()`

### Modifying Component Versions

```python
# Change from range(1, 4) to range(1, 6)
"your_component": ComponentConfig(
    versions=range(1, 6),  # Now includes v4 and v5
    func_prefix="your_component",
)
```

### Adding FlexGen URLs

```python
"your_component": ComponentConfig(
    versions=range(1, 4),
    func_prefix="your_component",
    flexgen_url="https://reflex.build/gen/your-gen-id/",
)
```

### Enabling API References

```python
# Only for charts currently
"your_chart": ComponentConfig(
    versions=range(1, 4),
    func_prefix="your_chart",
    has_api_reference=True,  # Adds API documentation
)
```

## Troubleshooting

### Common Issues

1. **Import Error**: Check file structure and function naming
2. **Missing Routes**: Verify route configuration and dev mode settings
3. **Source Not Found**: Check file paths in source retrieval methods
4. **Version Mismatch**: Ensure version ranges match actual files

### Debug Mode

The system prints debug information when `BURIDAN_DEV_MODE=true`:

```
Development mode: Enabled
Selected components: cards, buttons
Selected charts: bar, line
```

### Error Messages

The system provides descriptive error messages:
```
Failed to import card_v1 from buridan_ui.pantry.cards.v1: No module named 'buridan_ui.pantry.cards.v1'
```

## Best Practices

1. **Consistent Naming**: Follow the `{prefix}_v{version}` convention
2. **Version Management**: Use ranges for consecutive versions, lists for specific versions
3. **Configuration First**: Always update configuration before adding files
4. **Test in Dev Mode**: Use development mode to test individual components
5. **Document Changes**: Update this README when adding new patterns

## Migration Guide

### From Old System

If migrating from the old system:

1. **Move configurations** to `ComponentConfig` instances
2. **Update function names** to match new conventions
3. **Move static routes** to `STATIC_ROUTES` configuration
4. **Update imports** to use new public API
5. **Test thoroughly** with development mode

### Adding Legacy Components

For components that don't follow the standard pattern, you may need to:

1. Create custom source retrieval methods
2. Create custom export factory methods
3. Handle special cases in the configuration

This system is designed to be flexible and extensible while maintaining clean separation of concerns.
