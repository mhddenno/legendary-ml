from dataclasses import dataclass, field
from rich.console import Console
from rich.table import Table

# Normal Class Example
class Person:
    age: int
    job: str
    name: str

    def __init__(self, *args) -> None:
        self.age = args[0]
        self.job = args[1]
        self.name = args[2]

    # For better representation
    #def __repr__(self) -> str:
    #    return f"Person(age={self.age}, job={self.job}, name={self.name})"


# Data Calss Example
@dataclass(order=True, frozen=True)
class PersonDataClass:
    sort_index: int = field(init=False, repr=False)
    age: int
    job: str
    name: str
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strength)

def main():
    p1 = Person(31, 'AI Engineer', 'Mo')
    p2 = Person(28, 'Network Engineer', 'Aghyad')
    p3 = Person(28, 'Network Engineer', 'Aghyad')
    
    p1_d = PersonDataClass(31, 'AI Engineer', 'Mo',90)
    p2_d = PersonDataClass(28, 'Network Engineer', 'Aghyad')
    p3_d = PersonDataClass(28, 'Network Engineer', 'Aghyad')

    table = Table(title="Class VS DataClass")

    table.add_column("Command", justify="right", style="cyan", no_wrap=True)
    table.add_column("Normal Class", style="magenta")
    table.add_column("Data Class", justify="right", style="green")

    table.add_row("print(id(instance_2))", str(id(p2)), str(id(p2_d)))
    table.add_row("print(id(instance_3))", str(id(p3)), str(id(p3_d)))
    table.add_row("print(instance_1)", str(p1), str(p1_d))
    table.add_row("print(instance_3 == instance_2)", str(p3 == p2), str(p3_d == p2_d))
    table.add_row("print(instance_1 > instance_2)", '----', str(p1_d > p2_d))

    console = Console()
    console.print(table)

if __name__ == "__main__":
    main()
