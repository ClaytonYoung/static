from typing import override
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    """docstring for LeafNode."""

    def __init__(self, tag, value):
        super(LeafNode, self).__init__(tag=tag, value=value, children=[])

    @override
    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return f"{self.value}"
        return f"<{self.tag}>{self.value}</{self.tag}>"
