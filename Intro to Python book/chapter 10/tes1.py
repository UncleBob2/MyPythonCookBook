import time, datetime

# Custom object to hold article date and time
class customObject:
    def __init__(self, title, date):
        self.title = title
        self.date = datetime.strptime(date, "%B %d, %Y")


def main():

    obj3 = customObject("TLS 1.3 - Better, Stronger, Faster", "January 6, 2018")
    obj4 = customObject(
        "User Interface Testing with Swift and XCTest", "December 10, 2017"
    )
    obj2 = customObject("How to Use Python List Comprehensions", "December 2, 2017")
    obj1 = customObject("Attending WWDC 2017 - Predictions Answered", "June 13, 2017")
    obj5 = customObject(
        "Swift Network Testing - Automate XCTest with Python", "November 26, 2017"
    )

    print("---------------------------------------------------------------")

    # Display the dates and titles
    print("Unsorted Date from obj1: " + str(obj1.date) + " with title: " + obj1.title)
    print("Unsorted Date from obj2: " + str(obj2.date) + " with title: " + obj2.title)
    print("Unsorted Date from obj3: " + str(obj3.date) + " with title: " + obj3.title)
    print("Unsorted Date from obj4: " + str(obj4.date) + " with title: " + obj4.title)
    print(
        "Unsorted Date from obj5: "
        + str(obj5.date)
        + " with title: "
        + obj5.title
        + "\n"
    )


main()
