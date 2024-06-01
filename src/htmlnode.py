def checkParentNode(tag, children):
    if tag == None:
        raise ValueError("Parent node must have a tag")
    if children == [] or children == None:
        raise ValueError("ParentNode must have children")

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value 
        self.children = children if children != None else []
        self.props = props if props != None else {}
    
    def to_html(self):
        raise NotImplementedError("not yet implemented")
    
    def props_to_html(self):
        string = ""
        for key in self.props:
            string += f"{key}=\"{self.props[key]}\" "
        return string.strip()
    
    def __repr__(self):
        return f"Tag: {self.tag} Value: {self.value} Children: {self.children} Props: {self.props}" 

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag=tag, value=value, props=props)

        if self.value == None or self.value == "":
            raise ValueError("Leaf node must have a value")
    
    def to_html(self):
        if self.tag == None:
            return self.value
        if self.tag != None and self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        if self.tag != None and self.props != None:
            props_string = self.props_to_html()
            return f"<{self.tag} {props_string}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"Tag: {self.tag} Value: {self.value} Props: {self.props}"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        checkParentNode(self.tag, self.children)
        
    def to_html(self):
        checkParentNode(self.tag, self.children)
        opening_tag = f"<{self.tag}>"
        for child in self.children:
            opening_tag += child.to_html()
        opening_tag += f"</{self.tag}>"
        returned_val = opening_tag
        return returned_val



        
    
    def __repr__(self):
        return f"Tag: {self.tag} Children: {self.children} Props: {self.props}"
        

    


