from ..choices import UserStatus


def superuser_login_payload():
    return {"username": "+8801111111111", "password": "rakib123"}


def super_user_payload():
    return {
        "username": "+8801111111111",
        "phone": "+8801111111111",
        "email": "testsuper@mail.com",
        "password": "rakib123",
        "status": UserStatus.ABSENT,
    }


def absent_user_payload():
    return {
        "username": "+8801111111112",
        "phone": "+8801111111112",
        "email": "testabsent@mail.com",
        "password": "rakib123",
        "status": UserStatus.ABSENT,
    }


def present_user_payload():
    return {
        "username": "+8801111111113",
        "phone": "+8801111111113",
        "email": "testabsent@mail.com",
        "password": "rakib123",
        "status": UserStatus.PRESENT,
    }


def update_user_payload():
    return {"status": UserStatus.ABSENT}
