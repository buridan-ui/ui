import reflex as rx

from buridan_ui.charts.area.v8 import areachart_v8
from buridan_ui.charts.bar.v9 import barchart_v9
from buridan_ui.charts.line.v8 import linechart_v8
from buridan_ui.charts.pie.v1 import piechart_v1
from buridan_ui.charts.radar.v1 import radar_v1
from buridan_ui.charts.doughnut.v2 import doughnutchart_v2
from buridan_ui.charts.scatter.v1 import scatterchart_v1
from buridan_ui.pantry.accordions.v1 import accordion_v1
from buridan_ui.pantry.animations.v1 import animation_v1
from buridan_ui.pantry.backgrounds.v1 import background_v1
from buridan_ui.pantry.cards.v1 import card_v1
from buridan_ui.pantry.faq.v1 import faq_v1
from buridan_ui.pantry.featured.v1 import featured_v1
from buridan_ui.pantry.footers.v1 import footer_v1
from buridan_ui.pantry.forms.v1 import forms_v1
from buridan_ui.pantry.inputs.v1 import input_v1
from buridan_ui.pantry.lists.v1 import lists_v1
from buridan_ui.pantry.logins.v1 import logins_v1
from buridan_ui.pantry.menus.v1 import menus_v1
from buridan_ui.pantry.onboardings.v1 import onboardings_v1
from buridan_ui.pantry.payments.v1 import payments_v1
from buridan_ui.pantry.popups.v1 import popups_v1
from buridan_ui.pantry.pricing.v1 import pricing_v1
from buridan_ui.pantry.prompts.v1 import prompt_v1
from buridan_ui.pantry.sidebars.v1 import sidebar_v1
from buridan_ui.pantry.stats.v2 import stat_v2
from buridan_ui.pantry.subscribe.v1 import subscribe_v1
from buridan_ui.pantry.tables.v4 import tables_v4
from buridan_ui.pantry.tabs.v1 import tab_v1
from buridan_ui.pantry.timeline.v1 import timeline_v1


def get_search_components(dir: str):
    return rx.match(
        dir,
        ("area", areachart_v8()),
        ("bar", barchart_v9()),
        ("line", linechart_v8()),
        ("pie", piechart_v1()),
        ("radar", radar_v1()),
        ("doughnut", doughnutchart_v2()),
        ("scatter", scatterchart_v1()),
        ("accordions", accordion_v1()),
        ("animations", animation_v1()),
        ("backgrounds", background_v1()),
        ("cards", card_v1()),
        ("faq", faq_v1()),
        ("featured", featured_v1()),
        ("footers", footer_v1()),
        ("forms", forms_v1()),
        ("inputs", input_v1()),
        ("lists", lists_v1()),
        ("logins", logins_v1()),
        ("menus", menus_v1()),
        ("onboardings", onboardings_v1()),
        ("payments", payments_v1()),
        ("popups", popups_v1()),
        ("pricing", pricing_v1()),
        ("prompts", prompt_v1()),
        ("sidebars", sidebar_v1()),
        ("stats", stat_v2()),
        ("subscribe", subscribe_v1()),
        ("tables", tables_v4()),
        ("tabs", tab_v1()),
        ("timeline", timeline_v1()),
    )
