# https://dmoj.ca/problem/ecoo19r2p1


def remove_dot(email: str) -> str:
    position_at = email.find("@")
    return email[:position_at].replace(".", "") + email[position_at:]


def remove_after_plus(email: str) -> str:
    position_plus = email.find("+")

    if position_plus >= 0:
        position_at = email.find("@")
        email = email[:position_plus] + email[position_at:]

    return email


def count_unique_emails(emails: list[str]) -> int:
    unique_emails = set()

    for email in emails:
        email = email.lower()
        email = remove_dot(email)
        email = remove_after_plus(email)
        unique_emails.add(email)

    return len(unique_emails)


def get_emails() -> list[str]:
    n = int(input())
    emails = [input() for _ in range(n)]
    return emails


if __name__ == "__main__":
    for _ in range(10):
        emails = get_emails()
        print(count_unique_emails(emails))
