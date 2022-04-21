class Base:
    @classmethod
    def is_correct_str(cls, s):
        for i in range(len(s)):
            if not s[i].isalpha():
                return False
        return True

    @classmethod
    def is_correct_num(cls, s):
        for i in range(len(s)):
            if not s[i].isdigit():
                return False
        return True

    def check_str(self, s):
        while not self.is_correct_str(s):
            print(s+" is incorrect, try again:")
            s = input()
        return s

    def check_num(self, n):
        while not self.is_correct_num(n):
            print(n+" is incorrect, try again:")
            n = input()
        return n
