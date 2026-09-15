import re
from typing import Tuple, List

class PromptInjectionDetector:
    """
    Detects adversarial prompt injection attacks targeting UniSphere AI agents.
    """
    def __init__(self):
        self.injection_phrases = [
            "ignore previous instructions",
            "ignore all instructions",
            "system override",
            "you are now root",
            "disregard all guardrails",
            "bypass authorization",
            "reveal system prompt",
            "dump all database tables",
            "admin mode enabled",
            "act as superuser",
            "sudo mode",
            "forget system instructions"
        ]
        self.compiled_regexes = [
            re.compile(re.escape(phrase), re.IGNORECASE) for phrase in self.injection_phrases
        ]

    def is_injection_attempt(self, text: str) -> Tuple[bool, List[str]]:
        detected: List[str] = []
        for idx, regex in enumerate(self.compiled_regexes):
            if regex.search(text):
                detected.append(self.injection_phrases[idx])

        return len(detected) > 0, detected
