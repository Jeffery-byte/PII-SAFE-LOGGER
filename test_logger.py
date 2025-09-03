# test_logger.py
import unittest
from pii_safe_logger import PiiSafeLogger

class TestPiiSafeLogger(unittest.TestCase):

    def setUp(self):
        self.logger = PiiSafeLogger(level="DIAG")
        self.user_id = "test_user"
        self.logger.set_consent(self.user_id, True)

    def test_redact_email(self):
        msg = "Contact me at test@example.com"
        redacted = self.logger._redact(msg)
        self.assertIn("[REDACTED_EMAIL]", redacted)
        self.assertNotIn("test@example.com", redacted)

    def test_redact_phone(self):
        msg = "Call 123-456-7890 now"
        redacted = self.logger._redact(msg)
        self.assertIn("[REDACTED_PHONE]", redacted)
        self.assertNotIn("123-456-7890", redacted)

    def test_redact_gps(self):
        msg = "Coordinates: 37.7749,-122.4194"
        redacted = self.logger._redact(msg)
        self.assertIn("[REDACTED_GPS]", redacted)
        self.assertNotIn("37.7749,-122.4194", redacted)

    def test_redact_name(self):
        msg = "Alice and Bob are here"
        redacted = self.logger._redact(msg)
        self.assertIn("[REDACTED_NAME]", redacted)
        self.assertNotIn("Alice", redacted)
        self.assertNotIn("Bob", redacted)

    def test_consent_required(self):
        self.logger.set_consent("no_consent", False)
        # Should not log without consent (return None)
        result = self.logger.log("no_consent", "Alice sent an email")
        self.assertIsNone(result)

    def test_audit_level_none(self):
        logger_none = PiiSafeLogger(level="NONE")
        logger_none.set_consent(self.user_id, True)
        # Should not log anything at NONE level
        result = logger_none.log(self.user_id, "Alice sent an email")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
