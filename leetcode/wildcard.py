class Solution:
    def isMatch(self, s: str, p: str)-> bool:
        sp =0
        pp = 0

        while pp < len(p):

            if s[sp != p[pp]]:
                return False
            else:
                sp += 1
                pp += 1
            if p[pp] == '?':
                sp += 1
                pp += 1
            if p[pp] == '*':
                # capture the char after the *
                next = p[pp + 1] if pp + 1 < len(p) else None
                # if next is none then * is at the end of the pattern
                if next is None:
                    break

                while s[sp] != next:
                    sp += 1
                # check if char at sp matches the char at pattern pointer:
                if s[sp] != p[pp]:
                    return False
                sp += 1
                pp += 1
        return True 