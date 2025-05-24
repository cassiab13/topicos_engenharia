from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    grade_avg: float
    absences: float