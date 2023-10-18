```python
import dearpygui.dearpygui as dpg
from UnityMLAgents.Editor.Node import Node
from UnityMLAgents.Editor.BehaviorTree import BehaviorTree

class BehaviorTreeEditor:
    def __init__(self):
        self.tree = BehaviorTree()
        self.node_editor_id = dpg.generate_uuid()

    def create_node(self, node_type):
        node = Node(node_type)
        self.tree.add_node(node)
        dpg.add_node(self.node_editor_id, node.id, node_type)
        return node.id

    def delete_node(self, node_id):
        self.tree.remove_node(node_id)
        dpg.delete_node(self.node_editor_id, node_id)

    def update_behavior_tree(self):
        dpg.clear_node_links(self.node_editor_id)
        for node in self.tree.nodes:
            for child in node.children:
                dpg.add_node_link(self.node_editor_id, node.id, child.id)

    def show(self):
        with dpg.node_editor(self.node_editor_id):
            for node in self.tree.nodes:
                dpg.add_node(node.id, node_type=node.type)
        dpg.show_documentation()

    def hide(self):
        dpg.hide_documentation()
```