required_classes = {
    # Bioscience (need 1 from group 1)
    'BS 161', 'ENT 205', 'IBIO 150', 'MGI 141', 'MGI 201', 'PLB 105', 'PSL 250',
    # Bioscience Lab (need 1 from group 2)
    'BS 171', 'CEM 161', 'CEM 162', 'PHY 191', 'PHY 192', 'PLB 106',
    # Core CS courses (all required)
    'CSE 232', 'CSE 260', 'CSE 300', 'CSE 320', 'CSE 325', 'CSE 331', 
    'CSE 335', 'CSE 380', 'CSE 498', 'STT 351',
    # Math requirement (need 1)
    'MTH 314', 'MTH 317H',
    # Electives (need 5 from these)
    'CSE 402', 'CSE 404', 'CSE 410', 'CSE 415', 'CSE 420', 'CSE 422',
    'CSE 425', 'CSE 431', 'CSE 434', 'CSE 435', 'CSE 440', 'CSE 450',
    'CSE 460', 'CSE 471', 'CSE 472', 'CSE 476', 'CSE 477', 'CSE 480',
    'CSE 482', 'CSE 491', 'MTH 451'
}

students = {
    'Alice': ['CSE 232', 'CSE 260', 'CSE 300', 'CSE 320', 'BS 161', 'CEM 161', 'MTH 314', 'CSE 404', 'CSE 440'],
    'Bob': ['CSE 325', 'CSE 331', 'CSE 335', 'CSE 380', 'IBIO 150', 'PHY 191', 'CSE 422', 'CSE 425', 'CSE 480'],
    'Carol': ['CSE 498', 'STT 351', 'CSE 410', 'CSE 435', 'CSE 472', 'MGI 201', 'BS 171', 'MTH 317H'],
    'David': ['CSE 232', 'CSE 260', 'CSE 331', 'CSE 335', 'PSL 250', 'PHY 192', 'CSE 415', 'CSE 431', 'CSE 482'],
    'Eve': ['CSE 300', 'CSE 320', 'CSE 325', 'CSE 380', 'ENT 205', 'CEM 162', 'CSE 420', 'CSE 450', 'CSE 471'],
    'Frank': ['CSE 498', 'STT 351', 'CSE 402', 'CSE 434', 'CSE 476', 'PLB 105', 'PLB 106', 'MTH 314'],
    'Grace': ['CSE 232', 'CSE 335', 'CSE 498', 'CSE 440', 'CSE 477', 'MGI 141', 'CEM 161', 'CSE 460'],
    'Henry': ['CSE 260', 'CSE 320', 'CSE 331', 'CSE 380', 'CSE 410', 'BS 161', 'PHY 191', 'MTH 451'],
    'Iris': ['CSE 300', 'CSE 325', 'STT 351', 'CSE 422', 'CSE 435', 'CSE 480', 'IBIO 150', 'BS 171'],
    'Jack': ['CSE 232', 'CSE 260', 'CSE 498', 'CSE 415', 'CSE 425', 'CSE 472', 'PSL 250', 'PHY 192', 'MTH 317H'],
    'Kelly': ['CSE 331', 'CSE 335', 'CSE 380', 'CSE 491', 'CSE 460', 'CSE 477', 'ENT 205', 'CEM 162'],
    'Leo': ['CSE 232', 'CSE 300', 'CSE 320', 'CSE 325', 'CSE 434', 'CSE 471', 'MGI 141', 'PHY 192', 'MTH 314']
}


current_courses_covered = set()

for student, courses in students.items():
    for course in courses:
        current_courses_covered.add(course)
    if current_courses_covered == required_classes:
        print(f"All required classes are covered by the first {list(students.keys()).index(student) + 1} students.")
        break
