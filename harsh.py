# Decorator
def deco(func):
    def wrap(self):
        print("*" * 20)
        func(self)
        print("*" * 20)
    return wrap


class Report:
    template = "Student Report"

    # Constructor
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class Method
    @classmethod
    def change_template(cls, new_template):
        cls.template = new_template

    # Magic Method
    def __str__(self):
        return f"Template: {Report.template}\nTitle: {self.title}\nContent: {self.content}"

    # Display Method
    @deco
    def display(self):
        print(self)


# Change Template
Report.change_template("Hotel Report")

# Create Object
hotel = Report(
    "Grand Palace Hotel Report",
    "Luxury hotel with 150 rooms, 92% occupancy, 4.7/5 customer rating, located in Pune."
)

# Display Report
hotel.display()