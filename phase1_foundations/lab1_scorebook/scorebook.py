from datetime import date 
import csv 
from statistics import mean,median
print("Welcome to The Score Book")
print("today: ", date.today())
grades=[]

class student:
    def __init__(self,name,quiz,hw,exam):
        self.name=name
        self.quiz=quiz
        self.hw=hw
        self.exam=exam
    def final_score(self):
        return (self.quiz+self.hw+self.exam) / 3





def add_record(records):
    name=input("student name: ")
    while True:
        try:
            quiz = int(input("Quiz score: "))
            hw = int(input("Homework score: "))
            exam = int(input("Exam score: "))
            break
        except ValueError:
            print("Invalid number.")
    record = {
    "name": name,
    "quiz": quiz,
    "hw": hw,
    "exam": exam
}
    records.append(record)
    print("student added ")
    
        
def avg_grade(record):
    return (record["quiz"]+record["hw"]+record["exam"])/3
def class_stats(records):
    if not records:
        print("no record available ")
        return 
    scores=[]
    for r in records:
        scores.append(avg_grade(r))
    print("Class Statistics")
    print("Students:", len(scores))
    print("Average:", round(mean(scores), 2))
    print("Median:", round(median(scores), 2))
    print("Highest:", round(max(scores), 2))
    print("Lowest:", round(min(scores), 2))
    print()


     
def load_csv(path):
    result=[]
    try:
        with open(path,mode='r',newline='',encoding='utf-8') as csv_file:
            csv_reader=csv.DictReader(csv_file)
            for row in csv_reader:
                result.append({"name":row["name"],"quiz":int(row["quiz"]),"hw":int(row["hw"]),"exam":int(row["exam"])})
        print("data loaded from csv")

    except FileNotFoundError:
        print("File not found")

    return result


def save_csv(records, path):
    
    with open(path,mode='w',newline='') as csv_file:
        fieldnames=["name","quiz","hw","exam"]
        writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
        print("data saved to csv")
        

def list_records(records):
    if not records:
        print("No records.\n")
        return

    for r in records:
        print(
            f"{r['name']} , Quiz: {r['quiz']} , HW: {r['hw']} , "
            f"Exam: {r['exam']} , Final: {round(avg_grade(r),2)}"
        )
    print()
    

if __name__ == "__main__":
    
    records = [
        {"name": "Ava", "quiz": 9, "hw": 8, "exam": 87},
        {"name": "Liam", "quiz": 7, "hw": 10, "exam": 92},
        {"name": "Emma", "quiz": 8, "hw": 9, "exam": 85},
    ]

    while True:
        print("here is the app menu :")
        
        print('''[1] Add\n
                [2] List\n
                [3] Stats\n
                [4] Save\n
                [5] Load\n
                [0] Exit        
            ''')
        choice=(input("Enter ur choice: "))
        if choice == "1":
            add_record(records)
            print(records)

        elif choice == "2":
            list_records(records)

        elif choice == "3":
            class_stats(records)

        elif choice == "4":
            save_csv(records, "grades.csv")

        elif choice == "5":
            records = load_csv("grades.csv")

        elif choice == "0":
            print("Goodbye")
            break

        else:
            print("Invalid option")
            
  
        
    
    
        
    
    
        
    
        
        
        

