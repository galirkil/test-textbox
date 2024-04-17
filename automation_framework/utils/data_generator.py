from faker import Faker


class DataGen:
    fake = Faker("ru_RU")

    @classmethod
    def full_name(cls):
        return cls.fake.name()

    @classmethod
    def email(cls):
        return cls.fake.email()

    @classmethod
    def address(cls):
        return cls.fake.address()
