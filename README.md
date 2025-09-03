 # PII-Safe Logging Utility

## Overview
`PII-Safe Logger` is a Python module designed to demonstrate privacy-conscious logging for applications that handle user data. It detects and redacts likely personally identifiable information (PII) such as emails, phone numbers, GPS coordinates, and basic names. The logger also enforces consent-aware logging and supports multiple audit levels (`NONE`, `MINIMAL`, `DIAG`), defaulting to `MINIMAL`.

This tool helps developers ensure that logs do not unintentionally expose sensitive information and that users retain control over what is recorded.

---

## Setup

1. **Clone the repository**  
```bash
git clone <your-repo-link>
cd <repo-folder>


## Dependencies
python -m pip install -r requirements.txt


## Project Structure

repo/
├─ src/
│  └─ pii_safe_logger.py       # Logger implementation
├─ tests/
│  └─ test_logger.py           # Unit tests
└─ README.md


## Run/Usage

from src.pii_safe_logger import PiiSafeLogger

# Initialize logger
logger = PiiSafeLogger()

# Set user consent
logger.set_consent("user1", True)

# Log a message (audit level MINIMAL by default)
logger.log("user1", "User email: test@example.com and location: 37.7749, -122.4194")

# Change audit level
logger.log("user1", "This is a diagnostic message", level="DIAG")


# Run unit tests
python -m unittest discover -s tests


#Known Limitations

PII detection is basic: simple regex patterns for emails, phone numbers, GPS, and a small set of names. Complex names or uncommon patterns may not be detected.

Consent is tracked in-memory; restarting the app resets consent states.

Redacted logs are printed to the console; integration with production logging systems is not included.

Audit levels are simplistic and may need enhancement for fine-grained logging policies.


#Future Work

Expand PII detection: full name lists, addresses, structured data, and NLP-based detection.

Persist consent in a database or secure storage to survive restarts.

Add integration with centralized logging systems (e.g., ELK, Splunk) with PII-safe transformations.

Introduce role-based audit levels and policy-driven logging configurations.

Add performance benchmarking and optimize for high-throughput logging environments.