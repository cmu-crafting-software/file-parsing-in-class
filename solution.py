import itertools
import json
import statistics
from datetime import datetime
from pathlib import Path

presidents = json.loads(Path("presidents.json").read_text())
this_year = datetime.now().year
ages = [
    this_year - datetime.strptime(president["DOB"], "%Y-%m-%d").year
    for president in presidents
]
print(f"Average presidential age: {int(statistics.mean(ages))} years")
for president in sorted(presidents, key=lambda president: president["BirthState"]):
    print(f'{president["BirthState"]}:', president["First"], president["Last"])
