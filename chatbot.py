import time

def chatbot():
    print("📦 Welcome to eGain Package Tracker Bot!")
    print("How can I help you today?")
    
    user_input = input("> ").lower()
    
    if "lost" in user_input or "track" in user_input:
        print("I'm sorry to hear that! Can you provide your tracking number?")
        tracking_number = input("Tracking number: ")
        
        if len(tracking_number) == 10 and tracking_number.isalnum():
            print("Thanks! Let me check that for you...")
            time.sleep(2)  # simulate a delay
            print("✅ Your package was last seen in Chicago, IL on March 30th.")
            print("Would you like me to file a missing package report? (yes/no)")
            report = input("> ").lower()
            if "yes" in report:
                print("📨 Done! A report has been filed. You’ll receive updates by email.")
            else:
                print("👍 Alright! Let me know if you need anything else.")
        else:
            print("⚠️ Hmm, that tracking number doesn’t look right. Can you double-check it?")
    else:
        print("🤔 Sorry, I didn’t understand that. I'm here to help with lost packages.")
        # optional retry logic

chatbot()
