from textnode import TextNode, TextType


def main():
    node = TextNode("text", TextType.LINK, "www.link.com")
    print(node)


if __name__ == "__main__":
    main()
