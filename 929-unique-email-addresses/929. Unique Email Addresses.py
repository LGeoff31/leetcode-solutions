class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def get_forwarded_email(email):
            local_address, domain = email.split("@")

            local_address = local_address.replace(".", "")
            if "+" in local_address:
                local_address = local_address[:local_address.index("+")]
            return local_address + "@" + domain

        unique_emails = set()

        for email in emails:
            print(email, get_forwarded_email(email))
            unique_emails.add(get_forwarded_email(email))
        return len(unique_emails)