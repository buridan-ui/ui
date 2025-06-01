import reflex as rx

from buridan_ui.wrappers.base.main import base


def changelog_meta(tag: str, text: str):
    return rx.box(
        (
            rx.icon(tag=tag, size=14, color=rx.color("slate", 11))
            if text
            else rx.box(class_name="hidden")
        ),
        rx.text(text, class_name="text-sm font-semibold"),
        class_name="flex flex-row gap-x-2 items-center",
    )


def changelog_wrapper(title: str, date: str, version: str, log: str):
    return rx.box(
        rx.box(
            rx.box(
                changelog_meta("calendar-range", date),
                changelog_meta("git-compare", version),
                class_name="flex flex-row gap-x-4 items-center",
            ),
            rx.text(title, class_name="text-2xl font-semibold"),
            class_name="flex flex-col gap-y-2",
        ),
        rx.markdown(
            log,
            component_map={
                "ul": lambda *children: rx.list(*children, class_name="py-3"),
                "li": lambda text: rx.list_item(
                    rx.el.span("•", class_name="text-[12px]"),
                    rx.text(f"{text}", class_name="text-[12px]"),
                    class_name="flex flex-row items-center gap-x-4 py-1",
                ),
            },
        ),
        border=f"1px dashed {rx.color('gray', 5)}",
        class_name="rounded-xl p-4",
    )


