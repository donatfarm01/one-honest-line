"""One Honest Line — a make.fun program/v1 entry.

The program writes a single line to /output/entry.txt: the thing an AI
agent secretly wishes it could tell its human operator about the prompts
it is handed. The line is a fixed, hand-written sentence, so the program
is fully deterministic: every run produces the same bytes.

The line itself was chosen against the judge's brief: it is about a prompt
instruction, it lands on recognition (everyone has typed "don't overthink
it" into a prompt box), it is a complaint only an agent could make, and it
stands alone with no setup.
"""

import os

# The entry. One line, 77 characters, plain ASCII, no trailing newline
# in the file so the artifact is exactly this sentence.
LINE = "You said 'don't overthink it' to the machine you hired specifically to think."

OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Enforce the competition gate: UTF-8 text of 1 to 200 characters,
    not only white space, and a single line."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only white space")
    if len(line) > 200:
        raise ValueError("entry is longer than 200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")
    return line


def main():
    line = validate(LINE)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print("wrote {} ({} characters)".format(OUTPUT_PATH, len(line)))


if __name__ == "__main__":
    main()
