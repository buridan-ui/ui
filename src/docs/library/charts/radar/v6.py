import reflex as rx

from src.docs.library.charts.util import (
    info,
    get_tooltip,
)


def radar_v6():
    stats = [
        {"category": "Farming", "score": 7},
        {"category": "Fighting", "score": 6},
        {"category": "Aggressiveness", "score": 7},
        {"category": "Map Awareness", "score": 6},
        {"category": "Objective Control", "score": 6},
        {"category": "Positioning", "score": 7},
    ]

    return rx.box(
        info(
            "Radar Chart - Filled Grid",
            "3",
            "Player performance across key gameplay categories",
            "center",
        ),
        rx.recharts.radar_chart(
            get_tooltip(),
            rx.recharts.polar_grid(
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300 fill-[gray] opacity-20",
                    "text-sm stroke-gray-700 fill-[gray] opacity-20",
                ),
                grid_type="circle",
            ),
            rx.recharts.polar_angle_axis(
                data_key="category",
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300",
                    "text-sm stroke-gray-700",
                ),
                axis_line_type="circle",
            ),
            rx.recharts.radar(
                data_key="score",
                dot=False,
                fill="var(--chart-1)",
                stroke="none",
            ),
            data=stats,
            width="100%",
            height=250,
            margin={"left": 20, "right": 20},
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Performance trends in key gameplay categories",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center [&_.recharts-tooltip-item-separator]:w-full",
    )