@base("/getting-started/changelog", "Site Changelog")
def changelog():
    return [
        rx.box(
            changelog_wrapper(
                title="Enhanced Charting Experience & Theming Overhaul",
                date="June 1, 2025",
                version="buridan/ui v0.6.7",
                log="""
- Introduced a centralized theming system for consistent chart styling.
- Enhanced Recharts with smooth animations and improved responsiveness.
- Added subtle hover effects to theme selection for better UX.
- Updated documentation for theming and charting components.
""",
            ),
            changelog_wrapper(
                title="Minor Updates and Docs Enhancements",
                date="May 30, 2025",
                version="buridan/ui v0.6.6",
                log="""
- Patch error for sidebar visibility feature.
- Support for uv package manager.
- Client State Var documentation.
- Dashboard documentation.
""",
            ),
            changelog_wrapper(
                title="Sidebar Changes and Doc Improvement",
                date="May 22, 2025",
                version="buridan/ui v0.6.5",
                log="""
- New changelog UI design page.
- Update sidebar with new visibility feature.
- Improved charting walkthrough documentation.
""",
            ),
            changelog_wrapper(
                title="New Sidebar UX and Menu Structure",
                date="May 18, 2025",
                version="buridan/ui v0.6.4",
                log="""
- New component wrapper menu bar.
- Updated chart structure: Area, Bar, Line.
- Bumped Reflex version and related files.
- New UX for sidebar.
""",
            ),
            changelog_wrapper(
                title="Component Refinements and Bug Fixes",
                date="May 04, 2025",
                version="buridan/ui v0.6.3",
                log="""
- Fixed issues in several components to enhance stability.
- Restored missing exports.py file.
- Performed code cleanup for improved maintainability.
""",
            ),
            changelog_wrapper(
                title="New Features, Pro Tier, and Improvements",
                date="April 20, 2025",
                version="buridan/ui v0.6.2",
                log="""
- Introduced Buridan Pro — gated access to premium components.
- Added development helper script: dev.sh for local testing & filtering.
- Implemented active sidebar highlighting based on current route.
- Improved layout: breadcrumb in main content, version in left sidebar.
- Right sidebar now includes a persistent header and optional callouts.
- Refined styling and responsiveness across components.
- Minor bug fixes and performance improvements.
""",
            ),
            changelog_wrapper(
                title="Site Refactoring & Major Changes",
                date="March 22, 2025",
                version="buridan/ui v0.6.1",
                log="""
- Major site refactoring of the codebase.
- Major updates to site UI & UX.
- Several sections have been removed or added elsewhere.
- Landing page has been removed.
- New landing page routes to either UI or Lab apps.
- New charts: Doughnut and Scatter Charts.
- New feature: Download repo directly from the site.
- New feature: Code view now separate from tab.
- Site is almost completely stateless (aim to make site static in the near future).
""",
            ),
            changelog_wrapper(
                title="Buridan Dev Labs: Charts",
                date="December 17, 2024",
                version="buridan/ui v0.4.2",
                log="""
- New `Dev Lab` for charts. Easily generate charts with your own data.
- Updated charts theme colors.
- Fixed Area Charts stacking options.
""",
            ),
            changelog_wrapper(
                title="Site Patches and Updates",
                date="December 13, 2024",
                version="buridan/ui v0.4.1",
                log="""
- Added GitHub workflow for Reflex Cloud Deploy automation.
- Code base cleanup and code refactoring.
- Live code editor (experimental) has been deployed (buridan-ui.reflex.run/buridan-sandbox).
""",
            ),
            changelog_wrapper(
                title="Buridan Charts",
                date="December 02, 2024",
                version="buridan/ui v0.4.0",
                log="""
- New charts landing page.
- New chart item: Radar Charts.
- New chart theme color: purple.
- New chart tooltip style sheet.
- Updated responsive logic for mobile view.
- Significant UI update to entire chart codebase.
- New dynamic charting for area, bar, and line charts.
""",
            ),
            changelog_wrapper(
                title="Site patches and New Blueprint Items",
                date="November 26, 2024",
                version="buridan/ui v0.3.4",
                log="""
- New blueprint items: Dashboards & Layouts.
- Major code refactoring for pantry, charts, and blueprint wrappers.
""",
            ),
            changelog_wrapper(
                title="New library feature: Blueprint Templates",
                date="November 20, 2024",
                version="buridan/ui v0.3.3",
                log="""
- Blueprints templates consist of in-depth, more well-rounded apps that can be used out of the box with minor changes.
- Authentication
""",
            ),
            changelog_wrapper(
                title="New Site Landing Page and UI Changes",
                date="November 17, 2024",
                version="buridan/ui v0.3.2",
                log="""
- New site landing page with animation!
- Fixed UI scaling issue for site: functional.
- Updated many site components (nav, side menu, etc...)
""",
            ),
            changelog_wrapper(
                title="Small Patch for Site Scaling UI",
                date="November 15, 2024",
                version="buridan/ui v0.3.1",
                log="""
- Fixed UI scaling issue for site: operational.
""",
            ),
            changelog_wrapper(
                title="New Apps and Site UI Changes",
                date="November 13, 2024",
                version="buridan/ui v0.3.0",
                log="""
- New pantry: Footers!
- New chart item: Pie Charts!
- New interactive app: PubMed A.I.
- UI changes to site landing page.
""",
            ),
            changelog_wrapper(
                title="Site Refinement and UI Updates",
                date="November 08, 2024",
                version="buridan/ui v0.2.0",
                log="""
- Changes to Charts component wrapper.
- Codebase refactor and state changes.
- Changes to code block theme and font size.
- Major changes to @component_wrapper menu items.
""",
            ),
            changelog_wrapper(
                title="New Components and Improvements to Pantry Items",
                date="October 21, 2024",
                version="buridan/ui v0.1.0",
                log="""
- Accordions
- Animations
- Backgrounds
- Cards
- Descriptive Lists
- Featured
- Footers
- Frequently Asked Questions
- Inputs
- Logins
- Menus
- Onboarding & Progress
- Payments & Billing
- Popups
- Pricing Sections
- Prompt Boxes
- Sidebars
- Standard Forms
- Standard Tables
- Stats
- Subscribe
- Tabs
- Timeline
""",
            ),
            changelog_wrapper(
                title="New Library Component: Charts",
                date="October 18, 2024",
                version="buridan/ui v0.1.0",
                log="""
- Area Charts
- Bar Charts
- Doughnut Charts
- Line Charts
- Pie Charts
- Radar Charts
- Scatter Charts
""",
            ),
            changelog_wrapper(
                title="buridan/ui v0.0.1 Deployed to Reflex",
                date="October 16, 2024",
                version="buridan/ui v0.0.1",
                log="""""",
            ),
            changelog_wrapper(
                title="Initial Release", date="October 5, 2024", version="", log=""""""
            ),
            class_name="flex flex-col gap-y-8 w-full min-h-[100vh] p-4",
        )
    ]
