print("====================================")
print("   N.A.Y.A.B  AI  SYSTEM  v1.0")
print("   Neural Assistant for Your Ambitions & Brilliance")
print("====================================")
print("Status: Online 🟢 | Model: Muse Spark | Dev: Nayab")
print("")

user_name = input("AUTHENTICATE USER: Enter your name > ")
mood = input("SYSTEM SCAN: How are you feeling today? > ")

print("")
print("PROCESSING...")
print("Hello", user_name + ". N.A.Y.A.B AI here 🤖")
print("")

if "good" in mood.lower() or "acha" in mood.lower() or "great" in mood.lower():
    print("ANALYSIS: Positive energy detected ✨")
    print("RECOMMENDATION: Use this momentum. Code for 1 hour today.")
    print("STAT: Coders who practice daily have 73% higher success rate.")
    
elif "sad" in mood.lower() or "tired" in mood.lower() or "thak" in mood.lower():
    print("ANALYSIS: Low energy detected 💙")
    print("RECOMMENDATION: 10 min break lo. Phir 1 chota task karo.")
    print("STAT: Small wins rebuild momentum faster than rest.")
    
elif "stress" in mood.lower() or "papers" in mood.lower() or "exam" in mood.lower():
    print("ANALYSIS: Academic pressure detected 📚")
    print("RECOMMENDATION: Pomodoro technique use karo. 25 min study, 5 min break.")
    print("STAT: 2nd Year ke toppers yehi method use karte hain.")
    
else:
    print("ANALYSIS: Neutral state detected ⚙️")
    print("RECOMMENDATION: Ek naya Python concept seekho aaj.")
    print("STAT: Consistency > Intensity. Daily 1% better = 37x in 1 year.")

print("")
print("====================================")
print("N.A.Y.A.B AI: Session terminated. Keep building the future.")
print("====================================")
