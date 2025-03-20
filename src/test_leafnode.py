import unittest
from leafnode import LeafNode, ParentNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "This is a test text node")
        node2 = LeafNode("p", "This is a test text node")
        self.assertEqual(node, node2)
    
    def test_neq(self):
        node1 = LeafNode("p", "Dummy text")
        node2 = LeafNode("p", "Dummy text not equal to the one above")
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = LeafNode("p", "This is a test node")
        self.assertEqual("LeafNode(p, This is a test node, None, None)", repr(node))
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("div", [LeafNode("p", "This is a test text node")])
        node2 = ParentNode("div", [LeafNode("p", "This is a test text node")])
        self.assertEqual(node, node2)
    
    def test_neq(self):
        node1 = ParentNode("div", [LeafNode("p", "Dummy text")])
        node2 = ParentNode("div", [LeafNode("p", "Dummy text not equal to the one above")])
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = ParentNode("div", [LeafNode("p", "This is a test node")])
        self.assertEqual("ParentNode(div, [LeafNode(p, This is a test node, None, None)], None)", repr(node))
        
    def test_parent_to_html(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")])
        self.assertEqual(node.to_html(), "<div><p>Hello, world!</p></div>")

    def test_parent_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("p", "Hello, world!")])
        with self.assertRaises(ValueError) as context:
            node.to_html()
        # self.assertRaises("Parent tag is required" in str(context.exception))

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_childrens(self):
        child_node1 = LeafNode("span1", "child1")
        child_node2 = LeafNode("span2", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        print(parent_node.to_html())
        self.assertEqual(parent_node.to_html(), "<div><span1>child1</span1><span2>child2</span2></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
 
       )

if __name__ == "__main__":
    unittest.main()