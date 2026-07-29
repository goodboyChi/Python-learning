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
    45:65,
}
if "boy" in names:
    print(names["boy"])
else:
    print("not found")
for key,val in names.items():
    print(key,val)
print(names[45])
print(names.values())
print(names.items())
print(names.keys())
# names.append("python")

# print(names[-1])

# print(len(names))
