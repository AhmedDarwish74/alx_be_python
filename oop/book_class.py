class Book:
    def __init__(self,title,auther,year):
        self.title = title
        self.auther = auther
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")
    
    def __str__(self):
        return f"{self.title} by {self.auther}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}','{self.auther}','{self.year}'"
        