#First import models
from models import db, Student, School, Application, User
from app import app


def run():
    # delete all existing data
    Student.query.delete()
    School.query.delete()
    Application.query.delete()
    User.query.delete()

    # Seed schools; might need to revisit zipcode starting with 0
    schools = [
        School(gov_id=1010, school_name="Alpha School", school_zip=60629, school_state="IL", school_city="Chicago"),
        School(gov_id=2020, school_name="Beta School", school_zip=79936, school_state="TX", school_city="El Paso"),
        School(gov_id=3030, school_name="Delta School", school_zip=90011, school_state="CA", school_city="Los Angeles"),
        School(gov_id=4040, school_name="Gamma School", school_zip=08701, school_state="NJ", school_city="Lakewood"),
        School(gov_id=5050, school_name="Zeta School", school_zip=10467, school_state="NY", school_city="Bronx")
    ]

    db.session.add_all(schools)
    db.session.commit()

    #Seed users - note doing this in individual variables instead of array because students will be assigned parent users like pets had owners
    smith123 = User(username="smith123", user_type="applicant", zip=60629)

    db.session.add_all([smith123, ])
    db.session.commit()

    #Seed students; note circle back to adding user= to all students similar to how pets had owner and rethink user_student relationship (E.g. should it live on student or what?)
    students = [
        Student(first_name="Jack", last_name="Smith", dob=1/1/2020, age=4, expected_grade_level="Kindergarten", user=smith123),
        Student(first_name="Jill", last_name="Smith", dob=1/1/2018, age=6, expected_grade_level="2nd Grade", user=smith123),
        Student(first_name="Jo", last_name="Self", dob=7/12/2019, age=5, expected_grade_level="1st Grade"),
        Student(first_name="Jen", last_name="Dovetheworld", dob=3/20/2020, age=4, expected_grade_level="Kindergarten"),
        Student(first_name="Jam", last_name="Berry", dob=9/1/2020, age=4, expected_grade_level="PreK"),
        Student(first_name="Jelly", last_name="Berry", dob=9/1/2020, age=4, expected_grade_level="PreK")

    ]

    db.session.add_all(students)
    db.session.commit()

    #Seed Applications; revisit after talking to Ben
    applications = [
        Application()
    ]

    db.session.add_all(applications)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():  # running out script inside and app context
        run()