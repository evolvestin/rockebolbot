import re
from typing import Any

ESCAPE_SEQUENCES = {'{': '&#123;', '<': '&#60;', '}': '&#125;', "'": '&#39;'}


def bold(text: Any) -> str:
    """Wraps the given text in bold HTML tags."""
    return f'<b>{text}</b>'


def italic(text: Any) -> str:
    """Wraps the given text in italic HTML tags."""
    return f'<i>{text}</i>'


def strike(text: Any) -> str:
    """Wraps the given text in strikethrough HTML tags."""
    return f'<s>{text}</s>'


def under(text: Any) -> str:
    """Wraps the given text in underline HTML tags."""
    return f'<u>{text}</u>'


def code(text: Any) -> str:
    """Wraps the given text in code HTML tags."""
    return f'<code>{text}</code>'


def html_link(link: str, text: str) -> str:
    """Creates an HTML hyperlink with the specified URL and link text."""
    return f'<a href="{link}">{text}</a>'


def sub_tag(text: str) -> str:
    """Removes all HTML tags from the given text."""
    return re.sub('<.*?>', '', str(text))


def blockquote(text: Any, expandable: bool = False) -> str:
    """Wraps the given text in blockquote HTML tags."""
    return f'{"<blockquote expandable>" if expandable else "<blockquote>"}{text}</blockquote>'


def html_secure(text: Any, reverse: bool = False) -> str:
    """Escapes or unescapes HTML special characters in the given text."""
    for pattern, value in ESCAPE_SEQUENCES.items():
        text = re.sub(pattern, value, str(text)) if not reverse else re.sub(value, pattern, str(text))
    return text
