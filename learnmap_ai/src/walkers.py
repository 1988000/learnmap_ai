class Walker:
    def __init__(self, name):
        self.name = name

    def traverse(self, node):
        print(f"[{self.name}] Visiting: {node.name}")
        for next_node in node.next_nodes:
            self.traverse(next_node)


class CollectorWalker(Walker):
    def __init__(self, name):
        super().__init__(name)
        self.collected = []

    def traverse(self, node):
        if node.name not in self.collected:
            self.collected.append(node.name)
        print(f"[{self.name}] Collected: {self.collected}")
        for next_node in node.next_nodes:
            self.traverse(next_node)
