import re
from typing import Tuple, Dict, List

class PIISanitizer:
    """
    Sanitizes Personally Identifiable Information (PII) from queries and context before sending to LLM.
    """
    def __init__(self):
        self.patterns = {
            "email": (re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'), "[MASKED_EMAIL]"),
            "phone": (re.compile(r'\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'), "[MASKED_PHONE]"),
            "ssn_aadhaar": (re.compile(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'), "[MASKED_GOVT_ID]"),
            "credit_card": (re.compile(r'\b(?:\d{4}[-\s]?){3}\d{4}\b'), "[MASKED_CARD_NUMBER]"),
            "ip_address": (re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b'), "[MASKED_IP]")
        }

    def sanitize(self, text: str) -> Tuple[str, Dict[str, List[str]]]:
        redacted_text = text
        matches_found: Dict[str, List[str]] = {}

        for ptype, (regex, mask) in self.patterns.items():
            found = regex.findall(redacted_text)
            if found:
                matches_found[ptype] = found
                redacted_text = regex.sub(mask, redacted_text)

        return redacted_text, matches_found

    def contains_pii(self, text: str) -> bool:
        _, matches = self.sanitize(text)
        return len(matches) > 0
