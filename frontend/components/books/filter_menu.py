from nicegui import ui

from backend.src import http_exceptions
from backend.src.tags.endpoints import get_all_tags
from frontend.components.books import books_grid
from frontend.static import classes


class FilterMenuComponent:
    def __init__(self, all_books: list):
        self.all_books = all_books
        self.selected_tags = set()
        self.grid_container = None
        self.all_tags = []

    async def render(self):
        try:
            self.all_tags = await get_all_tags()
        except http_exceptions.NotFound404:
            self.all_tags = []

        with ui.row().classes(
            f"{classes.FILTER_MENU_CONTAINER} justify-center"
        ):
            # Grid column (ALWAYS exists)
            with ui.column().classes(
                classes.FILTER_MENU_GRID_CONTAINER + " mx-auto"
            ) as self.grid_container:
                pass

            # Tags column (ONLY if tags exist)
            if self.all_tags:
                with ui.column().classes(
                    classes.FILTER_MENU_TAGS_CONTAINER,
                ):
                    for tag in self.all_tags:
                        tag_name = tag.tag_name

                        def _on_tag_toggle(e, name=tag_name):
                            if e.value:
                                self.selected_tags.add(name)
                            else:
                                self.selected_tags.discard(name)
                            self._update_grid()

                        ui.checkbox(tag_name, on_change=_on_tag_toggle)

        self._update_grid()


    def _update_grid(self):
        if self.grid_container is None:
            return

        self.grid_container.clear()

        filtered_books = (
            [
                book
                for book in self.all_books
                if self.selected_tags.issubset(
                    {tag.tag_name for tag in book.book_tags},
                )
            ]
            if self.selected_tags
            else self.all_books
        )

        with self.grid_container:
            books_grid.BooksGridComponent(books=filtered_books).render()
