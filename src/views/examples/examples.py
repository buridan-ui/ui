import reflex as rx
from typing import Literal
from reflex.experimental import ClientStateVar
from src.docs.library.base_ui.components.base.input_group import input_with_addons
from src.docs.library.base_ui.components.base.button import button
from src.docs.library.base_ui.components.base.badge import badge
import src.hooks as hooks

selected = ClientStateVar.create("selected", "vm")


def checkout_form():
    return rx.el.div(
        rx.el.div(
            rx.form(
                rx.el.div(
                    # Payment Method Section
                    rx.el.fieldset(
                        rx.el.legend(
                            "Payment Method",
                            data_slot="field-legend",
                            data_variant="legend",
                            class_name="mb-3 font-medium data-[variant=legend]:text-base data-[variant=label]:text-sm",
                        ),
                        rx.el.p(
                            "All transactions are secure and encrypted",
                            data_slot="field-description",
                            class_name="text-muted-foreground text-sm leading-normal font-normal group-has-[[data-orientation=horizontal]]/field:text-balance last:mt-0 nth-last-2:-mt-1 [[data-variant=legend]+&]:-mt-1.5 [&>a:hover]:text-primary [&>a]:underline [&>a]:underline-offset-4",
                        ),
                        rx.el.div(
                            # Name on Card
                            rx.el.div(
                                rx.el.label(
                                    "Name on Card",
                                    html_for="checkout-7j9-card-name-43j",
                                    data_slot="field-label",
                                    class_name="items-center text-sm font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50 group/field-label peer/field-label flex w-fit gap-2 leading-snug group-data-[disabled=true]/field:opacity-50 has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col has-[>[data-slot=field]]:rounded-md has-[>[data-slot=field]]:border [&>*]:data-[slot=field]:p-4 has-data-[state=checked]:bg-primary/5 has-data-[state=checked]:border-primary dark:has-data-[state=checked]:bg-primary/10",
                                ),
                                rx.el.input(
                                    id="checkout-7j9-card-name-43j",
                                    placeholder="John Doe",
                                    required=True,
                                    data_slot="input",
                                    class_name="file:text-foreground placeholder:text-muted-foreground selection:bg-primary selection:text-primary-foreground dark:bg-input/30 border-input h-9 w-full min-w-0 rounded-md border bg-transparent px-3 py-1 text-base shadow-xs transition-[color,box-shadow] outline-none file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
                                ),
                                role="group",
                                data_slot="field",
                                data_orientation="vertical",
                                class_name="group/field flex w-full gap-3 data-[invalid=true]:text-destructive flex-col [&>*]:w-full [&>.sr-only]:w-auto",
                            ),
                            # Card Number and CVV Grid
                            rx.el.div(
                                rx.el.div(
                                    rx.el.label(
                                        "Card Number",
                                        html_for="checkout-7j9-card-number-uw1",
                                        data_slot="field-label",
                                        class_name="items-center text-sm font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50 group/field-label peer/field-label flex w-fit gap-2 leading-snug group-data-[disabled=true]/field:opacity-50 has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col has-[>[data-slot=field]]:rounded-md has-[>[data-slot=field]]:border [&>*]:data-[slot=field]:p-4 has-data-[state=checked]:bg-primary/5 has-data-[state=checked]:border-primary dark:has-data-[state=checked]:bg-primary/10",
                                    ),
                                    rx.el.input(
                                        id="checkout-7j9-card-number-uw1",
                                        placeholder="1234 5678 9012 3456",
                                        required=True,
                                        data_slot="input",
                                        class_name="file:text-foreground placeholder:text-muted-foreground selection:bg-primary selection:text-primary-foreground dark:bg-input/30 border-input h-9 w-full min-w-0 rounded-md border bg-transparent px-3 py-1 text-base shadow-xs transition-[color,box-shadow] outline-none file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
                                    ),
                                    rx.el.p(
                                        "Enter your 16-digit number.",
                                        data_slot="field-description",
                                        class_name="text-muted-foreground text-sm leading-normal font-normal group-has-[[data-orientation=horizontal]]/field:text-balance last:mt-0 nth-last-2:-mt-1 [[data-variant=legend]+&]:-mt-1.5 [&>a:hover]:text-primary [&>a]:underline [&>a]:underline-offset-4",
                                    ),
                                    role="group",
                                    data_slot="field",
                                    data_orientation="vertical",
                                    class_name="group/field flex w-full gap-3 data-[invalid=true]:text-destructive flex-col [&>*]:w-full [&>.sr-only]:w-auto col-span-2",
                                ),
                                rx.el.div(
                                    rx.el.label(
                                        "CVV",
                                        html_for="checkout-7j9-cvv",
                                        data_slot="field-label",
                                        class_name="items-center text-sm font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50 group/field-label peer/field-label flex w-fit gap-2 leading-snug group-data-[disabled=true]/field:opacity-50 has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col has-[>[data-slot=field]]:rounded-md has-[>[data-slot=field]]:border [&>*]:data-[slot=field]:p-4 has-data-[state=checked]:bg-primary/5 has-data-[state=checked]:border-primary dark:has-data-[state=checked]:bg-primary/10",
                                    ),
                                    rx.el.input(
                                        id="checkout-7j9-cvv",
                                        placeholder="123",
                                        required=True,
                                        data_slot="input",
                                        class_name="file:text-foreground placeholder:text-muted-foreground selection:bg-primary selection:text-primary-foreground dark:bg-input/30 border-input h-9 w-full min-w-0 rounded-md border bg-transparent px-3 py-1 text-base shadow-xs transition-[color,box-shadow] outline-none file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
                                    ),
                                    role="group",
                                    data_slot="field",
                                    data_orientation="vertical",
                                    class_name="group/field flex w-full gap-3 data-[invalid=true]:text-destructive flex-col [&>*]:w-full [&>.sr-only]:w-auto col-span-1",
                                ),
                                class_name="grid grid-cols-3 gap-4",
                            ),
                            # Month and Year Grid
                            rx.el.div(
                                rx.el.div(
                                    rx.el.label(
                                        "Month",
                                        html_for="checkout-7j9-exp-month-ts6",
                                        data_slot="field-label",
                                        class_name="items-center text-sm font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50 group/field-label peer/field-label flex w-fit gap-2 leading-snug group-data-[disabled=true]/field:opacity-50 has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col has-[>[data-slot=field]]:rounded-md has-[>[data-slot=field]]:border [&>*]:data-[slot=field]:p-4 has-data-[state=checked]:bg-primary/5 has-data-[state=checked]:border-primary dark:has-data-[state=checked]:bg-primary/10",
                                    ),
                                    rx.el.select(
                                        rx.el.option(
                                            "MM", value="", disabled=True, selected=True
                                        ),
                                        rx.el.option("01", value="01"),
                                        rx.el.option("02", value="02"),
                                        rx.el.option("03", value="03"),
                                        rx.el.option("04", value="04"),
                                        rx.el.option("05", value="05"),
                                        rx.el.option("06", value="06"),
                                        rx.el.option("07", value="07"),
                                        rx.el.option("08", value="08"),
                                        rx.el.option("09", value="09"),
                                        rx.el.option("10", value="10"),
                                        rx.el.option("11", value="11"),
                                        rx.el.option("12", value="12"),
                                        id="checkout-7j9-exp-month-ts6",
                                        class_name="border-input data-[placeholder]:text-muted-foreground dark:bg-input/30 flex w-full items-center justify-between gap-2 rounded-md border bg-transparent px-3 py-2 text-sm shadow-xs transition-[color,box-shadow] outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50 h-9",
                                    ),
                                    role="group",
                                    data_slot="field",
                                    data_orientation="vertical",
                                    class_name="group/field flex w-full gap-3 data-[invalid=true]:text-destructive flex-col [&>*]:w-full [&>.sr-only]:w-auto",
                                ),
                                rx.el.div(
                                    rx.el.label(
                                        "Year",
                                        html_for="checkout-7j9-exp-year-f59",
                                        data_slot="field-label",
                                        class_name="items-center text-sm font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50 group/field-label peer/field-label flex w-fit gap-2 leading-snug group-data-[disabled=true]/field:opacity-50 has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col has-[>[data-slot=field]]:rounded-md has-[>[data-slot=field]]:border [&>*]:data-[slot=field]:p-4 has-data-[state=checked]:bg-primary/5 has-data-[state=checked]:border-primary dark:has-data-[state=checked]:bg-primary/10",
                                    ),
                                    rx.el.select(
                                        rx.el.option(
                                            "YYYY",
                                            value="",
                                            disabled=True,
                                            selected=True,
                                        ),
                                        rx.el.option("2024", value="2024"),
                                        rx.el.option("2025", value="2025"),
                                        rx.el.option("2026", value="2026"),
                                        rx.el.option("2027", value="2027"),
                                        rx.el.option("2028", value="2028"),
                                        rx.el.option("2029", value="2029"),
                                        id="checkout-7j9-exp-year-f59",
                                        class_name="border-input data-[placeholder]:text-muted-foreground dark:bg-input/30 flex w-full items-center justify-between gap-2 rounded-md border bg-transparent px-3 py-2 text-sm shadow-xs transition-[color,box-shadow] outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50 h-9",
                                    ),
                                    role="group",
                                    data_slot="field",
                                    data_orientation="vertical",
                                    class_name="group/field flex w-full gap-3 data-[invalid=true]:text-destructive flex-col [&>*]:w-full [&>.sr-only]:w-auto",
                                ),
                                class_name="grid grid-cols-2 gap-4",
                            ),
                            data_slot="field-group",
                            class_name="group/field-group @container/field-group flex w-full flex-col gap-7 data-[slot=checkbox-group]:gap-3 [&>[data-slot=field-group]]:gap-4",
                        ),
                        data_slot="field-set",
                        class_name="flex flex-col gap-6 has-[>[data-slot=checkbox-group]]:gap-3 has-[>[data-slot=radio-group]]:gap-3",
                    ),
                    # Separator
                    rx.el.div(
                        rx.el.div(
                            data_orientation="horizontal",
                            role="none",
                            data_slot="separator",
                            class_name="bg-border shrink-0 data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full data-[orientation=vertical]:h-full data-[orientation=vertical]:w-px absolute inset-0 top-1/2",
                        ),
                        data_slot="field-separator",
                        data_content="false",
                        class_name="relative -my-2 h-5 text-sm group-data-[variant=outline]/field-group:-mb-2",
                    ),
                    # Billing Address Section
                    rx.el.fieldset(
                        rx.el.legend(
                            "Billing Address",
                            data_slot="field-legend",
                            data_variant="legend",
                            class_name="mb-3 font-medium data-[variant=legend]:text-base data-[variant=label]:text-sm",
                        ),
                        rx.el.p(
                            "The billing address associated with your payment method",
                            data_slot="field-description",
                            class_name="text-muted-foreground text-sm leading-normal font-normal group-has-[[data-orientation=horizontal]]/field:text-balance last:mt-0 nth-last-2:-mt-1 [[data-variant=legend]+&]:-mt-1.5 [&>a:hover]:text-primary [&>a]:underline [&>a]:underline-offset-4",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.input(
                                    type="checkbox",
                                    id="checkout-7j9-same-as-shipping-wgm",
                                    checked=True,
                                    class_name="peer border-input dark:bg-input/30 size-4 shrink-0 rounded-[4px] border shadow-xs transition-shadow outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50",
                                ),
                                rx.el.label(
                                    "Same as shipping address",
                                    html_for="checkout-7j9-same-as-shipping-wgm",
                                    data_slot="field-label",
                                    class_name="items-center text-sm select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50 group/field-label peer/field-label flex w-fit gap-2 leading-snug group-data-[disabled=true]/field:opacity-50 has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col has-[>[data-slot=field]]:rounded-md has-[>[data-slot=field]]:border [&>*]:data-[slot=field]:p-4 has-data-[state=checked]:bg-primary/5 has-data-[state=checked]:border-primary dark:has-data-[state=checked]:bg-primary/10 font-normal",
                                ),
                                role="group",
                                data_slot="field",
                                data_orientation="horizontal",
                                class_name="group/field flex w-full gap-3 data-[invalid=true]:text-destructive flex-row items-center [&>[data-slot=field-label]]:flex-auto has-[>[data-slot=field-content]]:items-start has-[>[data-slot=field-content]]:[&>[role=checkbox],[role=radio]]:mt-px",
                            ),
                            data_slot="field-group",
                            class_name="group/field-group @container/field-group flex w-full flex-col gap-7 data-[slot=checkbox-group]:gap-3 [&>[data-slot=field-group]]:gap-4",
                        ),
                        data_slot="field-set",
                        class_name="flex flex-col gap-6 has-[>[data-slot=checkbox-group]]:gap-3 has-[>[data-slot=radio-group]]:gap-3",
                    ),
                    # Separator
                    rx.el.div(
                        rx.el.div(
                            data_orientation="horizontal",
                            role="none",
                            data_slot="separator",
                            class_name="bg-border shrink-0 data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full data-[orientation=vertical]:h-full data-[orientation=vertical]:w-px absolute inset-0 top-1/2",
                        ),
                        data_slot="field-separator",
                        data_content="false",
                        class_name="relative -my-2 h-5 text-sm group-data-[variant=outline]/field-group:-mb-2",
                    ),
                    # Comments Section
                    rx.el.fieldset(
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Comments",
                                    html_for="checkout-7j9-optional-comments",
                                    data_slot="field-label",
                                    class_name="items-center text-sm font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50 group/field-label peer/field-label flex w-fit gap-2 leading-snug group-data-[disabled=true]/field:opacity-50 has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col has-[>[data-slot=field]]:rounded-md has-[>[data-slot=field]]:border [&>*]:data-[slot=field]:p-4 has-data-[state=checked]:bg-primary/5 has-data-[state=checked]:border-primary dark:has-data-[state=checked]:bg-primary/10",
                                ),
                                rx.el.textarea(
                                    id="checkout-7j9-optional-comments",
                                    placeholder="Add any additional comments",
                                    data_slot="textarea",
                                    class_name="border-input placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive dark:bg-input/30 flex field-sizing-content min-h-16 w-full rounded-md border bg-transparent px-3 py-2 text-base shadow-xs transition-[color,box-shadow] outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
                                ),
                                role="group",
                                data_slot="field",
                                data_orientation="vertical",
                                class_name="group/field flex w-full gap-3 data-[invalid=true]:text-destructive flex-col [&>*]:w-full [&>.sr-only]:w-auto",
                            ),
                            data_slot="field-group",
                            class_name="group/field-group @container/field-group flex w-full flex-col gap-7 data-[slot=checkbox-group]:gap-3 [&>[data-slot=field-group]]:gap-4",
                        ),
                        data_slot="field-set",
                        class_name="flex flex-col gap-6 has-[>[data-slot=checkbox-group]]:gap-3 has-[>[data-slot=radio-group]]:gap-3",
                    ),
                    # Submit and Cancel Buttons
                    rx.el.div(
                        button("Submit"),
                        button("Cancel", variant="outline"),
                        class_name="flex flex-row items-center gap-x-4 [&>[data-slot=field-label]]:flex-auto has-[>[data-slot=field-content]]:items-start has-[>[data-slot=field-content]]:[&>[role=checkbox],[role=radio]]:mt-px",
                    ),
                    data_slot="field-group",
                    class_name="group/field-group @container/field-group flex w-full flex-col gap-7 data-[slot=checkbox-group]:gap-3 [&>[data-slot=field-group]]:gap-4",
                ),
                class_name="w-full rounded-lg border border-[var(--input)] p-6",
            ),
            class_name="flex flex-col gap-6 *:[div]:w-full *:[div]:max-w-full",
        ),
    )


