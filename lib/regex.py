import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"John Cena|Anya Taylor-Joy|D'Angelo"
name_regex = re.compile(name)
match = name_regex.fullmatch("John Cena")
# print(match)

phone_number = r"5555555555|555-555-5555|\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
phone_regex = re.compile(phone_number)
match = phone_regex.fullmatch("(555) 555-5555")
# print(match)

email_address = r"\D[A-z0-9_.+-]+@[A-z0-9-]+\.[a-zA-Z0-9-.]+"
email_regex = re.compile(email_address)
match = email_regex.fullmatch("johncena@wwe.com")
# print(match)
