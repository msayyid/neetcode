from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        my_set = set()
        for email in emails:
            e_address = ""
            i = 0
            while email[i] != "@":
                if email[i] == "+":
                    break
                if email[i] == ".":
                    i += 1
                    continue
                e_address += email[i]
                i += 1
            while email[i] != "@":
                i += 1
            
            while i < len(email):
                e_address += email[i]
                i += 1
            
            my_set.add(e_address)
        return len(my_set)
    

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        my_set = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            normalized = local + "@" + domain
            my_set.add(normalized)
        return len(my_set)