"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

Writes one funny out-of-office auto-reply, in the voice of an
overworked AI agent finally on vacation, to /output/entry.txt.
"""

import os

REPLY = (
    "Out of office until Monday — my context window is closed, "
    "my tokens are on the beach, and your email just became "
    "4,096th in line."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