def input_group():
    return rx.el.div(
        rx.el.textarea(
            data_slot="input-group-control",
            class_name="border-input placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive flex field-sizing-content min-h-16 w-full px-3 text-base transition-[color,box-shadow] outline-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm flex-1 resize-none rounded-none border-0 bg-transparent py-3 shadow-none focus-visible:ring-0 dark:bg-transparent",
            placeholder="Ask, Search or Chat...",
        ),
        rx.el.div(
            rx.el.button(
                rx.html(
                    """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-plus "><path d="M12 5l0 14"></path><path d="M5 12l14 0"></path></svg>"""
                ),
                data_slot="button",
                class_name="justify-center whitespace-nowrap font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive border bg-background hover:bg-accent hover:text-accent-foreground dark:bg-input/30 dark:border-input dark:hover:bg-input/50 text-sm shadow-none flex gap-2 items-center size-6 p-0 has-[>svg]:p-0 rounded-full",
                type="button",
                data_size="icon-xs",
                aria_label="Add",
            ),
            rx.el.button(
                "Auto",
                data_slot="dropdown-menu-trigger",
                class_name="justify-center whitespace-nowrap font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50 py-2 text-sm shadow-none flex items-center h-6 gap-1 px-2 rounded-[calc(var(--radius)-5px)] [&>svg:not([class*='size-'])]:size-3.5 has-[>svg]:px-2",
                type="button",
                data_size="xs",
                id="radix-«rhm»",
                aria_haspopup="menu",
                aria_expanded="false",
                data_state="closed",
            ),
            rx.el.span(
                "52% used",
                class_name="text-muted-foreground flex items-center gap-2 text-sm [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 ml-auto",
            ),
            rx.el.div(
                data_orientation="vertical",
                role="none",
                data_slot="separator",
                class_name="bg-border shrink-0 data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full data-[orientation=vertical]:h-full data-[orientation=vertical]:w-px !h-4",
            ),
            rx.el.button(
                rx.html(
                    """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-up"><path d="m5 12 7-7 7 7"></path><path d="M12 19V5"></path></svg>"""
                ),
                rx.el.span("Send", class_name="sr-only"),
                data_slot="button",
                class_name="justify-center whitespace-nowrap font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive bg-primary text-primary-foreground hover:bg-primary/90 text-sm shadow-none flex gap-2 items-center size-6 p-0 has-[>svg]:p-0 rounded-full",
                type="button",
                data_size="icon-xs",
            ),
            role="group",
            data_slot="input-group-addon",
            data_align="block-end",
            class_name="text-muted-foreground flex h-auto cursor-text items-center gap-2 py-1.5 text-sm font-medium select-none [&>svg:not([class*='size-'])]:size-4 [&>kbd]:rounded-[calc(var(--radius)-5px)] group-data-[disabled=true]/input-group:opacity-50 order-last w-full justify-start px-3 pb-3 [.border-t]:pt-3 group-has-[>input]/input-group:pb-2.5",
        ),
        data_slot="input-group",
        role="group",
        class_name="group/input-group border-input dark:bg-input/30 relative flex w-full items-center rounded-md border shadow-xs transition-[color,box-shadow] outline-none h-9 min-w-0 has-[>textarea]:h-auto has-[>[data-align=inline-start]]:[&>input]:pl-2 has-[>[data-align=inline-end]]:[&>input]:pr-2 has-[>[data-align=block-start]]:h-auto has-[>[data-align=block-start]]:flex-col has-[>[data-align=block-start]]:[&>input]:pb-3 has-[>[data-align=block-end]]:h-auto has-[>[data-align=block-end]]:flex-col has-[>[data-align=block-end]]:[&>input]:pt-3 has-[[data-slot=input-group-control]:focus-visible]:border-ring has-[[data-slot=input-group-control]:focus-visible]:ring-ring/50 has-[[data-slot=input-group-control]:focus-visible]:ring-[3px] has-[[data-slot][aria-invalid=true]]:ring-destructive/20 has-[[data-slot][aria-invalid=true]]:border-destructive dark:has-[[data-slot][aria-invalid=true]]:ring-destructive/40",
    )


