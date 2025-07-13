# ... base prefixes for different sections
_GS_Base = "/getting-started/"
_P = "/pantry/"
_C = "/charts/"
_Pro = "/pro/"

# ... pro routes
BuridanProRoutes = [
    {
        "name": "Integrated Tables",
        "path": f"{_Pro}integrated-tables",
        "dir": "table",
        "description": "Advanced table layout with dynamic data integration.",
    },
]


# ... getting started paths
GettingStartedRoutes = [
    {
        "name": "Introduction",
        "path": f"{_GS_Base}introduction",
        "dir": "introduction",
        "description": "Overview of what Buridan UI is and how it works.",
    },
    {
        "name": "Who is Buridan?",
        "path": f"{_GS_Base}who-is-buridan",
        "dir": "buridan",
        "description": "A brief backstory on Buridan and the philosophy behind the framework.",
    },
    {
        "name": "Installation",
        "path": f"{_GS_Base}installation",
        "dir": "installation",
        "description": "Steps to install and start using Buridan in your project.",
    },
    {
        "name": "Theming",
        "path": f"{_GS_Base}theming",
        "dir": "theming",
        "description": "Customize your app’s appearance using themes and tokens.",
    },
    {
        "name": "Charting Walkthrough",
        "path": f"{_GS_Base}charting",
        "dir": "charting",
        "description": "Step-by-step guide to building charts using Buridan.",
    },
    {
        "name": "Dashboard Walkthrough",
        "path": f"{_GS_Base}dashboard",
        "dir": "dashboard",
        "description": "Build a full dashboard UI using Buridan components.",
    },
    {
        "name": "ClientStateVar",
        "path": f"{_GS_Base}client-state-var",
        "dir": "clientstate",
        "description": "Use client-side state variables to manage local interactivity.",
    },
    {
        "name": "Changelog",
        "path": f"{_GS_Base}changelog",
        "dir": "changelog",
        "description": "Track feature additions, improvements, and bug fixes.",
    },
]


# ... pantry component paths
PantryRoutes = sorted(
    [
        {
            "name": "Accordions",
            "path": f"{_P}accordions",
            "dir": "accordions",
            "description": "Expandable accordion sections for showing and hiding content.",
        },
        {
            "name": "Animations",
            "path": f"{_P}animations",
            "dir": "animations",
            "description": "Prebuilt animation utilities for smooth transitions.",
        },
        {
            "name": "Backgrounds",
            "path": f"{_P}backgrounds",
            "dir": "backgrounds",
            "description": "Flexible background sections for visual structure.",
        },
        {
            "name": "Cards",
            "path": f"{_P}cards",
            "dir": "cards",
            "description": "Modular content containers for displaying grouped information.",
        },
        {
            "name": "Descriptive Lists",
            "path": f"{_P}descriptive-lists",
            "dir": "lists",
            "description": "Use description lists to pair labels with detailed values.",
        },
        {
            "name": "Featured",
            "path": f"{_P}featured",
            "dir": "featured",
            "description": "Highlight key content with featured callout components.",
        },
        {
            "name": "Footers",
            "path": f"{_P}footers",
            "dir": "footers",
            "description": "Footer layouts with links, branding, and legal content.",
        },
        {
            "name": "Frequently Asked Questions",
            "path": f"{_P}frequently-asked-questions",
            "dir": "faq",
            "description": "FAQ layout for answering common user questions.",
        },
        {
            "name": "Inputs",
            "path": f"{_P}inputs",
            "dir": "inputs",
            "description": "Reusable input components for forms and interactions.",
        },
        {
            "name": "Logins",
            "path": f"{_P}logins",
            "dir": "logins",
            "description": "Authentication page templates for login and signup.",
        },
        {
            "name": "Menus",
            "path": f"{_P}menus",
            "dir": "menus",
            "description": "Dropdown and popover menus for navigation or options.",
        },
        {
            "name": "Onboarding & Progress",
            "path": f"{_P}onboarding-and-progress",
            "dir": "onboardings",
            "description": "Guided onboarding steps and progress indicators.",
        },
        {
            "name": "Payments & Billing",
            "path": f"{_P}payments-and-billing",
            "dir": "payments",
            "description": "Sections for pricing, plans, and payment details.",
        },
        {
            "name": "Popups",
            "path": f"{_P}popups",
            "dir": "popups",
            "description": "Alert boxes and modal popups for messages and actions.",
        },
        {
            "name": "Pricing Sections",
            "path": f"{_P}pricing-sections",
            "dir": "pricing",
            "description": "Prebuilt pricing tables and plan comparison layouts.",
        },
        {
            "name": "Prompt Boxes",
            "path": f"{_P}prompt-boxes",
            "dir": "prompts",
            "description": "Lightweight prompts for alerts, confirmations, and actions.",
        },
        {
            "name": "Sidebars",
            "path": f"{_P}sidebars",
            "dir": "sidebars",
            "description": "Responsive sidebar layouts for navigation or content grouping.",
        },
        {
            "name": "Standard Forms",
            "path": f"{_P}standard-forms",
            "dir": "forms",
            "description": "Ready-to-use forms with fields and validation.",
        },
        {
            "name": "Standard Tables",
            "path": f"{_P}standard-tables",
            "dir": "tables",
            "description": "Clean and sortable tables for structured data.",
        },
        {
            "name": "Stats",
            "path": f"{_P}stats",
            "dir": "stats",
            "description": "Visual stats blocks for metrics and KPIs.",
        },
        {
            "name": "Subscribe",
            "path": f"{_P}subscribe",
            "dir": "subscribe",
            "description": "Subscription forms and call-to-action sections.",
        },
        {
            "name": "Tabs",
            "path": f"{_P}tabs",
            "dir": "tabs",
            "description": "Tab navigation components to switch between views.",
        },
        {
            "name": "Timeline",
            "path": f"{_P}timeline",
            "dir": "timeline",
            "description": "Timeline layouts for step-based or historical data.",
        },
    ],
    key=lambda x: x["name"],
)


# ... chart component paths
ChartRoutes = sorted(
    [
        {
            "name": "Area Charts",
            "path": f"{_C}area-charts",
            "dir": "area",
            "description": "Display continuous data with filled area charts.",
        },
        {
            "name": "Bar Charts",
            "path": f"{_C}bar-charts",
            "dir": "bar",
            "description": "Use vertical or horizontal bars to compare values.",
        },
        {
            "name": "Doughnut Charts",
            "path": f"{_C}doughnut-charts",
            "dir": "doughnut",
            "description": "Donut-style charts to show part-to-whole proportions.",
        },
        {
            "name": "Line Charts",
            "path": f"{_C}line-charts",
            "dir": "line",
            "description": "Plot trends over time or ordered categories using lines.",
        },
        {
            "name": "Pie Charts",
            "path": f"{_C}pie-charts",
            "dir": "pie",
            "description": "Display data as slices of a circular pie.",
        },
        {
            "name": "Radar Charts",
            "path": f"{_C}radar-charts",
            "dir": "radar",
            "description": "Compare multiple variables across axes in a radar format.",
        },
        {
            "name": "Scatter Charts",
            "path": f"{_C}scatter-charts",
            "dir": "scatter",
            "description": "Show correlations between two numerical variables.",
        },
    ],
    key=lambda x: x["name"],
)
