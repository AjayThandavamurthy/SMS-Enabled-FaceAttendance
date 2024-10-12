import csv
import phonenumbers
from twilio.rest import Client

# Your Twilio account SID and authentication token
account_sid = 'ACda67273788f52679e0c81f0a130e1391'
auth_token = 'fade05a4a5c0934e209f1ceaa72ea02b'

# Your Twilio phone number
twilio_phone_number = '+12059418754'

client = Client(account_sid, auth_token)

# Read the CSV file with absentees' phone numbers
with open(r"C:\Users\Ajay\OneDrive\Desktop\face-recognition-based-attendance-system-master\users.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        phone_number = row.get('Phone')
        
        if phone_number:
            try:
                # Parse and format the phone number
                parsed_number = phonenumbers.parse(phone_number, "IN")
                formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

                # Customize your SMS message
                message = f"Dear student, you were marked absent today. Please contact us if there's an issue. - Your School Name"

                # Send SMS using Twilio
                message = client.messages.create(
                    body=message,
                    from_=twilio_phone_number,
                    to=formatted_number
                )

                print(f"SMS sent to {formatted_number} with SID: {message.sid}")
            except phonenumbers.NumberParseException as e:
                print(f"Invalid phone number: {phone_number}. Error: {e}")
        else:
            print("Phone number not found in the row.")
