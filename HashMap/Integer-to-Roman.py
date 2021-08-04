class Solution(object):
    def intToRoman(self, num):
        dict = {"M": 0, "CM": 0, "D": 0, "CD": 0, "C": 0, "XC": 0, "L": 0, "XL": 0, "X": 0, "IX": 0, "V": 0, "IV": 0,  "I": 0}
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for i in range(len(roman)):
            dict[roman[i]] = num // number[i]
            num = num % number[i]
        return dict["M"] * "M" + dict["CM"] * "CM" + dict["D"] * "D" + dict["CD"] * "CD" + dict["C"] * "C" + dict["XC"] * "XC" + dict["L"] * "L" + dict["XL"] * "XL" + dict["X"] * "X" + dict["IX"] * "IX" + dict["V"] * "V" + dict["IV"] * "IV" + dict["I"] * "I"