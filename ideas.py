#!/usr/bin/env python3
from pathlib import Path
import os

# Folder for ideas
IDEAS_FOLDER = Path(os.environ["HOME"]) / ".local/share/ideas/"

def main():
    title = input("What is your idea? ")

    print("Interesting, tell me more...")
    description = list()
    line = "placeholder"
    while line != "":
        line = input("> ")
        description.append(line)
    
    path = IDEAS_FOLDER / f"{title}.md"
    with path.open("w") as idea_file:
        idea_file.write(f"# {title}\n")
        for line in description:
            idea_file.write(f"{line}\n")

    print(f"Sounds like a fun idea! I recorded it at {path}")

if __name__ == "__main__":
    main()