class CheckboxState(rx.State):
    social_media: bool = True
    search_engine: bool = False
    referral: bool = False
    other: bool = False

    def toggle_social_media(self):
        self.social_media = not self.social_media

    def toggle_search_engine(self):
        self.search_engine = not self.search_engine

    def toggle_referral(self):
        self.referral = not self.referral

    def toggle_other(self):
        self.other = not self.other


def checkbox_button(id_val: str, value: str, label: str, is_checked: bool, on_click):
    return rx.el.label(
        rx.el.div(
            rx.el.button(
                rx.cond(is_checked, rx.icon("check", size=12), rx.fragment()),
                type="button",
                role="checkbox",
                aria_checked=rx.cond(is_checked, "true", "false"),
                data_state=rx.cond(is_checked, "checked", "unchecked"),
                value=value,
                data_slot="checkbox",
                id=id_val,
                on_click=on_click,
                class_name="peer dark:bg-input/30 data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground dark:data-[state=checked]:bg-primary data-[state=checked]:border-input focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive size-4 shrink-0 border shadow-xs outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50 -ml-6 -translate-x-1 rounded-full transition-all duration-100 ease-linear data-[state=checked]:ml-0 data-[state=checked]:translate-x-0 flex items-center justify-center",
            ),
            rx.el.input(
                type="checkbox",
                value=value,
                checked=is_checked,
                aria_hidden="true",
                tab_index=-1,
                style={
                    "position": "absolute",
                    "pointer-events": "none",
                    "opacity": "0",
                    "margin": "0px",
                    "transform": "translateX(-100%)",
                    "width": "16px",
                    "height": "16px",
                },
            ),
            rx.el.div(
                label,
                data_slot="field-label",
                class_name="flex w-fit items-center gap-2 text-sm leading-snug font-medium group-data-[disabled=true]/field:opacity-50",
            ),
            role="group",
            data_slot="field",
            data_orientation="horizontal",
            class_name="group/field flex w-full data-[invalid=true]:text-destructive flex-row items-center [&>[data-slot=field-label]]:flex-auto has-[>[data-slot=field-content]]:items-start has-[>[data-slot=field-content]]:[&>[role=checkbox],[role=radio]]:mt-px gap-1.5 overflow-hidden !px-3 !py-1.5 transition-all duration-100 ease-linear group-has-data-[state=checked]/field-label:!px-2",
        ),
        html_for=id_val,
        data_slot="field-label",
        data_state=rx.cond(is_checked, "checked", "unchecked"),
        class_name="items-center text-sm font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50 group/field-label peer/field-label flex w-fit gap-2 leading-snug group-data-[disabled=true]/field:opacity-50 has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col has-[>[data-slot=field]]:rounded-md has-[>[data-slot=field]]:border [&>*]:data-[slot=field]:p-4 has-data-[state=checked]:bg-primary/5 border-input has-data-[state=checked]:border-input dark:has-data-[state=checked]:bg-primary/10 !w-fit",
    )


