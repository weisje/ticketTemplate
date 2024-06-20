import datetime
import pyperclip
import random
import sys


def timeOfDay() -> str:
    """
    Function to get the current hour & provide a "Greeting" to the caller based on the hour of the day
    :return: str
    """
    currentHour = datetime.datetime.now().hour
    currentTimeOfDay = "Day"

    if currentHour < 12 and currentHour >= 3:
        currentTimeOfDay = "Morning"
    elif currentHour < 17 and currentHour >= 12:
        currentTimeOfDay = "Afternoon"
    elif currentHour < 3 and currentHour >= 17:
        currentTimeOfDay = "Evening"

    return currentTimeOfDay


def cannedGreeting(greetingType="general") -> str:
    """
    Function to take in selection from caller and provide a randomly selected "greeting" for the message being returned
    :param greetingType: type of greeting that should be returned to the caller. if the greeting requested is not found, a boilerplate general message will be returned.
    :type greetingType: str
    :return: str
    """
    greetings = {"request": ["Thank you for submitting this request",
                             "Thank you for submitting this service request"],
                 "general": ["Thank you for reaching out about this",
                             "Thank you for bringing this to our attention"]}

    if greetingType in greetings:
        return random.choice(greetings[greetingType])
    else:
        return random.choice(greetings["general"])

def main(keyphrase) -> None:
    """
    Main function for tickTemp.py to copy user's keyphrase to the clipboard
    :param keyphrase: dictionary key for the phrase the user wants to copy to the clipboard
    :type keyphrase: str
    :return: None
    """
    TEXT = {"accountworksnoaction": "We have reviewed your account and you should be able to access it now.  If you still cannot access it in 48 hours let us know & we will troubleshoot further.",
            "accountworksaction": "We have made adjustments to your account and you should be able to access it now.  If you still cannot access it in 48 hours let us know & we will troubleshoot further.",
            "sendtohr": "After reviewing this we have determined that it will need to be reviewed by the Human Resources department.  They can be reached at hr@iqtech.555 or by phone at 555-555-5555. They will be able to assist you further.",
            "template": """Username:
Customer: N/A
Description:
Error: N/A
Verdict:
Article:"""}
    timeGreeting = timeOfDay()
    introGreetng = cannedGreeting()
    cannedSalutations = ["Have a good day",
                         "Take care",
                         "Have a great day"]

    salutation = random.choice(cannedSalutations)

    signature = """John Q. Smith
Senior Help Desk Technician
Information Technology Department
IQ Technology
"""

    if keyphrase in TEXT:
        if keyphrase == "template":
            print(TEXT[keyphrase])
        else:
            print(f"\nGood {timeGreeting},\n\n{introGreetng}. {TEXT[keyphrase]} {salutation}.\n\n{signature}")
    else:
        print(f"\'{keyphrase}\' is not a valid selection.")
        sys.exit()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: tickTemp.py [keyphrase] -> Copy body of keyphrase to clipboard")
        sys.exit()

    main(sys.argv[1])
