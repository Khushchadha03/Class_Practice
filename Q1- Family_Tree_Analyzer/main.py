from utils import Family_Tree_Analyzer, Person

root = Person("John", 78)


analyzer = Family_Tree_Analyzer(root)

analyzer.add_member("John", "Alice" ,18)
analyzer.add_member("Alice", "Mike" ,18)
analyzer.add_member("John", "Bob" ,18)
analyzer.Oldest_member()
analyzer.total_members()
analyzer.generation_depth()
analyzer.print_family_tree()