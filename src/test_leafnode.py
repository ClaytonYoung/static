import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html(self):
        node = LeafNode("", "hello world")
        self.assertEqual(node.to_html(), "hello world")

    def test_leaf_wrong_html_p(self):
        node = LeafNode("p", "no tag")
        self.assertNotEqual(node.to_html(), "no tag")

    #
    #
    #
    #
    # def test_eq(self):
    #     node = TextNode("This is a text node", TextType.BOLD)
    #     node2 = TextNode("This is a text node", TextType.BOLD)
    #     self.assertEqual(node, node2)
    #
    # def test_not_eq(self):
    #     node = TextNode("This is a text node", TextType.BOLD)
    #     node2 = TextNode("This is also a text node", TextType.BOLD)
    #     self.assertNotEqual(node, node2)
    #
    # def test_diff_class(self):
    #     node = TextNode("This is a text node", TextType.ITALIC)
    #     node2 = TextNode("This is a text node", TextType.BOLD)
    #     self.assertNotEqual(node, node2)
    #
    # def test_url_missing(self):
    #     node = TextNode("This is a link node", TextType.LINK)
    #     node2 = TextNode("This is a link node", TextType.LINK, None)
    #     self.assertEqual(node, node2)
    #
    #


if __name__ == "__main__":
    unittest.main()