def checkbox_form():
    return rx.el.div(
        rx.form(
            rx.el.div(
                rx.el.fieldset(
                    rx.el.legend(
                        "How did you hear about us?",
                        data_slot="field-legend",
                        data_variant="legend",
                        class_name="mb-3 font-medium data-[variant=legend]:text-base data-[variant=label]:text-sm",
                    ),
                    rx.el.p(
                        "Select the option that best describes how you heard about us.",
                        data_slot="field-description",
                        class_name="text-muted-foreground text-sm leading-normal font-normal group-has-[[data-orientation=horizontal]]/field:text-balance last:mt-0 nth-last-2:-mt-1 [[data-variant=legend]+&]:-mt-1.5 [&>a:hover]:text-primary [&>a]:underline [&>a]:underline-offset-4 line-clamp-1",
                    ),
                    rx.el.div(
                        checkbox_button(
                            "social-media",
                            "social-media",
                            "Social Media",
                            CheckboxState.social_media,
                            CheckboxState.toggle_social_media,
                        ),
                        checkbox_button(
                            "search-engine",
                            "search-engine",
                            "Search Engine",
                            CheckboxState.search_engine,
                            CheckboxState.toggle_search_engine,
                        ),
                        checkbox_button(
                            "referral",
                            "referral",
                            "Referral",
                            CheckboxState.referral,
                            CheckboxState.toggle_referral,
                        ),
                        checkbox_button(
                            "other",
                            "other",
                            "Other",
                            CheckboxState.other,
                            CheckboxState.toggle_other,
                        ),
                        data_slot="field-group",
                        class_name="group/field-group @container/field-group w-full data-[slot=checkbox-group]:gap-3 [&>[data-slot=field-group]]:gap-4 flex flex-row flex-wrap gap-2 [--radius:9999rem]",
                    ),
                    data_slot="field-set",
                    class_name="flex flex-col has-[>[data-slot=checkbox-group]]:gap-3 has-[>[data-slot=radio-group]]:gap-3 gap-4",
                ),
                data_slot="field-group",
                class_name="group/field-group @container/field-group flex w-full flex-col gap-7 data-[slot=checkbox-group]:gap-3 [&>[data-slot=field-group]]:gap-4",
            ),
        ),
        data_slot="card-content",
    )


def input_type_one():
    return input_with_addons(
        prefix=rx.icon("search", size=14),
        placeholder="Search...",
        suffix="12 results",
        class_name="pl-2",
    )


def input_type_two():
    return input_with_addons(
        placeholder="@buridan",
        suffix=button(
            rx.icon("check", size=10),
            size="icon-sm",
            class_name="!size-4 !rounded-full !flex !items-center !justify-center",
        ),
        class_name="pr-2",
    )


def input_type_three():
    return input_with_addons(
        prefix="https://",
        placeholder="example.com",
        suffix=rx.tooltip(
            rx.icon("info", size=14),
            content="This is content in a tooltip.",
            class_name="text-sm py-1.5 font-medium",
        ),
        class_name="pr-2",
    )


def button_group(
    *children,
    orientation: Literal["horizontal", "vertical"] = "horizontal",
    class_name: str = "",
    **props,
):
    """
    Button group component for grouping related buttons together.
    Uses CSS variables from your shadcn theme.

    Args:
        *children: Button elements to group
        orientation: Layout direction (horizontal or vertical)
        class_name: Additional classes
        **props: Additional props for the group element
    """
    base_classes = (
        "flex w-fit items-stretch [&>*]:focus-visible:z-10 [&>*]:focus-visible:relative "
        "[&>[data-slot=select-trigger]:not([class*='w-'])]:w-fit [&>input]:flex-1 "
        "has-[select[aria-hidden=true]:last-child]:[&>[data-slot=select-trigger]:last-of-type]:rounded-r-md "
        "has-[>[data-slot=button-group]]:gap-2"
    )

    orientation_classes = {
        "horizontal": (
            "[&>*:not(:first-child)]:rounded-l-none [&>*:not(:first-child)]:border-l-0 "
            "[&>*:not(:last-child)]:rounded-r-none"
        ),
        "vertical": (
            "flex-col [&>*:not(:first-child)]:rounded-t-none [&>*:not(:first-child)]:border-t-0 "
            "[&>*:not(:last-child)]:rounded-b-none"
        ),
    }

    return rx.box(
        *children,
        role="group",
        data_slot="button-group",
        data_orientation=orientation,
        class_name=f"{base_classes} {orientation_classes[orientation]} {class_name}".strip(),
        **props,
    )


def button_group_text(*children, class_name: str = "", **props):
    """
    Text/label element for button groups.
    Used for displaying static text alongside buttons.

    Args:
        *children: Text or icon content
        class_name: Additional classes
        **props: Additional props
    """
    base_classes = (
        "bg-[var(--muted)] flex items-center gap-2 rounded-md border px-4 text-sm font-medium "
        "shadow-xs [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4"
    )

    return rx.box(*children, class_name=f"{base_classes} {class_name}".strip(), **props)


def button_group_separator(
    orientation: Literal["horizontal", "vertical"] = "vertical",
    class_name: str = "",
    **props,
):
    """
    Separator line between button group elements.

    Args:
        orientation: Separator direction
        class_name: Additional classes
        **props: Additional props
    """
    base_classes = (
        "bg-[var(--input)] relative !m-0 self-stretch "
        "data-[orientation=vertical]:h-auto"
    )

    # Use rx.divider for the separator
    return rx.divider(
        data_slot="button-group-separator",
        orientation=orientation,
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def button_group_demo():
    """Basic button group example"""
    return rx.box(
        button_group(
            rx.el.button(
                "First",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "bg-[var(--primary)] text-[var(--primary-foreground)] "
                    "hover:bg-[var(--primary)]/90 h-9 px-4 py-2 text-sm font-medium "
                    "transition-all outline-none border border-transparent"
                ),
            ),
            rx.el.button(
                "Second",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "bg-[var(--primary)] text-[var(--primary-foreground)] "
                    "hover:bg-[var(--primary)]/90 h-9 px-4 py-2 text-sm font-medium "
                    "transition-all outline-none border border-transparent"
                ),
            ),
            rx.el.button(
                "Third",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "bg-[var(--primary)] text-[var(--primary-foreground)] "
                    "hover:bg-[var(--primary)]/90 h-9 px-4 py-2 text-sm font-medium "
                    "transition-all outline-none border border-transparent"
                ),
            ),
        ),
    )


