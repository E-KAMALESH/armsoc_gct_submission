contacts_dict = {
    "रवि": "6364679034",
    "राम": "9876543210"
}

def get_contact_number(text):
    for name in contacts_dict:
        if name in text:
            return contacts_dict[name]
    return None
