response = {
    "hi":"hello",
    "how are you":"i am fine",
    "what is your name": "I am a simple Python chatbot.",
    "bye": "Goodbye! Have a nice day.",
    "help": "Sure! Tell me what you need help with.",
    "thanks": "You're welcome!",
    "what can you do": "I can reply to simple questions.",
    "who made you": "I was created using Python programming by Rouqia.",
    "ok": "Alright!"
}
def get_response_of_bot(userinput):
    for eachkey in response:
        if eachkey in userquestion:
            return response[eachkey]
    return"i will learn soon"    
userquestion= input("ask anything: ")
replay= get_response_of_bot(userquestion)
print("bot response: ",replay)