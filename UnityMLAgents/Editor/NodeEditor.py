import dearpygui.dearpygui as dpg
from UnityMLAgents.Editor.Node import Node
from UnityMLAgents.Editor.BehaviorTree import BehaviorTree
from UnityMLAgents.Editor.Observations import Observations
from UnityMLAgents.Editor.Actions import Actions

class NodeEditor:

    def __init__(self):
        self.node_id_counter = 0
        self.nodes = {}
        self.behavior_tree = BehaviorTree()
        self.observations = Observations()
        self.actions = Actions()

    def create_node(self):
        node_id = self.node_id_counter
        self.node_id_counter += 1
        node = Node(node_id)
        self.nodes[node_id] = node
        dpg.add_text(f"Node {node_id} created")
        return node_id

    def delete_node(self, node_id):
        if node_id in self.nodes:
            del self.nodes[node_id]
            dpg.add_text(f"Node {node_id} deleted")
        else:
            dpg.add_text(f"Node {node_id} does not exist")

    def update_behavior_tree(self, node_id, behavior):
        if node_id in self.nodes:
            self.nodes[node_id].behavior = behavior
            self.behavior_tree.update(node_id, behavior)
            dpg.add_text(f"Node {node_id} behavior updated to {behavior}")
        else:
            dpg.add_text(f"Node {node_id} does not exist")

    def add_observation(self, node_id, observation):
        if node_id in self.nodes:
            self.nodes[node_id].observations.append(observation)
            self.observations.add(observation)
            dpg.add_text(f"Observation {observation} added to Node {node_id}")
        else:
            dpg.add_text(f"Node {node_id} does not exist")

    def take_action(self, node_id, action):
        if node_id in self.nodes:
            self.nodes[node_id].actions.append(action)
            self.actions.add(action)
            dpg.add_text(f"Action {action} added to Node {node_id}")
        else:
            dpg.add_text(f"Node {node_id} does not exist")