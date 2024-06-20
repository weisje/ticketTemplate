import pyperclip
import sys
import datetime


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

def main(keyphrase) -> None:
    """
    Main function for tickTemp.py to copy user's keyphrase to the clipboard
    :param keyphrase: dictionary key for the phrase the user wants to copy to the clipboard
    :type keyphrase: str
    :return: None
    """
    TEXT = {"agree": """This is true.  I agree.""",
            "busy": """I apologize but I have a lot going on right now.  Can this wait?""",
            "template": """Username:
Customer: N/A
Description:
Error: N/A
Verdict:
Article:"""}
    timeGreeting = timeOfDay()

    if keyphrase in TEXT:
        if keyphrase == "template":
            print(TEXT[keyphrase])
        else:
            print(f"\nGood {timeGreeting},\n\n{TEXT[keyphrase]}\n")
    else:
        print(f"\'{keyphrase}\' is not a valid selection.")
        sys.exit()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: tickTemp.py [keyphrase] -> Copy body of keyphrase to clipboard")
        sys.exit()

    main(sys.argv[1])
