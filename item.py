from dataclasses import dataclass

@dataclass
class Item:
    id: int
    name: str
    category: str
    description: str
    priority: str
    

    def __str__(self):
        return (
            f"--- Item Info ---\n"
            f"ID: {self.id} -- Name: {self.name}\n"
            f"Category: {self.category}\n"
            f"Description: {self.description}\n"
            f"------------------"
        )