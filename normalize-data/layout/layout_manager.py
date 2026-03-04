class LayoutManager:
    @staticmethod
    def get_column_bboxes(page):
        width, height = page.width, page.height
        return [
            (0, 0, width / 2, height),
            (width / 2, 0, width, height)
        ]