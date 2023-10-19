class Node:
    def __init__(self, id, name, type, parent=None):
        self.id = id
        self.name = name
        self.type = type
        self.parent = parent
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        self.children.remove(node)

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def set_name(self, name):
        self.name = name

    def set_type(self, type):
        self.type = type