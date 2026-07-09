# Attendance Management System

## Description

This project is a simple command-line Attendance Management System developed in Python. It records employee attendance based on their morning arrival and leaving time, classifies attendance status according to predefined working-hour rules, and generates a summary report.

The application is designed as a beginner-friendly Python project that demonstrates the use of loops, conditional statements, user input, and counters for tracking attendance statistics.

---

## Features

- Record attendance for multiple employees.
- Process attendance over multiple working days.
- Classify attendance into:
  - Present
  - Half Day
  - Short Attendance
  - Overtime
  - Absent
- Validate invalid time entries.
- Display attendance statistics after each employee.
- Generate a final attendance summary.

---

## Attendance Rules

| Status | Condition |
|---------|-----------|
| Present | Arrival at or before 8:00 and departure at 18:00 |
| Half Day | Worked only morning or afternoon shift |
| Short Attendance | Employee worked fewer than required hours |
| Overtime | Arrival before 8:00 and departure after 18:00 |
| Absent | Arrival time equals leaving time or either time is 0 |
| Invalid | Impossible or incorrect time entries |

---

## Technologies Used

- Python 3
- Command Line Interface (CLI)

---

## Project Structure

```
Attendance-Management-System/
│
├── attendance.py
└── README.md
```

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/Attendance-Management-System.git
```

2. Navigate to the project folder.

```bash
cd Attendance-Management-System
```

3. Run the program.

```bash
python attendance.py
```

---

## Sample Workflow

```
Day = 1
User = 1

Enter morning time:
Enter leaving time:

Attendance Status:
Present

Current Summary:
Present: 1
Half Day: 0
Absent: 0
Short Attendance: 0
Overtime: 0
```

---

## Learning Objectives

This project demonstrates:

- Nested loops
- Conditional logic
- Input validation
- Counter variables
- Console-based applications
- Basic program design

---

## Future Improvements

- Store attendance records in a file or database.
- Generate attendance reports in CSV or Excel format.
- Support minutes in addition to hours.
- Add employee names and IDs.
- Create a graphical user interface.
- Improve attendance rule flexibility.

---

## License

This project is open for learning and educational purposes.
