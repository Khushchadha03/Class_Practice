from utils import Family_tree_analyzer

Initial_Tree = {
    "name": "John",
    "age": 65,
    "children": [
        {"name": "Alice", "age": 40, "children": []}
    ]
}
analyzer = Family_tree_analyzer(Initial_Tree)
analyzer.add_member("Alice", "Mike" ,18)
analyzer.add_member("John", "Bob" ,18)
analyzer.oldest_member()
analyzer.total_members()
analyzer.generation_depth()
analyzer._family_tree()