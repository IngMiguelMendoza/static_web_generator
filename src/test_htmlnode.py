import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a test text node")
        node2 = HTMLNode("p", "This is a test text node")
        self.assertEqual(node, node2)

    def test_neq(self):
        node1 = HTMLNode("p", "Dummy text")
        node2 = HTMLNode("p", "Dummy text not equal to the one above")
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = HTMLNode("p", "This is a test node")
        self.assertEqual("HTMLNode(p, This is a test node, None, None)", repr(node))

if __name__ == "__main__":
    unittest.main()