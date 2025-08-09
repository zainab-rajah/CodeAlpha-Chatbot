# questions:answer

qna={
    "hi":"hello" ,
    "how are you":"I am good" ,
    "who are you": ", a simple chatbot created to assist you.",
    "your good name please!":"your AI powered assistant! Gemini , How may I help you",
    "what can you do": "I can answer basic questions and help you with simple tasks.",
    "thank you": "You're welcome!",
    "thanks": "Glad I could help!",
    "bye": "Goodbye! Have a great day!",
    "goodbye": "See you later! Take care."
}
while True:
    queries=input("enter your query: ").lower()
     
    if (queries=="bye"):
        break
    elif queries in qna:
      print(qna[queries])
    else:
     print("Sorry I don't understand")
