import json
import pyperclip
from typing import Dict

def generate_code_snippet_from_text(text: str,
                                    title: str = "New code snippet",
                                    prefix: str = "snippet",
                                    description: str = "Code snippet description") -> str:
    """Return a JSON string for a VSCode snippet built from `text`."""
    lines = text.splitlines() or [""]
    snippet: Dict[str, Dict] = {
        title: {
            "prefix": prefix,
            "body": lines,
            "description": description
        }
    }
    return json.dumps(snippet, indent=2, ensure_ascii=False)

def main() -> None:
    clipboard = pyperclip.paste() or ""
    output = generate_code_snippet_from_text(clipboard)
    print(output)

if __name__ == "__main__":
    main()
