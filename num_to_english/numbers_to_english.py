class NumberToWords:
    def __init__(self):
        self.TRILLION = 1e12
        self.BILLION = 1e9
        self.MILLION = 1e6
        self.THOUSAND = 1e3
        self.HUNDRED = 1e2
        self.one_digit = {
            1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
        }

        self.two_digit = {
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",

        }

        self.twenties = {
            2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy',
            8: 'Eighty', 9: 'Ninety'
        }

    def helper(self, num: str) -> str:

        ans = []
        if num >= self.TRILLION:
            ans += self.helper(num // self.TRILLION)
            ans.append("Trillion")
            ans += self.helper(num % self.TRILLION)
        elif num >= self.BILLION:
            ans += self.helper(num // self.BILLION)
            ans.append("Billion")
            ans += self.helper(num % self.BILLION)
        elif num >= self.MILLION:
            ans += self.helper(num // self.MILLION)
            ans.append("Million")
            ans += self.helper(num % self.MILLION)
        elif num >= self.THOUSAND:
            ans += self.helper(num // self.THOUSAND)
            ans.append("Thousand")
            ans += self.helper(num % self.THOUSAND)
        elif num >= self.HUNDRED:
            ans = []
            ans += self.helper(num // self.HUNDRED)
            ans.append("Hundred")
            ans += self.helper(num % self.HUNDRED)

        elif num >= 20:

            ans = [self.twenties[num // 10]]
            if num % 10 != 0:
                ans.append(self.one_digit[num % 10])

        elif num >= 10:
            ans.append(self.two_digit[num])
        elif num > 0:
            ans.append(self.one_digit[num])

        return ans

    def number_to_words(self, strnum: str) -> str:

        num = int(strnum)
        if num == 0:
            return "Zero"
        ans = self.helper(num)
        return ' '.join(ans)


# number = NumberToWords()
# print(number.number_to_words("875455"))