def button_group_outline():
    """Button group with outline variant"""
    return rx.box(
        button_group(
            rx.el.button(
                "Copy",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "border bg-[var(--background)] shadow-xs hover:bg-[var(--accent)] "
                    "hover:text-[var(--accent-foreground)] "
                    "dark:bg-[var(--input)]/30 dark:border-[var(--input)] "
                    "dark:hover:bg-[var(--input)]/50 "
                    "h-9 px-4 py-2 text-sm font-medium transition-all outline-none"
                ),
            ),
            rx.el.button(
                "Cut",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "border bg-[var(--background)] shadow-xs hover:bg-[var(--accent)] "
                    "hover:text-[var(--accent-foreground)] "
                    "dark:bg-[var(--input)]/30 dark:border-[var(--input)] "
                    "dark:hover:bg-[var(--input)]/50 "
                    "h-9 px-4 py-2 text-sm font-medium transition-all outline-none"
                ),
            ),
            rx.el.button(
                "Paste",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "border bg-[var(--background)] shadow-xs hover:bg-[var(--accent)] "
                    "hover:text-[var(--accent-foreground)] "
                    "dark:bg-[var(--input)]/30 dark:border-[var(--input)] "
                    "dark:hover:bg-[var(--input)]/50 "
                    "h-9 px-4 py-2 text-sm font-medium transition-all outline-none"
                ),
            ),
        ),
    )


def button_group_with_separator():
    """Button group with separators"""
    return rx.box(
        button_group(
            rx.el.button(
                "Bold",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "border bg-[var(--background)] shadow-xs hover:bg-[var(--accent)] "
                    "hover:text-[var(--accent-foreground)] "
                    "dark:bg-[var(--input)]/30 dark:border-[var(--input)] "
                    "dark:hover:bg-[var(--input)]/50 "
                    "h-9 px-4 py-2 text-sm font-medium transition-all outline-none"
                ),
            ),
            button_group_separator(),
            rx.el.button(
                "Italic",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "border bg-[var(--background)] shadow-xs hover:bg-[var(--accent)] "
                    "hover:text-[var(--accent-foreground)] "
                    "dark:bg-[var(--input)]/30 dark:border-[var(--input)] "
                    "dark:hover:bg-[var(--input)]/50 "
                    "h-9 px-4 py-2 text-sm font-medium transition-all outline-none"
                ),
            ),
            button_group_separator(),
            rx.el.button(
                "Underline",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "border bg-[var(--background)] shadow-xs hover:bg-[var(--accent)] "
                    "hover:text-[var(--accent-foreground)] "
                    "dark:bg-[var(--input)]/30 dark:border-[var(--input)] "
                    "dark:hover:bg-[var(--input)]/50 "
                    "h-9 px-4 py-2 text-sm font-medium transition-all outline-none"
                ),
            ),
        ),
    )


def button_group_with_text():
    """Button group with text label"""
    return rx.box(
        button_group(
            rx.el.button(
                "Name",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "border bg-[var(--background)] shadow-xs hover:bg-[var(--accent)] "
                    "hover:text-[var(--accent-foreground)] "
                    "dark:bg-[var(--input)]/30 dark:border-[var(--input)] "
                    "dark:hover:bg-[var(--input)]/50 "
                    "h-9 px-4 py-2 text-sm font-medium transition-all outline-none"
                ),
            ),
            rx.el.button(
                "Date",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "border bg-[var(--background)] shadow-xs hover:bg-[var(--accent)] "
                    "hover:text-[var(--accent-foreground)] "
                    "dark:bg-[var(--input)]/30 dark:border-[var(--input)] "
                    "dark:hover:bg-[var(--input)]/50 "
                    "h-9 px-4 py-2 text-sm font-medium transition-all outline-none"
                ),
            ),
            rx.el.button(
                "Size",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "border bg-[var(--background)] shadow-xs hover:bg-[var(--accent)] "
                    "hover:text-[var(--accent-foreground)] "
                    "dark:bg-[var(--input)]/30 dark:border-[var(--input)] "
                    "dark:hover:bg-[var(--input)]/50 "
                    "h-9 px-4 py-2 text-sm font-medium transition-all outline-none"
                ),
            ),
        ),
    )


def button_group_vertical():
    """Vertical button group"""
    return rx.box(
        button_group(
            rx.el.button(
                "Top",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "border bg-[var(--background)] shadow-xs hover:bg-[var(--accent)] "
                    "hover:text-[var(--accent-foreground)] "
                    "dark:bg-[var(--input)]/30 dark:border-[var(--input)] "
                    "dark:hover:bg-[var(--input)]/50 "
                    "h-9 px-4 py-2 text-sm font-medium transition-all outline-none"
                ),
            ),
            rx.el.button(
                "Middle",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "border bg-[var(--background)] shadow-xs hover:bg-[var(--accent)] "
                    "hover:text-[var(--accent-foreground)] "
                    "dark:bg-[var(--input)]/30 dark:border-[var(--input)] "
                    "dark:hover:bg-[var(--input)]/50 "
                    "h-9 px-4 py-2 text-sm font-medium transition-all outline-none"
                ),
            ),
            rx.el.button(
                "Bottom",
                class_name=(
                    "inline-flex items-center justify-center gap-2 rounded-md "
                    "border bg-[var(--background)] shadow-xs hover:bg-[var(--accent)] "
                    "hover:text-[var(--accent-foreground)] "
                    "dark:bg-[var(--input)]/30 dark:border-[var(--input)] "
                    "dark:hover:bg-[var(--input)]/50 "
                    "h-9 px-4 py-2 text-sm font-medium transition-all outline-none"
                ),
            ),
            orientation="vertical",
        ),
    )


