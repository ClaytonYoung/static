from typing import override
from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)

    @override
    def to_html(self):
        if not self.tag:
            raise ValueError
        if not self.children:
            raise ValueError("children are messed up")
        return f"<{self.tag}>{self.children.to_html()}</{self.tag}>"
