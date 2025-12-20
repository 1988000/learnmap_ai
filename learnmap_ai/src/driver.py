from nodes import Node
from walkers import Walker, CollectorWalker

# Create nodes
lesson1 = Node("Lesson 1")
lesson2 = Node("Lesson 2")
quiz1 = Node("Quiz 1")
taskA = Node("Task A")
taskB = Node("Task B")

# Connect nodes
lesson1.connect(lesson2)
lesson2.connect(quiz1)
quiz1.connect(taskA)
taskA.connect(taskB)

# Create walkers
walker = Walker("Explorer")
collector = CollectorWalker("Collector")

# Traverse
walker.traverse(lesson1)
collector.traverse(lesson1)

print("\n[Collector] Final collected nodes:", collector.collected)
