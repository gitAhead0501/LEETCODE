"""
929. Unique Email Addresses
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.

Constraints:
A) 1 <= emails.length <= 100
B) 1 <= emails[i].length <= 100
C) email[i] consist of lowercase English letters, '+', '.' and '@'.
D) Each emails[i] contains exactly one '@' character.
E) All local and domain names are non-empty.
F) Local names do not start with a '+' character.

Approach: split wrt @ evaluate left side and combine with right side
Evaluating left side of @ : if '+' is found in left side we neglect right side from that idx and replace . with '' : i.e. fill . with ''

"""

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for i in emails:
            a, b = i.split('@')
            if '+' in a:
                a = a[:a.index('+')]
            s.add(a.replace('.','') + '@' + b)
        return len(s)