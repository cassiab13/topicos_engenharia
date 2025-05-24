import random

def initial_centroid(students, n=2):
    initial_centroids = random.sample(students, n)
    return [(p.age, p.grade_avg, p.absences) for p in initial_centroids]