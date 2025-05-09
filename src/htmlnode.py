class HTMLNode:
    """docstring for HTMLNode."""

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        thestring = ""
        if self.props:
            for key, value in self.props.items():
                thestring += f' {key}="{value}"'
            return thestring
        return ""

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
