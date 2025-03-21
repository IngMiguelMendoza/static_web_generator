import unittest
from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter

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

class TestTextNodeToHtml(unittest.TestCase):
    def test_text_conversion(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_conversion(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic_conversion(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic text node")

    def test_code_conversion(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_link_conversion(self):
        node = TextNode("This is a link node", TextType.LINK, "https://examlpe.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://examlpe.com"})
        self.assertEqual(html_node.value, "This is a link node")

    def test_image_conversion(self):
        node = TextNode("Alternative image atribute", TextType.IMAGE, "https://examlpe.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://examlpe.com", "alt": "Alternative image atribute"})
        self.assertEqual(html_node.value, None)

class SplitTextDelimiters(unittest.TestCase):

    def test_negative_split_nodes_delimiter_at_end(self):
        old_nodes = [
            TextNode("**This is a bad bolded phase", TextType.NORMAL),
        ]

        new_nodes = []
        with self.assertRaises(ValueError) as context:
            new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 0)

    def test_negative_split_nodes_delimiter_at_end(self):
        old_nodes = [
            TextNode("This is **text** with a **bad bolded phrase at the end", TextType.NORMAL),
        ]

        new_nodes = []
        with self.assertRaises(ValueError) as context:
            new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 0)


    def test_positive_split_nodes_delimiter_at_end(self):
        old_nodes = [
            TextNode("This is text with a **bolded phrase at the end**", TextType.NORMAL),
        ]

        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.NORMAL)
        self.assertEqual(new_nodes[1].text, "bolded phrase at the end")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)


    def test_split_nodes_delimiter(self):
        old_nodes = [
            TextNode("This is text with a **bolded phrase** in the middle", TextType.NORMAL),
            TextNode("This is text with a _italic phrase_ in the middle", TextType.ITALIC),
            TextNode("This is text with a `code block` word", TextType.CODE)
        ]

        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.NORMAL)
        self.assertEqual(new_nodes[1].text, "bolded phrase")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " in the middle")
        self.assertEqual(new_nodes[2].text_type, TextType.NORMAL)
        self.assertEqual(new_nodes[3].text, "This is text with a _italic phrase_ in the middle")
        self.assertEqual(new_nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[4].text, "This is text with a `code block` word")
        self.assertEqual(new_nodes[4].text_type, TextType.CODE)

if __name__ == "__main__":
    unittest.main()