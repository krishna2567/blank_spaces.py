import re
import sys
from pathlib import Path

WHITESPACE_RE = re.compile(r'\s+')          # collapse any spaces/tabs/newlines

def clean_extra_spaces(input_path: Path, output_path: Path) -> None:
    with input_path.open('r', encoding='utf-8') as fin, \
         output_path.open('w', encoding='utf-8') as fout:
        for raw in fin:
            stripped = raw.strip()
            if not stripped:                # skip completely blank lines
                continue
            normalised = WHITESPACE_RE.sub(' ', stripped)
            fout.write(normalised + '\n')   # keep lines separate
    print(f"✅ Cleaned file saved to {output_path.resolve()}")

if _name_ == "_main_":
    if len(sys.argv) != 3:
        sys.exit("Usage: python clean_txt.py <input_file> <output_file>")
    clean_extra_spaces(Path(sys.argv[1]), Path(sys.argv[2]))