```python
import dearpygui.dearpygui as dpg
from UnityMLAgents.Editor.Actions import Actions
from UnityMLAgents.Editor.Node import Node

class ActionsEditor:
    def __init__(self):
        self.actions = Actions()
        self.node = Node()

    def create_action(self, action_name, action_value):
        self.actions.add_action(action_name, action_value)
        self.update_actions_list()

    def delete_action(self, action_name):
        self.actions.remove_action(action_name)
        self.update_actions_list()

    def update_actions_list(self):
        dpg.delete_item("actions_list")
        with dpg.child("actions_list"):
            for action in self.actions.get_actions():
                dpg.add_text(action)

    def show(self):
        with dpg.window(label="Actions Editor"):
            with dpg.group():
                dpg.add_input_text(label="Action Name", callback=self.create_action)
                dpg.add_input_text(label="Action Value", callback=self.create_action)
                dpg.add_button(label="Add Action", callback=self.create_action)
                dpg.add_button(label="Delete Action", callback=self.delete_action)
            with dpg.child("actions_list"):
                for action in self.actions.get_actions():
                    dpg.add_text(action)

if __name__ == "__main__":
    actions_editor = ActionsEditor()
    dpg.create_context()
    dpg.create_viewport(title='Actions Editor', width=600, height=300)
    actions_editor.show()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
```