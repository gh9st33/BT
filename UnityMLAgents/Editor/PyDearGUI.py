import dearpygui.dearpygui as dpg

class PyDearGUI:
    def __init__(self):
        self.node_editor = None
        self.behavior_tree_editor = None
        self.observations_editor = None
        self.actions_editor = None

    def create_window(self, title):
        return dpg.add_window(label=title)

    def create_node_editor(self, parent):
        self.node_editor = dpg.add_node_editor(parent=parent)
        return self.node_editor

    def create_behavior_tree_editor(self, parent):
        self.behavior_tree_editor = dpg.add_node_editor(parent=parent)
        return self.behavior_tree_editor

    def create_observations_editor(self, parent):
        self.observations_editor = dpg.add_node_editor(parent=parent)
        return self.observations_editor

    def create_actions_editor(self, parent):
        self.actions_editor = dpg.add_node_editor(parent=parent)
        return self.actions_editor

    def run(self):
        dpg.create_context()
        dpg.create_viewport(title='Unity ML Agents Node Editor', width=600, height=600)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()