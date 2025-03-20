import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test text node", TextType.BOLD)
        node2 = TextNode("This is a test text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node1 = TextNode("Dummy text", TextType.NORMAL)
        node2 = TextNode("Dummy text not equal to the one above", TextType.NORMAL)
        self.assertNotEqual(node1, node2)

    def test_text(self):
        node = TextNode("This is a test text node", TextType.BOLD, "")
        self.assertEqual(node.text, "This is a test text node")
        self.assertEqual(node.text_type, TextType.BOLD)
        self.assertEqual(node.url, "")

    def test_url(self):
        node = TextNode("This is a test text node", TextType.LINK, "https://example.com")
        self.assertEqual(node.url, "https://example.com")

        node = TextNode("This is a test text node", TextType.LINK)
        self.assertEqual(node.url, None)

    def test_repr(self):
        node = TextNode("This is a test node", TextType.NORMAL, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a test node, Normal, https://www.boot.dev)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()