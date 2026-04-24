from datetime import date


class Assessment:
    def __init__(self, name:str , type:str , score:float):        
        self.name = name
        self.type = type
        self.score = score

        if self.score > 100:
            raise ValueError("Can't be higher then 100")
        
        if self.score < 0:
            raise ValueError("Can't be lower then 0")
        
        if self.type != "multiple-choice" : 
            if self.type !="technical" :
                if self.type != "presentation":
                    raise ValueError("invalid type")
        


class Trainee:
    def __init__(self, name:str , email:str , date_of_birth:date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = list()
        

    def get_age(self):
        age = date.today() - self.date_of_birth
        return age.days // 365
    
    def add_assessment(self, assessment: Assessment) -> None:
        return self.assessments.append(assessment)

    def get_assessment(self ,name: str) -> Assessment | None:
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
            return None






if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
