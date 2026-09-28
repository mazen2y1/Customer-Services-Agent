from Agent import chat
while True:
    message = input("\nCustomer : ")
    if message.lower() == "exit":
        break
    response = chat(message)
    print("\nAgent : ",response)