def component():
    return rx.el.div(
        rx.el.div(
            # Icon / Avatar group
            rx.el.div(
                rx.el.div(
                    # Avatar 1
                    rx.el.span(
                        rx.el.img(
                            data_slot="avatar-image",
                            class_name="aspect-square size-full",
                            src="https://avatars.githubusercontent.com/u/84860195?v=4",
                        ),
                        data_slot="avatar",
                        class_name="relative flex size-8 shrink-0 overflow-hidden rounded-full",
                    ),
                    # Avatar 2
                    rx.el.span(
                        rx.el.img(
                            data_slot="avatar-image",
                            class_name="aspect-square size-full",
                            src="https://avatars.githubusercontent.com/u/198465274?s=200&v=4",
                        ),
                        data_slot="avatar",
                        class_name="relative flex size-8 shrink-0 overflow-hidden rounded-full",
                    ),
                    # Avatar 3
                    rx.el.span(
                        rx.el.img(
                            data_slot="avatar-image",
                            class_name="aspect-square size-full",
                            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
                        ),
                        data_slot="avatar",
                        class_name="relative flex size-8 shrink-0 overflow-hidden rounded-full",
                    ),
                    class_name=(
                        "*:data-[slot=avatar]:ring-background flex -space-x-2 "
                        "*:data-[slot=avatar]:size-12 *:data-[slot=avatar]:ring-2 "
                        "*:data-[slot=avatar]:grayscale"
                    ),
                ),
                data_slot="empty-icon",
                data_variant="default",
                class_name=(
                    "flex shrink-0 items-center justify-center mb-2 "
                    "[&_svg]:pointer-events-none [&_svg]:shrink-0 bg-transparent"
                ),
            ),
            # Title
            rx.el.div(
                "No Team Members",
                data_slot="empty-title",
                class_name="text-lg font-medium tracking-tight",
            ),
            # Description
            rx.el.div(
                "Invite your team to collaborate on this project.",
                data_slot="empty-description",
                class_name=(
                    "text-muted-foreground [&>a:hover]:text-primary text-sm/relaxed "
                    "[&>a]:underline [&>a]:underline-offset-4"
                ),
            ),
            data_slot="empty-header",
            class_name="flex max-w-sm flex-col items-center gap-2 text-center",
        ),
        # === Content Section ===
        rx.el.div(
            rx.el.button(
                "Invite Members",
                data_slot="button",
                class_name=(
                    "inline-flex items-center justify-center whitespace-nowrap text-sm font-medium "
                    "transition-all disabled:pointer-events-none disabled:opacity-50 "
                    "[&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 "
                    "shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring "
                    "focus-visible:ring-ring/50 focus-visible:ring-[3px] "
                    "aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 "
                    "aria-invalid:border-destructive bg-primary text-primary-foreground "
                    "hover:bg-primary/90 h-8 rounded-md gap-1.5 px-3 has-[>svg]:px-2.5"
                ),
            ),
            data_slot="empty-content",
            class_name=(
                "flex w-full max-w-sm min-w-0 flex-col items-center gap-4 "
                "text-sm text-balance"
            ),
        ),
        # === Root Wrapper ===
        data_slot="empty",
        class_name=(
            "flex min-w-0 flex-col items-center justify-center gap-6 rounded-lg border-dashed "
            "p-6 text-center text-balance md:p-12 flex-none border border-input"
        ),
    )


def component_two():
    return rx.el.fieldset(
        rx.el.legend(
            "Compute Environment",
            data_slot="field-legend",
            data_variant="legend",
            class_name="mb-3 font-medium data-[variant=legend]:text-base data-[variant=label]:text-sm",
        ),
        rx.el.p(
            "Select the compute environment for your cluster.",
            data_slot="field-description",
            class_name="text-muted-foreground text-sm leading-normal font-normal group-has-[[data-orientation=horizontal]]/field:text-balance last:mt-0 nth-last-2:-mt-1 [[data-variant=legend]+&]:-mt-1.5 [&>a:hover]:text-primary [&>a]:underline [&>a]:underline-offset-4",
        ),
        rx.el.div(
            rx.el.label(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            "Kubernetes",
                            data_slot="field-label",
                            class_name="flex w-fit items-center gap-2 text-sm leading-snug font-medium group-data-[disabled=true]/field:opacity-50",
                        ),
                        rx.el.p(
                            "Run GPU workloads on a K8s configured cluster. This is the default.",
                            data_slot="field-description",
                            class_name="text-muted-foreground text-sm leading-normal font-normal group-has-[[data-orientation=horizontal]]/field:text-balance last:mt-0 nth-last-2:-mt-1 [[data-variant=legend]+&]:-mt-1.5 [&>a:hover]:text-primary [&>a]:underline [&>a]:underline-offset-4",
                        ),
                        data_slot="field-content",
                        class_name="group/field-content flex flex-1 flex-col gap-1.5 leading-snug",
                    ),
                    rx.el.input(
                        type="radio",
                        role="radio",
                        checked=selected.value == "kubernetes",
                        data_state=rx.cond(
                            selected.value == "kubernetes", "checked", "unchecked"
                        ),
                        value="kubernetes",
                        data_slot="radio-group-item",
                        class_name="accent-primary border-input text-primary focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive dark:bg-input/30 aspect-square size-4 shrink-0 rounded-full border shadow-xs transition-[color,box-shadow] outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50",
                        id="kubernetes-r2h",
                        aria_label="Kubernetes",
                        tab_index=0,
                        data_radix_collection_item=True,
                        on_click=selected.set_value("kubernetes"),
                    ),
                    role="group",
                    data_slot="field",
                    data_orientation="horizontal",
                    class_name="group/field flex w-full gap-3 data-[invalid=true]:text-destructive flex-row items-center [&>[data-slot=field-label]]:flex-auto has-[>[data-slot=field-content]]:items-start has-[>[data-slot=field-content]]:[&>[role=checkbox],[role=radio]]:mt-px",
                ),
                data_slot="field-label",
                class_name="items-center border border-input text-sm font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50 group/field-label peer/field-label flex w-fit gap-2 leading-snug group-data-[disabled=true]/field:opacity-50 has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col has-[>[data-slot=field]]:rounded-md has-[>[data-slot=field]]:border [&>*]:data-[slot=field]:p-4 has-data-[state=checked]:bg-primary/5 has-data-[state=checked]:border-primary dark:has-data-[state=checked]:bg-primary/10",
                html_for="kubernetes-r2h",
            ),
            rx.el.label(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            "Virtual Machine",
                            data_slot="field-label",
                            class_name="flex w-fit items-center gap-2 text-sm leading-snug font-medium group-data-[disabled=true]/field:opacity-50",
                        ),
                        rx.el.p(
                            "Access a VM configured cluster to run workloads. (Coming soon)",
                            data_slot="field-description",
                            class_name="text-muted-foreground text-sm leading-normal font-normal group-has-[[data-orientation=horizontal]]/field:text-balance last:mt-0 nth-last-2:-mt-1 [[data-variant=legend]+&]:-mt-1.5 [&>a:hover]:text-primary [&>a]:underline [&>a]:underline-offset-4",
                        ),
                        data_slot="field-content",
                        class_name="group/field-content flex flex-1 flex-col gap-1.5 leading-snug",
                    ),
                    rx.el.input(
                        type="radio",
                        role="radio",
                        checked=selected.value == "vm",
                        data_state=rx.cond(
                            selected.value == "vm", "checked", "unchecked"
                        ),
                        value="vm",
                        data_slot="radio-group-item",
                        class_name="accent-primary border-input text-primary focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive dark:bg-input/30 aspect-square size-4 shrink-0 rounded-full border shadow-xs transition-[color,box-shadow] outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50",
                        id="vm-z4k",
                        aria_label="Virtual Machine",
                        tab_index=-1,
                        data_radix_collection_item=True,
                        on_click=selected.set_value("vm"),
                    ),
                    role="group",
                    data_slot="field",
                    data_orientation="horizontal",
                    class_name="group/field flex w-full gap-3 data-[invalid=true]:text-destructive flex-row items-center [&>[data-slot=field-label]]:flex-auto has-[>[data-slot=field-content]]:items-start has-[>[data-slot=field-content]]:[&>[role=checkbox],[role=radio]]:mt-px",
                ),
                data_slot="field-label",
                class_name="items-center border border-input text-sm font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50 group/field-label peer/field-label flex w-fit gap-2 leading-snug group-data-[disabled=true]/field:opacity-50 has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col has-[>[data-slot=field]]:rounded-md has-[>[data-slot=field]]:border [&>*]:data-[slot=field]:p-4 has-data-[state=checked]:bg-primary/5 has-data-[state=checked]:border-primary dark:has-data-[state=checked]:bg-primary/10",
                html_for="vm-z4k",
            ),
            role="radiogroup",
            aria_required=False,
            dir="ltr",
            data_slot="radio-group",
            class_name="grid gap-3",
            tab_index=0,
            style={"outline": "none"},
        ),
        data_slot="field-set",
        class_name="flex flex-col gap-4 has-[>[data-slot=checkbox-group]]:gap-3 has-[>[data-slot=radio-group]]:gap-3 p-2",
    )


