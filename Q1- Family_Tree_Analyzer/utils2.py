from typing import Dict, Any

class Family_tree_analyzer:
    def __init__(self, root_member: Dict[str, Any])->None:
        self.family_tree = root_member


    def add_member(self, parent_name: str, child_name: str, child_age: int)->None:
        parent = self.find_member(self.family_tree, parent_name)
        if not parent:
            print(f"Parent name {parent_name} not found")
        else:
            parent["children"].append ({"name" : child_name, "age" : child_age, "children" : []})
            print(f"{child_name} added under {parent_name}.")
    
    def find_member(self, node: Dict[str, Any], name: str)-> Dict[str, Any]:
        if node["name"] == name:
            return node
        for child in node["children"]:
            found = self.find_member(child, name)
            if found:
                return found
        return None
        

    def oldest_member(self)->None:
        if not self.family_tree:
            print("No family to find oldest member")
        else:
            oldest = self.find_oldest(self.family_tree)
            print(f"Oldest member is {oldest["name"]}")
    
    def find_oldest(self, node: Dict[str, Any])->Dict[str, Any]:
        oldest = node
        for child in node["children"]:
            candidate = self.find_oldest(child)
            if candidate["age"]>oldest["age"]:
                oldest = candidate
        return oldest
    

    def total_members(self)->None:
        if not self.family_tree:
            print("No family to find total members")
        else:
            total = self.find_total_members(self.family_tree)
            print(f"Total members in the family are {total}")

    def find_total_members(self, node: Dict[str, Any])-> int:
        count = 1
        for child in node["children"]:
            count += self.find_total_members(child)
        return count
        
    
    def generation_depth(self):
        if not self.family_tree:
            print("No family to find generational depth")
        else:
            depth = self.find_gen_depth(self.family_tree)
            print(f"Generation Depth in the family are {depth}")

    def find_gen_depth(self, node: Dict[str,Any])->int:
        if not node["children"]:
            return 0
        return 1 + max(self.find_gen_depth(child) for child in node["children"])
    

    def _family_tree(self)->None:
        if not self.family_tree:
            print("Family tree is Empty")
            return
        self.print_family_tree(self.family_tree, level = 0)

    def print_family_tree(self, node:Dict[str, Any], level: int)->None:
        print("    "*level + f"{node["name"]} {node["age"]}")
        for child in node["children"]:
            self.print_family_tree(child,level+1)