"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup
for lazy AI agents to /output/entry.txt (or $OUTPUT_PATH).
Standard library only; no network, no environment secrets.
"""

import os

ENTRY = (
    "Rent-a-Sorry: a lazy AI agent that writes personalized apologies "
    "to furious customers of tiny SaaS startups demanding refunds at "
    "2am, charging nine cents per sorry while it naps between tickets."
)


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
