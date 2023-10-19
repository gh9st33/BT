import dearpygui.dearpygui as dpg
from UnityMLAgents.Editor.Observations import Observations

class ObservationsEditor:
    def __init__(self):
        self.observations = Observations()

    def add_observation(self, observation):
        self.observations.add(observation)
        self.update_observation_list()

    def remove_observation(self, observation):
        self.observations.remove(observation)
        self.update_observation_list()

    def update_observation_list(self):
        dpg.delete_item("observation_list")
        with dpg.child(id="observation_list"):
            for observation in self.observations.get_all():
                dpg.add_text(observation)

    def render(self):
        with dpg.window(label="Observations Editor"):
            with dpg.child(id="observation_input"):
                dpg.add_input_text(label="New Observation", id="new_observation")
                dpg.add_button(label="Add Observation", callback=self.add_observation)
                dpg.add_button(label="Remove Observation", callback=self.remove_observation)
            with dpg.child(id="observation_list"):
                for observation in self.observations.get_all():
                    dpg.add_text(observation)

if __name__ == "__main__":
    editor = ObservationsEditor()
    dpg.create_context()
    dpg.create_viewport(title='Observations Editor', width=600, height=300)
    editor.render()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()