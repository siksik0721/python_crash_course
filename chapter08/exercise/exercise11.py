def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        sent_messages.append(message)


messages = ["Hello", "Hi"]
print("Orinial messages:")
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("Send messages!")
print("messages:")
show_messages(messages)
print("sent_messages:")
show_messages(sent_messages)
