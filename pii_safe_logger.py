# import re
# import logging


# class PiiSafeLogger:

#     AUDIT_LEVELS = {"NONE": 0, "MINIMAL": 1, "DIAG": 2}

#     def __init__(self, level="MINIMAL"):
#         self.logger = logging.getLogger("PiiSafeLogger")
#         self.logger.setLevel(logging.DEBUG)
#         handler = logging.StreamHandler()
#         formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
#         handler.setFormatter(formatter)
#         self.logger.addHandler(handler)
#         self.audit_level = self.AUDIT_LEVELS.get(level.upper(), 1)
#         self.user_consents = {}

#     def set_consent(self, user_id, consent=True):
#         """Store user consent decision."""
#         self.user_consents[user_id] = consent

#     def require_consent(self, user_id):
#         """Checks if user consent exists and is True."""
#         return self.user_consents.get(user_id, False)

#     def _redact(self, message: str) -> str:
#         """Redact common PII patterns from a log message."""
#         # Emails
#         message = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "[REDACTED_EMAIL]", message)

#         # Phone numbers (simple patterns)
#         message = re.sub(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b", "[REDACTED_PHONE]", message)

#         # GPS coordinates (decimal degrees)
#         message = re.sub(r"\b-?\d{1,3}\.\d+,\s*-?\d{1,3}\.\d+\b", "[REDACTED_GPS]", message)

#         # Names (toy example: capitalized first names only)
#         message = re.sub(r"\b([A-Z][a-z]+)\b", "[REDACTED_NAME]", message)

#         return message

#     def log(self, user_id, message: str, level="MINIMAL"):
#         """Log a message if consent exists, applying audit levels and redaction."""
#         if not self.require_consent(user_id):
#             return  

#         msg = self._redact(message)
#         audit_value = self.AUDIT_LEVELS.get(level.upper(), 1)

#         if self.audit_level == 0 or audit_value > self.audit_level:
#             return  

#         if self.audit_level == 1:
#             self.logger.info(msg)
#         elif self.audit_level == 2:
#             self.logger.debug(f"[DIAG] {msg}")



import re
import logging

class PiiSafeLogger:

    AUDIT_LEVELS = {"NONE": 0, "MINIMAL": 1, "DIAG": 2}

    def __init__(self, level="MINIMAL"):
        self.logger = logging.getLogger("PiiSafeLogger")
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(handler)
        self.audit_level = self.AUDIT_LEVELS.get(level.upper(), 1)
        self.user_consents = {}

    def set_consent(self, user_id, consent=True):
        """Store user consent decision."""
        self.user_consents[user_id] = consent

    def require_consent(self, user_id):
        """Checks if user consent exists and is True."""
        return self.user_consents.get(user_id, False)

    def _redact(self, message: str) -> str:
        """Redact common PII patterns from a log message."""
        # Emails
        message = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "[REDACTED_EMAIL]", message)

        # Phone numbers (simple patterns)
        message = re.sub(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b", "[REDACTED_PHONE]", message)

        # GPS coordinates (decimal degrees)
        message = re.sub(r"\b-?\d{1,3}\.\d+,\s*-?\d{1,3}\.\d+\b", "[REDACTED_GPS]", message)

        # Names (toy example: capitalized first names only)
        message = re.sub(r"\b([A-Z][a-z]+)\b", "[REDACTED_NAME]", message)

        return message

    def log(self, user_id, message: str, level="MINIMAL"):
        """Log a message if consent exists, applying audit levels and redaction."""
        if not self.require_consent(user_id):
            return  

        msg = self._redact(message)
        audit_value = self.AUDIT_LEVELS.get(level.upper(), 1)

        if self.audit_level == 0 or audit_value > self.audit_level:
            return  

        if self.audit_level == 1:
            self.logger.info(msg)
        elif self.audit_level == 2:
            self.logger.debug(f"[DIAG] {msg}")
