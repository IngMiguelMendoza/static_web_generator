from textnode import (TextNode, TextType)


def main():
    node = TextNode("This is some anchor text", TextType.NORMAL, "https://www.boot.dev")
    print(node)

main()