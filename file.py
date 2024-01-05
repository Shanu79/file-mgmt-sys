from copy import deepcopy
class File:
    def __init__(self, name) -> None:
        self.name=name
        self.content=""

    def serialize(self):
        serialized_data={
            'name': self.name,
            'content': self.content
        }

        return serialized_data
    
    def deserialize(self, file_data):
        self.content=file_data['content']
    
    def clone(self):
        return deepcopy(self)