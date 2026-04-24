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
        if self.type != "multiple-choice":
            if self.type !="technical":
                if self.type != "presentation":
                    raise ValueError("invalid type")
    def calculate_score(self):
        return self.score * self.weighting

class MultipleChoiceAssessment(Assessment):
    def __init__(self, name, score):
        super().__init__(name, "multiple-choice", score)
        self.weighting = 0.70

class TechnicalAssessment(Assessment):
    def __init__(self, name, score):
        super().__init__(name, "technical", score)
        self.weighting = 1.0

class PresentationAssessment(Assessment):
    def __init__(self, name,  score ):
        super().__init__(name, "presentation", score)
        self.weighting = 0.6

class Trainee:
    def __init__(self, name:str , email:str , date_of_birth:date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = list()

    def get_age(self):
        '''Gets your age from today'''
        age = date.today() - self.date_of_birth
        return age.days // 365

    def add_assessment(self, assessment: Assessment) -> None:
        if not isinstance(assessment, Assessment):
            raise TypeError("Not a subclass")
        self.assessments.append(assessment)

    def get_assessment(self ,name: str) -> Assessment | None:
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
            return None

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        list_assessments = list()
        for assessment in self.assessments:
            if assessment.type == type:
                list_assessments.append(assessment)
        return list_assessments


class Question:

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:

    def __init__(self, quiz: Quiz) -> None:
        self._quiz = quiz

    def mark(self) -> int:
        total_score = 0
        for question in self._quiz.questions:
            if question.chosen_answer == question.correct_answer:
                total_score += 1
        if total_score == 0:
            return 0
        return round((total_score / len(self._quiz.questions)) * 100)

    def generate_assessment(self) -> Assessment:
        if self._quiz.type == "technical":
            return TechnicalAssessment(self._quiz.name, self.mark())
        if self._quiz.type == "multiple-choice":
            return MultipleChoiceAssessment(self._quiz.name, self.mark())
        if self._quiz.type == "presentation":
            return PresentationAssessment(self._quiz.name , self.mark())

if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
