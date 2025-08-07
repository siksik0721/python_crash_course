magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

# for magician in magicians:
# print(magician)   # IndentationError : expected an indented block after 'for' statement

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")  # logical error

# message = "Hello Python world!"
#     print(message)    # IndentationError: unexpected indent

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you, everyone. That was a great magic show!")  # logical error

# for magician in magicians # SyntaxError: expected ':'
#     print(magician)
