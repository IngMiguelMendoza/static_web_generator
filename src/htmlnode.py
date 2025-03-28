
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, value):
        return (
            self.tag == value.tag and 
            self.value == value.value and 
            self.children == value.children and 
            self.props == value.props
        )

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'
        
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"