import json
question_bank = """
{"Question":
[
    {
        "name": "How many Infinity Stones are there?",
        "options" :["3","4","5","6"] ,
        "answer" : "5"
    },
    
    {
        "name": "What is the only food that cannot go bad?",
        "options": ["Honey","Dark chocolate","Peanut butter","Canned tuna"],
        "answer": "Honey"
    },
    {
        "name":"What is the most visited tourist attraction in the world?",
        "options":["Statue of Liberty", "Eiffel Tower","Great Wall of China", "Colosseum"],
        "answer":"Eiffel Tower"
    },
    {
        "name":"What is the heaviest organ in the human body?",
        "options": ["Brain","Skin","Heart","Liver"],
        "answer": "Liver"
    },
    {
        "name": "Who made the third most 3-pointers in the Playoffs in NBA history", 
        "options": ["Kevin Durant", "JJ Reddick","Lebron James", "Kyle Korver"],
        "answer": "Lebron James"
    },
    {
        "name": "Which of these EU countries does not use the euro as its currency?", 
        "options": ["Poland","Denmark", "Sweden","All of the above"] ,
        "answer": "All of the above"
    },
    {
        "name": "Which US city is the sunniest major city and sees more than 320 sunny days each year?", 
        "options": ["Phoenix","Miami","San Francisco","Austin"],
        "answer": "Phoenix"
    },
    {
        "name": "What type of food holds the world record for being the most stolen around the globe?", 
        "options": ["beef","Coffee","Cheese","Chocolate"],
        "answer": "Cheese"
    }

]

}
"""
data = json.loads(question_bank)

with open("Question Bank.json", "w") as questions:
    json.dump(data,questions)