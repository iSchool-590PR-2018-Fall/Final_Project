import random

# hist = input("Describe your level of experience with Python (beginner, intermediate, advanced, expert): ")
hist = 'expert'

def quiz_range(hist):
    """Determine the advantage a student has for the success in the course
    :param hist: A students prior history with coding
    :return first_score: The lower bounded score for assignments based on a student's history
    """
    if hist == 'beginner':
        first_score = 0
    if hist == 'intermediate':
        first_score = 30
    if hist == 'advanced':
        first_score = 60
    if hist == 'expert':
        first_score = 80
    return first_score

first_score = int(quiz_range(hist))

def quizzes(num_quiz, first_score):
    """Predict the grade for the students total quiz scores throughout the course
    :param num_quiz: Total number of quizzes in the course
    :param first_score: Given the history of the student, the first_score predicts a lower bound for quiz grades
    """
    num_quiz = num_quiz + 1
    quiz_list = []
    for quizzes in range(1, num_quiz):
        reading_adv = random.uniform(0, .2)
        quiz_raw = random.uniform(first_score, 100)
        quiz_1 = (quiz_raw * reading_adv) + quiz_raw
        if quiz_1 >= 100:
            quiz_grade = 100
        elif quiz_1 < 100:
            quiz_2 = random.uniform(quiz_1, 100)
            quiz_grade = (quiz_1 + quiz_2) / 2
        quiz_list.append(quiz_grade)
    final_quiz_grade = (sum(quiz_list)/8)/100
    return final_quiz_grade

total_quiz = quizzes(8, first_score)

def assignment_range(hist):
    """Determine the advantage a student has for the success in the course
        :param hist: A students prior history with coding
        :return lower_score: The lower bounded score for assignments based on a student's history
        """
    if hist == 'beginner':
        lower_score = 40
    if hist == 'intermediate':
        lower_score = 60
    if hist == 'advanced':
        lower_score = 75
    if hist == 'expert':
        lower_score = 85
    return lower_score

assign_range = assignment_range(hist)

def participation(num_classes):
    """Predict the grade for the students total participation in class
    :param num_classes: Total number of classes to participate in
    """
    part_total = 0
    total_classes = num_classes + 1
    for c in range(0, total_classes):
        part = random.uniform(0, 10)
        part_total += part
    part_total = part_total/(num_classes * 10)
    return part_total

total_part = participation(16)

# Create a function that randomly determines the outcome of group assignments
def group_assign(self, num_g_assign, first_score):
    """Predict the grade for the student's grades on the group assignments
    :param num_g_assign: Total number of group assignments
    """

    # They should have an advantage based on their prior experience and the other students will be completely random


# Create a function that randomly determines the outcome of indiviudal assignments
def ind_assign(self, num_i_assign):
    """Predict the grade for the student's individual assignments
    :param num_i_assign: Total number of individual assignments
    """
    # They should have an advantage if they have had prior experience

# Create a function that randomly determines the final project grade
def final_proj(self):
    """Predict the grade for the student's final project

    """
    # This could be completely random since we are working on it now?

# Create a function that adds all the grades up into one for a final probability
def grade(hist, part_points, quiz_points):
    """Use all of the following information and the weight of each grade to determine the final grade
        for the student in this course. Will they pass the course?
    :param hist: A students prior history with coding
    :param part_points: The total participation points calculated
    :param quiz_points: The total quiz points calculated
    """
    final_participation = part_points * .10
    final_quizzes = quiz_points * .15
    #final_assign = (group_points + ind_points + final_points) * .75

    total_points = final_participation + final_quizzes # + final_assign
    total_points = round(total_points * 100)

    if 100 <= total_points >= 93:
        print("As a/an", hist, ", your final grade is an A, and you have passed the course.")
    elif 92.9 <= total_points >= 90:
        print("As a/an", hist, ", your final grade is an A-, and you have passed the course.")
    elif 89.9 <= total_points >=87:
        print("As a/an", hist, ", your final grade is a B+, and you have passed the course.")
    elif 86.9 <= total_points >= 83:
        print("As a/an", hist, ", your final grade is a B, and you have passed the course.")
    elif 82.9 <= total_points >= 80:
        print("As a/an", hist, ", your final grade is a B-, and you have passed the course.")
    elif 79.9 <= total_points >= 77:
        print("As a/an", hist, ", your final grade is a C+, and you have passed the course.")
    elif 76.9 <= total_points >= 73:
        print("As a/an", hist, ", your final grade is a C, and you have passed the course.")
    elif 72.9 <= total_points >= 70:
        print("As a/an", hist, ", your final grade is a C-, and you have passed the course.")
    elif 69.9 <= total_points >= 65:
        print("As a/an", hist, ", your final grade is a D, and you have NOT passed the course.")
    elif total_points <= 65:
        print("As a/an", hist, ", your final grade is an F, and you have NOT passed the course.")

grade(hist, total_part, total_quiz)