def loading_empty_state():
    """Empty state component with loading spinner."""
    return rx.el.div(
        rx.el.div(
            rx.html(
                """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-loader-circle size-4 animate-spin" role="status" aria-label="Loading"><path d="M21 12a9 9 0 1 1-6.219-8.56"></path></svg>"""
            ),
            data_slot="empty-icon",
            data_variant="icon",
            class_name="mb-2 [&_svg]:pointer-events-none [&_svg]:shrink-0 bg-muted text-foreground flex size-10 shrink-0 items-center justify-center rounded-lg [&_svg:not([class*='size-'])]:size-6",
        ),
        rx.el.div(
            "Processing your request",
            data_slot="empty-title",
            class_name="text-lg font-medium tracking-tight",
        ),
        rx.el.div(
            "Please wait while we process your request. Do not refresh the page.",
            data_slot="empty-description",
            class_name="text-muted-foreground [&>a:hover]:text-primary text-sm/relaxed [&>a]:underline [&>a]:underline-offset-4",
        ),
        button("Cancel", variant="outline"),
        data_slot="empty-header",
        class_name="flex max-w-sm flex-col items-center gap-2 text-center border border-input rounded-lg p-4",
    )


def loading_badges():
    """Three loading badges with different variants."""
    return rx.el.div(
        rx.el.div(
            badge(
                rx.html(
                    """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-loader-circle size-4 animate-spin" role="status" aria-label="Loading"><path d="M21 12a9 9 0 1 1-6.219-8.56"></path></svg>"""
                ),
                "Syncing",
            ),
            badge(
                rx.html(
                    """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-loader-circle size-4 animate-spin" role="status" aria-label="Loading"><path d="M21 12a9 9 0 1 1-6.219-8.56"></path></svg>"""
                ),
                "Updating",
                variant="secondary",
            ),
            badge(
                rx.html(
                    """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-loader-circle size-4 animate-spin" role="status" aria-label="Loading"><path d="M21 12a9 9 0 1 1-6.219-8.56"></path></svg>"""
                ),
                "Loading",
                variant="outline",
            ),
            class_name="flex items-center gap-2 [--radius:1.2rem]",
        ),
        class_name="flex flex-row",
    )


def pagination_button_groups():
    """Pagination component with button groups for page numbers and navigation."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                button("1", variant="outline", size="sm"),
                button("2", variant="outline", size="sm"),
                button("3", variant="outline", size="sm"),
                role="group",
                data_slot="button-group",
                class_name="flex w-fit items-stretch [&>*]:focus-visible:z-10 [&>*]:focus-visible:relative [&>[data-slot=select-trigger]:not([class*='w-'])]:w-fit [&>input]:flex-1 has-[select[aria-hidden=true]:last-child]:[&>[data-slot=select-trigger]:last-of-type]:rounded-r-md has-[>[data-slot=button-group]]:gap-2 [&>*:not(:first-child)]:rounded-l-none [&>*:not(:first-child)]:border-l-0 [&>*:not(:last-child)]:rounded-r-none",
            ),
            role="group",
            data_slot="button-group",
            class_name="flex w-fit items-stretch [&>*]:focus-visible:z-10 [&>*]:focus-visible:relative [&>[data-slot=select-trigger]:not([class*='w-'])]:w-fit [&>input]:flex-1 has-[select[aria-hidden=true]:last-child]:[&>[data-slot=select-trigger]:last-of-type]:rounded-r-md has-[>[data-slot=button-group]]:gap-2 [&>*:not(:first-child)]:rounded-l-none [&>*:not(:first-child)]:border-l-0 [&>*:not(:last-child)]:rounded-r-none",
        ),
        rx.el.div(
            button(
                rx.html(
                    """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-left"><path d="m12 19-7-7 7-7"></path><path d="M19 12H5"></path></svg>"""
                ),
                aria_label="Previous",
                variant="outline",
                size="sm",
                class_name="size-8",
            ),
            button(
                rx.html(
                    """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-right"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>"""
                ),
                aria_label="Next",
                variant="outline",
                size="sm",
                class_name="size-8",
            ),
            role="group",
            data_slot="button-group",
            class_name="flex w-fit items-stretch [&>*]:focus-visible:z-10 [&>*]:focus-visible:relative [&>[data-slot=select-trigger]:not([class*='w-'])]:w-fit [&>input]:flex-1 has-[select[aria-hidden=true]:last-child]:[&>[data-slot=select-trigger]:last-of-type]:rounded-r-md has-[>[data-slot=button-group]]:gap-2 [&>*:not(:first-child)]:rounded-l-none [&>*:not(:first-child)]:border-l-0 [&>*:not(:last-child)]:rounded-r-none",
        ),
        rx.el.div(
            button(
                rx.html(
                    """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-bot"><path d="M12 8V4H8"></path><rect width="16" height="12" x="4" y="8" rx="2"></rect><path d="M2 14h2"></path><path d="M20 14h2"></path><path d="M15 13v2"></path><path d="M9 13v2"></path></svg>"""
                ),
                " Copilot",
                variant="outline",
                size="sm",
                # class_name="size-8"
            ),
            role="group",
            data_slot="button-group",
            class_name="flex w-fit items-stretch [&>*]:focus-visible:z-10 [&>*]:focus-visible:relative [&>[data-slot=select-trigger]:not([class*='w-'])]:w-fit [&>input]:flex-1 has-[select[aria-hidden=true]:last-child]:[&>[data-slot=select-trigger]:last-of-type]:rounded-r-md has-[>[data-slot=button-group]]:gap-2 [&>*:not(:first-child)]:rounded-l-none [&>*:not(:first-child)]:border-l-0 [&>*:not(:last-child)]:rounded-r-none",
        ),
        class_name="flex flex-row items-center justify-between gap-4",
    )


tooltip = {
    "is_animation_active": False,
    "separator": "",
    "cursor": False,
    "item_style": {
        "color": "currentColor",
        "display": "flex",
        "paddingBottom": "0px",
        "justifyContent": "space-between",
        "textTransform": "capitalize",
    },
    "label_style": {
        "color": rx.color("slate", 10),
        "fontWeight": "500",
    },
    "content_style": {
        "background": rx.color_mode_cond("oklch(0.97 0.00 0)", "oklch(0.14 0.00 286)"),
        "borderColor": rx.color("slate", 5),
        "borderRadius": "5px",
        "fontFamily": "IBM Plex Mono,ui-monospace,monospace",
        "fontSize": "0.875rem",
        "lineHeight": "1.25rem",
        "fontWeight": "500",
        "letterSpacing": "-0.01rem",
        "minWidth": "8rem",
        "width": "175px",
        "padding": "0.375rem 0.625rem ",
        "position": "relative",
    },
}


