import sys


def main(keyphrase) -> None:
    """
    Main function for tickTemp.py to copy user's keyphrase to the clipboard
    :param keyphrase: dictionary key for the phrase the user wants to copy to the clipboard
    :type keyphrase: str
    :return: None
    """
    pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: tickTemp.py [keyphrase] -> Copy body of keyphrase to clipboard")
        sys.exit()

    main(sys.argv[1])
