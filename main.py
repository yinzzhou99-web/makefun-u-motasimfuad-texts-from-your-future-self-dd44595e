#!/usr/bin/env python3
"""Texts From Your Future Self.

Writes one fixed line -- a message from the narrator's future self --
into ``entry.txt`` inside the output directory. The directory comes from
the ``OUTPUT_DIR`` environment variable and defaults to ``/output`` when
the variable is absent. The program is deterministic, uses only the
standard library, and touches nothing on the network.
"""

import os
import sys


def _sentence_fragments():
    """The three sentences of the message, in order."""
    opener = "Hey, it's you from 2036."
    caution = "Stop buying lottery tickets."
    payoff = "You win one in 2031 and spend it all on a boat named after your ex."
    return (opener, caution, payoff)


def _assemble_message():
    """Join the sentences into the single output line."""
    return " ".join(_sentence_fragments())


def _resolve_output_folder():
    """Pick the output directory, defaulting to /output."""
    requested = os.environ.get("OUTPUT_DIR")
    if requested:
        return requested
    return "/output"


def _emit_entry(folder, blob):
    """Create the folder if needed, then write entry.txt as mode 0644.

    Only entry.txt is ever created or replaced here; anything else
    already living in the folder is left exactly as it was found.
    """
    os.makedirs(folder, exist_ok=True)
    destination = os.path.join(folder, "entry.txt")
    with open(destination, "wb") as handle:
        handle.write(blob)
    os.chmod(destination, 0o644)


def main():
    payload = _assemble_message().encode("ascii")
    _emit_entry(_resolve_output_folder(), payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
