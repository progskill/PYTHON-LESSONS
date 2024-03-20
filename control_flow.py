def checkVowel(n):
  match n:
    case "a":
      return "Vowel alphabet"
    case "e":
      return "Vowel alphabet"
    case "i":
      return "Vowel alphabet"
    case "o":
      return "Vowel alphabet"
    case "u":
      return "Vowel alphabet"
    case _:
      return "Consonant alphabet"


print(checkVowel("a"))
print(checkVowel("m"))
print(checkVowel("o"))