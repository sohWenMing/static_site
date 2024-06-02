def checkParentNode(tag, children):
    if tag == None:
        raise ValueError("Parent node must have a tag")
    if children == [] or children == None:
        raise ValueError("ParentNode must have children")