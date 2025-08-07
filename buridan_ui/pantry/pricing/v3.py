import reflex as rx


def check_icon():
    """Reusable check icon component"""
    return rx.box(
        rx.html(
            """<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <polyline points="20,6 9,17 4,12"></polyline>
               </svg>"""
        ),
        class_name="flex items-center justify-center w-5 h-5 bg-blue-1 text-blue-6 rounded-full",
    )


def cross_icon():
    """Reusable cross icon component"""
    return rx.box(
        rx.html(
            """<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M18 6L6 18M6 6l12 12"></path>
               </svg>"""
        ),
        class_name="flex items-center justify-center w-5 h-5 bg-gray-1 text-gray-4 rounded-full",
    )


def feature_item(text: str, included: bool = True):
    """Reusable feature item component"""
    return rx.box(
        check_icon() if included else cross_icon(),
        rx.text(text, class_name="text-gray-7" if included else "text-gray-4"),
        class_name="flex items-center gap-3 text-sm",
    )


def pricing_card(
    title: str,
    description: str,
    price: str,
    price_cents: str = ".00",
    period: str = "USD / monthly",
    features: list = None,
    unavailable_features: list = None,
    is_popular: bool = False,
    button_text: str = "Start free trial",
):
    """Reusable pricing card component"""
    if features is None:
        features = []
    if unavailable_features is None:
        unavailable_features = []

    return rx.box(
        # Card content
        rx.box(
            # Header
            rx.box(
                rx.heading(title, class_name="text-xl font-bold text-gray-9 mb-2"),
                rx.text(description, class_name="text-gray-6 text-sm mb-6"),
                class_name="text-center",
            ),
            # Pricing
            rx.box(
                rx.box(
                    rx.text(
                        price, class_name="text-5xl md:text-6xl font-bold text-gray-9"
                    ),
                    rx.text(price_cents, class_name="text-xl font-bold text-gray-9"),
                    class_name="flex items-end justify-center",
                ),
                rx.text(period, class_name="text-gray-5 text-center mt-2"),
                class_name="mb-8",
            ),
            # Features
            rx.box(
                rx.box(
                    *[feature_item(feature, True) for feature in features],
                    *[feature_item(feature, False) for feature in unavailable_features],
                    class_name="space-y-4",
                ),
                class_name="mb-8",
            ),
            # Footer
            rx.box(
                rx.box(
                    rx.text("Cancel anytime.", class_name="text-xs text-gray-5"),
                    rx.text("No card required.", class_name="text-xs text-gray-5"),
                    class_name="text-center space-y-1 mb-4",
                ),
                rx.button(
                    button_text,
                    class_name=f"""
                        w-full py-3 px-6 rounded-lg font-medium transition-all duration-200
                        {"bg-blue-6 hover:bg-blue-7 text-white shadow-lg hover:shadow-xl" if is_popular else "hover:bg-gray-1 text-gray-8 border-2 border-gray-2 hover:border-gray-3"}
                        disabled:opacity-50 disabled:cursor-not-allowed
                    """,
                ),
            ),
            class_name="p-8",
        ),
        class_name=f"""
            relative rounded-2xl border border-gray-500/40 transition-all duration-300
            {"border-blue-5 shadow-xl" if is_popular else "border-gray-500/40 hover:border-gray-500/50 shadow-lg hover:shadow-xl"}
            hover:-translate-y-1
        """,
    )


def pricing_v3():
    """Main pricing component with improved design and responsiveness"""
    return rx.box(
        rx.container(
            # Header section
            rx.box(
                rx.heading(
                    "Solo, agency or team? We've got you covered.",
                    class_name="text-2xl md:text-3xl lg:text-4xl font-bold text-gray-9 text-center mb-4",
                ),
                rx.text(
                    "Choose the perfect plan for your needs. Upgrade or downgrade at any time.",
                    class_name="text-lg text-gray-6 text-center max-w-2xl mx-auto",
                ),
                class_name="mb-16",
            ),
            # Pricing cards
            rx.box(
                pricing_card(
                    title="Professional",
                    description="Everything a small team needs to get started.",
                    price="$18",
                    features=[
                        "Up to 10 people",
                        "Collect unlimited data",
                        "Code extensibility",
                        "Basic analytics",
                    ],
                    unavailable_features=[
                        "Custom reports",
                        "Priority support",
                        "Advanced integrations",
                    ],
                ),
                pricing_card(
                    title="Teams",
                    description="For growing businesses that need more power.",
                    price="$36",
                    price_cents=".99",
                    features=[
                        "Up to 50 people",
                        "Collect unlimited data",
                        "Code extensibility",
                        "Advanced analytics",
                        "Custom reports",
                        "Priority support",
                        "Advanced integrations",
                    ],
                    is_popular=True,
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-12 max-w-5xl mx-auto",
            ),
            # Additional info
            rx.box(
                rx.text(
                    "All plans include a 14-day free trial. No setup fees. Cancel anytime.",
                    class_name="text-center text-gray-6",
                ),
                rx.box(
                    rx.link(
                        "Questions? Contact our sales team →",
                        class_name="text-blue-6 hover:text-blue-7 font-medium",
                    ),
                    class_name="text-center mt-4",
                ),
                class_name="mt-16",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="py-10 lg:py-20 min-h-screen",
    )
