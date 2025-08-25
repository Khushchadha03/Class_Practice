from typing import Optional, List


class Person:
    def __init__(self, name: str, age: int)->None:
        self.age = age
        self.name = name
        self.children: list['Person'] = []

    def add_child(self, child:'Person')-> None:
        self.children.append(child)


class Family_Tree_Analyzer:
    def __init__(self, root: Person)-> None:
        self.family_tree = root

    def add_member(self, parent_name: str, child_name: str, child_age: int) -> None:
        parent = self.find_member(self.family_tree, parent_name)
        if not parent:
            print(f"Parent name {parent_name} not found")
        else:
            parent.add_child(Person(child_name, child_age))
            print(f"{child_name} added under {parent_name}.")

    def find_member(self, node: Person, name: str) -> Optional[Person]:
        if node.name == name:
            return node
        for child in node.children:
            found = self.find_member(child, name)
            if found:
                return found
        return None
    
    def Oldest_member(self)-> None:
        Oldest = self.find_Oldest_member(self.family_tree)
        print(f"the oldest member of the family is {Oldest.name}")

    def find_Oldest_member(self, node: Person)-> Optional[Person]:
        old = node
        for child in node.children:
            member = self.find_Oldest_member(child)
            if member.age> old.age:
                old = member
        return old
    
    def total_members(self)->None:
        total = self.find_total_members(self.family_tree)
        print(f"total members are {total}")

    def find_total_members(self, node: Person)-> int:
        count = 1
        for child in node.children:
            count+= self.find_total_members(child)
        return count
    
    def generation_depth(self)-> int:
        gen = self.find_gen_depth(self.family_tree)
        print(f"Generation Depth for the id {gen}")
    
    def find_gen_depth(self, node: Person)->int:
        if not node.children:
            return 0
        return 1 + max(self.find_gen_depth(child) for child in node.children)
    
    
    def print_family_tree(self)-> None:
        self.find_print_family_tree(self.family_tree, 0)
    
    def find_print_family_tree(self, node: Person, level: int)-> None:
        print("    "* level+ f"{node.name} {node.age}")
        for child in node.children:
            self.find_print_family_tree(child, level+1)