# names = "abcdiesd"
# vowel= "aeiou"

# # print(names)

# count = 0
# for letter in names:
#     if letter in vowel:
#         count+=1
#     print(count)

names = {
    "boy":54,
    "girl":65,
}
for key,val in enumerate(names):
    print(key,val)
print(names["girl"])
print(names.values())

# names.append("python")

# print(names[-1])

# print(len(names))