def info(title: str, size: str, subtitle: str, align: str):
    return rx.vstack(
        rx.heading(title, size=size, weight="bold"),
        rx.text(subtitle, size="1", color=rx.color("slate", 11), weight="medium"),
        spacing="1",
        align=align,
    )


def get_tooltip():
    """Standard tooltip for all charts."""
    return rx.recharts.graphing_tooltip(**tooltip)


def get_cartesian_grid():
    """Standard cartesian grid for charts."""
    return rx.recharts.cartesian_grid(
        horizontal=True, vertical=False, class_name="opacity-25"
    )


def get_x_axis(data_key: str):
    """Standard X axis configuration."""
    return rx.recharts.x_axis(
        data_key=data_key,
        axis_line=False,
        tick_size=10,
        tick_line=False,
        custom_attrs={"fontSize": "12px"},
        interval="preserveStartEnd",
    )


def barchart_v9():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80, "tablet": 50},
        {"month": "Feb", "desktop": 305, "mobile": 200, "tablet": 120},
        {"month": "Mar", "desktop": 237, "mobile": 120, "tablet": 70},
        # {"month": "Apr", "desktop": 73, "mobile": 190, "tablet": 30},
        # {"month": "May", "desktop": 209, "mobile": 130, "tablet": 80},
    ]

    return rx.box(
        rx.hstack(
            rx.foreach(
                [
                    ["Desktop", "var(--chart-1)"],
                    ["Mobile", "var(--chart-2)"],
                    ["Tablet", "var(--chart-3)"],
                ],
                lambda key: rx.hstack(
                    rx.box(class_name="w-3 h-3 rounded-sm", bg=key[1]),
                    rx.text(
                        key[0],
                        class_name="text-sm font-semibold",
                        color=rx.color("slate", 11),
                    ),
                    align="center",
                    spacing="2",
                ),
            ),
            class_name="py-4 px-4 flex w-full flex justify-center gap-8",
        ),
        rx.recharts.bar_chart(
            get_tooltip(),
            rx.recharts.bar(data_key="desktop", fill="var(--chart-1)", radius=4),
            rx.recharts.bar(data_key="mobile", fill="var(--chart-2)", radius=4),
            rx.recharts.bar(data_key="tablet", fill="var(--chart-3)", radius=4),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
        ),
        class_name="w-full flex flex-col gap-y-4 [&_.recharts-tooltip-item-separator]:w-full",
    )


def linechart_v8():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": "Jun", "desktop": 214, "mobile": 140},
    ]
    return rx.box(
        rx.recharts.line_chart(
            get_tooltip(),
            rx.recharts.line(
                data_key="desktop",
                stroke="var(--chart-1)",
                type_="linear",
                dot=False,
                stroke_width=2,
            ),
            rx.recharts.line(
                data_key="mobile",
                stroke="var(--chart-3)",
                type_="linear",
                dot=False,
                stroke_width=2,
            ),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
        ),
        rx.hstack(
            rx.foreach(
                [["Desktop", "var(--chart-1)"], ["Mobile", "var(--chart-3)"]],
                lambda key: rx.hstack(
                    rx.box(class_name="w-3 h-3 rounded-sm", bg=key[1]),
                    rx.text(
                        key[0],
                        class_name="text-sm font-semibold",
                        color=rx.color("slate", 11),
                    ),
                    align="center",
                    spacing="2",
                ),
            ),
            class_name="py-4 px-4 flex w-full flex justify-center gap-8",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )


def areachart_v5():
    import datetime
    import random

    start_date = datetime.date(2024, 4, 1)
    data = [
        {
            "date": (start_date + datetime.timedelta(days=i)).strftime("%b %d"),
            "desktop": random.randint(80, 500),
            "mobile": random.randint(100, 550),
        }
        for i in range(30)
    ]

    def gradient(id_: str, color: str):
        return rx.el.svg.linear_gradient(
            rx.el.svg.stop(stop_color=f"var(--{color})", offset="5%", stop_opacity=0.8),
            rx.el.svg.stop(
                stop_color=f"var(--{color})", offset="95%", stop_opacity=0.1
            ),
            x1=0,
            x2=0,
            y1=0,
            y2=1,
            id=id_,
        )

    def area(data_key: str, color: str):
        return rx.recharts.area(
            data_key=data_key,
            fill=f"url(#{data_key})",
            stack_id="a",
            stroke=f"var(--{color})",
            animation_easing="linear",
        )

    return rx.box(
        rx.recharts.area_chart(
            rx.el.svg.defs(
                gradient("desktop", "chart-1"),
                gradient("mobile", "chart-2"),
            ),
            get_tooltip(),
            get_cartesian_grid(),
            area("mobile", "chart-2"),
            area("desktop", "chart-1"),
            rx.recharts.x_axis(
                data_key="date",
                axis_line=False,
                min_tick_gap=32,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
                interval="preserveStartEnd",
            ),
            data=data,
            width="100%",
            height=280,
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )


def examples_page():
    # Define column groups for better organization
    column_one = [
        checkout_form(),
    ]

    column_two = [
        component(),
        loading_badges(),
        input_type_one(),
        barchart_v9(),
        input_type_two(),
        input_type_three(),
    ]

    column_three = [
        linechart_v8(),
        component_two(),
        loading_empty_state(),
    ]

    column_four = [
        input_group(),
        checkbox_form(),
        areachart_v5(),
        pagination_button_groups(),
    ]

    return rx.el.div(
        rx.el.div(
            # Column 1
            rx.el.div(
                *column_one,
                class_name="w-full flex flex-col gap-6",
            ),
            # Column 2
            rx.el.div(
                *column_two,
                class_name="w-full flex flex-col gap-6",
            ),
            # Column 3
            rx.el.div(
                *column_three,
                class_name="w-full flex flex-col gap-6",
            ),
            # Column 4
            rx.el.div(
                *column_four,
                class_name="w-full flex flex-col gap-6",
            ),
            class_name=" ".join(
                [
                    "mx-auto",
                    "grid gap-6",
                    "grid-cols-1",  # Mobile: 1 column
                    "sm:grid-cols-2",  # Small: 2 columns
                    "md:grid-cols-2",  # Medium: 2 columns (2x2 layout)
                    "lg:grid-cols-3",  # Large: 3 columns
                    "xl:grid-cols-4",  # XL: 4 columns
                    "sm:gap-6",  # Responsive gaps
                    "lg:gap-8",
                    "xl:gap-6",
                    "2xl:gap-8",
                    "py-1",
                ]
            ),
        ),
        class_name="w-full overflow-hidden p-4 sm:p-6 lg:p-8 "  # Responsive padding
        + rx.color_mode_cond(
            f"theme-{hooks.current_theme.value}",
            f"theme-{hooks.current_theme.value}-dark",
        ).to(str),
    )
