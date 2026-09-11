import re

# Email regex pattern
EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'

# Function to find emails from text
def find_emails(text):
    return re.findall(EMAIL_PATTERN, text)

# Function to check whether an email is valid
def is_valid_email(email):
    return re.fullmatch(EMAIL_PATTERN, email) is not None


# Sample text
sample_text = """
Contact us at support@gmail.com.
You can also email harsh_23@yahoo.com
or student123@college.edu.in.
"""

# Find all emails
emails = find_emails(sample_text)

print("Emails Found:")
for email in emails:
    print(email)

print("Total Emails:", len(emails))


# Test email validation
test_emails = [
    "harsh@gmail.com",
    "student_23@yahoo.com",
    "@missing-local.com",
    "wrongemail.com",
    "abc@college.edu.in"
]

print("\nEmail Validation:")

for email in test_emails:
    if is_valid_email(email):
        print(email, "- VALID")
    else:
        print(email, "- INVALID")