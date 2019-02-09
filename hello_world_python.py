import ast

class Analyzer:
    def __init__(self, userSol):
            self.sol = userSol

    def analyzeSolution(self):
        tree = ast.parse(self.sol)

        for node in ast.walk(tree):
            if isinstance(node, ast.Return) and node.value.s == "Hello, World!":
                return True

        return False
