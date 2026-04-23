feedback_message = " Hello Team, the service was Excellent! "

print("Original Message:", feedback_message)

cleaned_message = feedback_message.strip()

upper_message = cleaned_message.upper()
lower_message = cleaned_message.lower()

message_length = len(cleaned_message)

has_service = "service" in cleaned_message
no_bad = "bad" not in cleaned_message

first_char = cleaned_message[0]
last_char = cleaned_message[-1]

extracted_word = cleaned_message[17:24]

print(f"\nCleaned Message  : {cleaned_message}")
print(f"Uppercase        : {upper_message}")
print(f"Lowercase        : {lower_message}")
print(f"Length           : {message_length}")
print(f"Contains 'service': {has_service}")
print(f"'bad' not present: {no_bad}")
print(f"First Character  : {first_char}")
print(f"Last Character   : {last_char}")
print(f"Extracted Word   : {extracted_word}")
print(f"\nSummary: The cleaned feedback is '{cleaned_message}' with length {message_length}. Contains 'service': {has_service}.")