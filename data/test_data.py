from faker import Faker

fake = Faker()


class TestData:
    name = fake.user_name()
    email = fake.email()
    password = fake.password()
    first_name = fake.first_name()
    last_name = fake.last_name()
    company = fake.company()
    address = fake.address()
    address2 = fake.address()
    state = fake.state()
    city = fake.city()
    zipcode = fake.zipcode()
    mobile_number = fake.phone_number()
    subject = fake.word()
    message = fake.sentence()
    card_name = fake.name()
    card_number = fake.credit_card_number(card_type=None)
    cvc_code = fake.credit_card_security_code(card_type=None)
    expiry_month = fake.credit_card_expire(date_format="%m")
    expiry_year = fake.random_int(min=2025, max=2030)

    valid_user_email = 'testaccount@example.com'
    valid_user_password = 'qwerty12'
    valid_user_name = 'Jack Sparrow'

