
palindromes = [
    "A to kiwi zdziwi kota.",
    "A klei Popiel kota.",
    "A to kurdupel! Ile pudru kota?",
    "A tu mamy mamuta.",
    123123123,
    "A warta kosy wysoka trawa?",
    "Ada baluje – Jula bada.",
    "Ada baniak Kaina bada."
]

def palindrom_list_checker(palindrom_list):
    palindrom_dict = {i: [v, 0] for i, v in enumerate(palindromes)}
    palindromes_strings = [str(pal) for pal in palindromes]
    for i, v in enumerate(palindromes_strings):
        if v == v[-1:1]:
            palindrom_dict[i][1] += 1
    not_palindromes = [palindrom_state[0] for palindrom_state in palindrom_dict.values() if palindrom_state[1] == 0]
    return not_palindromes


print(palindrom_list_checker(palindromes))