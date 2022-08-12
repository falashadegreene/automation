import re


def clear_numbers(contact_string):
    contact_string = re.sub(r"\(", '', contact_string)
    contact_string = re.sub(r"\)", '-', contact_string)
    contact_string = re.sub(r"\.", '-', contact_string)

    if len(contact_string) == 8:
        contact_string = "206-" + contact_string

    if len(contact_string) == 9:
        contact_string = contact_string[:3] + '-' + contact_string[3:6] + '-' + contact_string[6:]

    return contact_string


def get_phone():
    clear = []
    num_pattern = re.compile(r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
    with open("assets/potential-contacts.txt") as numbers:
        lines = numbers.read()
        print(lines)

    match_contact = re.findall(num_pattern, lines)
    print(match_contact)

    for x in match_contact:
        clear.append(clear_numbers(x))

    print(clear)
    clear.sort()

    without_num_copies = list(dict.fromkeys(clear))

    with open("assets/phone_numbers.txt", "w+") as num_list:
        for num in without_num_copies:
            num_list.write(num)
            num_list.write('\n')


get_phone()


def get_email():
    mail_pattern = re.compile(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+")

    with open("assets/potential-contacts.txt") as mail:
        lines = mail.read()

    match_mail = re.findall(mail_pattern, lines)

    match_mail.sort()
    print(match_mail)

    mail_report = "\n".join(match_mail)

    with open("assets/emails.txt", "w+") as mail_string:
        mail_string.write(mail_report)


get_email()
