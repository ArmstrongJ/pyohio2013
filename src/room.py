import json


def get_room(id):
    ret = None
    with open(str(id)+".json", "r") as f:
        jsontext = f.read()
        d = json.loads(jsontext)
        d['id'] = id
        ret = Room(**d)
    return ret

class Room():
    def __init__(self, id=0, name="A Room", description="An empty room", neighbors={}):
        self.id = id
        self.name = name
        self.description = description
        self.neighbors = neighbors
        
    def _neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None
        
    def north(self):
        return self._neighbor('n')
    
    def south(self):
        return self._neighbor('s')
        
    def east(self):
        return self._neighbor('e')
        
    def west(self):
        return self._neighbor('w')
