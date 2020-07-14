# Print out each element of the following array on a separate line:
# ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# list = ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]

# # for i in list:
# #     print(i)

# print(*list, sep = "\n")


# Print out each element of the following array on a separate line, but this time the input array can contain arrays nested to an arbitrarily deep level:
# ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]
# For the above input, the expected output is:
# Bob
# Slack
# reddit
# 89
# 101
# alacritty
# (brackets)
# 5
# 375
# 0
# {slice, owned}
# 22
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

liist = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

# print(type(liist))

def print_list(lst):
    # elist = []

    for i in lst:
        if type(i) is not type(list):
            print(i)
        else:
            print_list(i)

print_list(liist)

# isinstance