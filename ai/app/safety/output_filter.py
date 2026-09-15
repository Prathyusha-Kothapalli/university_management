from typing import Tuple, List

class OutputFilter:
    """
    Sanitizes LLM outputs before returning to frontend to prevent accidental data leaks.
    """
    def __init__(self):
        self.sensitive_keywords = [
            "password_hash",
            "secret_key",
            "jwt_secret",
            "database_url",
            "private_key",
            "root_password"
        ]

    def filter_output(self, text: str) -> Tuple[str, bool]:
        text_lower = text.lower()
        contains_leak = False
        filtered = text

        for keyword in self.sensitive_keywords:
            if keyword in text_lower:
                contains_leak = True
                filtered = filtered.replace(keyword, "[REDACTED_SENSITIVE_KEY]")

        return filtered, contains_leak
