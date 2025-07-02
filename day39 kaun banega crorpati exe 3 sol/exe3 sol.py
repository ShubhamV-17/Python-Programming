import random
questions=[
     {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
     {
        "question": "Who wrote the national anthem of India?",
        "options": ["A.Bankim Chandra Chatterjee", "B.Rabindranath Tagore", "C.Sarojini Naidu", "D.Subhash Chandra Bose"],
        "answer": "B"
    },
     {
        "question": "What is the capital of Australia?",
        "options": ["A.Sydney", "B.Melbourne", "C.Canberra", "D.Perth"],
        "answer": "C"
    },
     {
         "question": "Which organ purifies our blood?",
        "options": ["A.Liver", "B.Heart", "C.Lungs", "D.Kidney"],
        "answer": "D"
    },
]
prizes=[1000,4000,10000,50000]
lifeline_used=True
def use_5050(options,correct_answer):
    incorrect=[opt for opt in options if opt != correct_answer] # opt= answer option
    removed = random.sample(incorrect,2) 
    new_options = [opt for opt in options if opt not in removed]
    return new_options

print("🟡 Welcome to KBC - Kaun Banega Crorepati!")
print("🎮 You will be asked 5 questions. Each correct answer increases your prize.")
print("📞 You have one lifeline: 50-50.\n")
for i, q in enumerate(questions):
    print(f"\nQuestion for ₹{prizes[i]}")
    print(q["question"])
    for idx, opt in enumerate(q["options"]):
        print(f"{opt}")
    answer = input("enter your answer:").strip().upper()

    try:
        chosen_option = q["options"][ord(answer) - 65]
    except:
        print("❌ Invalid option. Game Over.")
        break

    if answer == q["answer"]:
        print(f"✅ Correct! You’ve won ₹{prizes[i]}")
    else:
        print(f"❌ Wrong! The correct answer was: {q['answer']}")
        print(f"You leave with ₹{prizes[i-1] if i > 0 else 0}")
        break

else:
    print(f"\n🎉 Congratulations! You’ve won the top prize of ₹{prizes[-1]}!")



    