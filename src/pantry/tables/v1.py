import reflex as rx

data = [
    {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False},
    {
        "userId": 1,
        "id": 2,
        "title": "quis ut nam facilis et officia qui",
        "completed": False,
    },
    {"userId": 1, "id": 3, "title": "fugiat veniam minus", "completed": False},
    {"userId": 1, "id": 4, "title": "et porro tempora", "completed": True},
    {
        "userId": 1,
        "id": 5,
        "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
        "completed": False,
    },
    {
        "userId": 1,
        "id": 6,
        "title": "qui ullam ratione quibusdam voluptatem quia omnis",
        "completed": False,
    },
    {
        "userId": 1,
        "id": 7,
        "title": "illo expedita consequatur quia in",
        "completed": False,
    },
    {"userId": 1, "id": 8, "title": "quo adipisci enim quam ut ab", "completed": True},
    {"userId": 1, "id": 9, "title": "molestiae perspiciatis ipsa", "completed": False},
    {
        "userId": 1,
        "id": 10,
        "title": "illo est ratione doloremque quia maiores aut",
        "completed": True,
    },
]


class Table(rx.State):
    main_data: list[dict[str, str]] = data
    paginated_data: list[dict[str, str]] = data[:10]

    column_names: list[str] = list(main_data[0].keys())
    limits: list[str] = ["10", "15", "20", "30", "50"]

    current_limit: int = 10
    offset: int = 0
    current_page: int = 1
    number_of_rows: int = len(main_data)
    total_pages: int = (number_of_rows + current_limit - 1) // current_limit

    def paginate(self) -> None:
        start = self.offset
        end = start + self.current_limit
        self.paginated_data = self.main_data[start:end]
        self.current_page = (self.offset // self.current_limit) + 1

    def delta_limit(self, limit: str) -> None:
        self.current_limit = int(limit)
        self.offset = 0
        self.total_pages = (
            self.number_of_rows + self.current_limit - 1
        ) // self.current_limit
        self.paginate()

    def previous(self) -> None:
        if self.offset >= self.current_limit:
            self.offset -= self.current_limit
        else:
            self.offset = 0

        self.paginate()

    def next(self) -> None:
        if self.offset + self.current_limit < self.number_of_rows:
            self.offset += self.current_limit

        self.paginate()


def create_table_header(title: str):
    return rx.table.column_header_cell(title)


def create_query_rows(data: dict[str, str]):
    def fill_rows_with_data(data_):
        return rx.table.cell(f"{data_[1]}", cursor="pointer")

    return rx.table.row(
        rx.foreach(data, fill_rows_with_data),
        _hover={"bg": rx.color(color="gray", shade=4)},
        align="center",
        white_space="nowrap",
    )


def create_pagination():
    return rx.hstack(
        rx.hstack(
            rx.text("Rows per page", weight="bold", font_size="12px"),
            rx.select(
                Table.limits,
                default_value="10",
                on_change=Table.delta_limit,
                width="80px",
            ),
            align_items="center",
        ),
        rx.hstack(
            rx.text(
                f"Page {Table.current_page} of {Table.total_pages}",
                width="100px",
                weight="bold",
                font_size="12px",
            ),
            rx.button(
                rx.icon(
                    tag="chevron-left",
                    on_click=Table.previous,
                    size=25,
                    cursor="pointer",
                ),
                color_scheme="gray",
                variant="surface",
                size="1",
                width="32px",
                height="32px",
            ),
            rx.button(
                rx.icon(
                    tag="chevron-right",
                    on_click=Table.next,
                    size=25,
                    cursor="pointer",
                ),
                color_scheme="gray",
                variant="surface",
                size="1",
                width="32px",
                height="32px",
            ),
            align_items="center",
            spacing="1",
        ),
        align_items="center",
        spacing="4",
        flex_wrap="wrap",
    )


def tables_v1():
    return rx.vstack(
        create_pagination(),
        rx.table.root(
            rx.table.header(
                rx.table.row(rx.foreach(Table.column_names, create_table_header)),
            ),
            rx.table.body(rx.foreach(Table.paginated_data, create_query_rows)),
            width="100%",
            variant="surface",
            max_width="800px",
            size="1",
        ),
        width="100%",
        align="center",
    )
