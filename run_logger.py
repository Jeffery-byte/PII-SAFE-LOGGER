# from src.pii_safe_logger import PiiSafeLogger

# logger = PiiSafeLogger()

# # Set user consent
# logger.set_consent("user1", True)

# # Test logging
# logger.log("user1", "User email: test@example.com, phone: 123-456-7890, location: 37.7749,-122.4194")
# logger.log("user1", "Diagnostic info here", level="DIAG")


# from src.pii_safe_logger import PiiSafeLogger

# # Initialize logger
# logger = PiiSafeLogger(level="DIAG")

# # Set consent for users
# logger.set_consent("user1", True)
# logger.set_consent("user2", False)

# # Test logging
# logger.log("user1", "Contact John at john@example.com or 123-456-7890. Location: 37.7749,-122.4194")
# logger.log("user2", "This should NOT appear in logs because consent=False.")



from pii_safe_logger import PiiSafeLogger

logger = PiiSafeLogger(level="DIAG")

# Set consent for a user
logger.set_consent("user123", True)

# Logs with various PII
logger.log("user123", "Alice sent an email to alice@example.com")
logger.log("user123", "Call me at 123-456-7890")
logger.log("user123", "Meet at coordinates 37.7749,-122.4194")
logger.log("user123", "Bob just joined the platform")
