"""Warmup 9A - Widgets
Prof. O
2024-10-31
"""

class Widget:
    pass

class Button(Widget):
    pass

class Label(Widget):
    pass

class Panel(Widget):
    def __init__(self, items: list[Widget]):
        self.items = items
