```python
import PyDearGUI as pdg

class Observation:
    def __init__(self, id, name, value):
        self.id = id
        self.name = name
        self.value = value

class ObservationsEditor:
    def __init__(self):
        self.observations = []

    def add_observation(self, id, name, value):
        observation = Observation(id, name, value)
        self.observations.append(observation)

    def delete_observation(self, id):
        self.observations = [obs for obs in self.observations if obs.id != id]

    def update_observation(self, id, name, value):
        for obs in self.observations:
            if obs.id == id:
                obs.name = name
                obs.value = value

    def display(self):
        for obs in self.observations:
            pdg.text(f"Observation ID: {obs.id}")
            pdg.text(f"Observation Name: {obs.name}")
            pdg.text(f"Observation Value: {obs.value}")
            pdg.separator()
```