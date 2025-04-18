# write tests
import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    """docstring for TestHTMLNode."""

    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="a", value="hiiya", props=None)
        result = node.props_to_html()
        self.assertEqual(result, "", "None prop is ''")

    def test_props_to_html_empty_props(self):
        node = HTMLNode(tag="a", value="frig", props={})
        result = node.props_to_html()
        self.assertEqual(result, "", "Empty prop is ''")

    def test_props_to_single_props(self):
        node = HTMLNode(
            tag="a", value="the value", props={"href": "https://example.com"}
        )
        result = node.props_to_html()
        self.assertEqual(
            result, ' href="https://example.com"', "single prop is functioning"
        )


if __name__ == "__main__":
    unittest.main()
