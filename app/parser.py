import re
from typing import List, Tuple

#Parses requirements.txt content and extracts (package, version)import re
def parse_requirements(content: str) -> List[Tuple[str, str]]:
    pattern = re.compile(r"^([\w\-]+)==([\d\.]+)$")
    lines = content.strip().splitlines()
    deps = []
    for line in lines:
        match = pattern.match(line.strip())
        if match:
            deps.append((match.group(1), match.group(2)))
    return deps