```python
class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)


class BehaviorTree:
    def __init__(self):
        self.root = None

    def set_root(self, node):
        self.root = node

    def get_node(self, id, node=None):
        if node is None:
            node = self.root
        if node.id == id:
            return node
        for child in node.children:
            found_node = self.get_node(id, child)
            if found_node is not None:
                return found_node
        return None

    def add_node(self, id, name, parent_id=None):
        new_node = Node(id, name)
        if parent_id is None:
            self.set_root(new_node)
        else:
            parent_node = self.get_node(parent_id)
            if parent_node is not None:
                parent_node.add_child(new_node)
```