from services.cluster import Cluster
from typing import Tuple
from models.student import Student

class Calculate:
    
    def define_cluster(student: Student, cluster1: Cluster, cluster2: Cluster):
        distance_from_centroid1 = student.calculate_euclidean_distante(cluster1.centroid)
        distance_from_centroid2 = student.calculate_euclidean_distante(cluster2.centroid)
        
        if distance_from_centroid1 < distance_from_centroid2:
            cluster1.addStudent(student)
            print(f"Cluster1 {cluster1.students}")
            print(f"Distância {distance_from_centroid1}")
            return cluster1
        cluster2.addStudent(student)
        print(f"Cluster2 {cluster1.students}")
        print(f"Distância2 {distance_from_centroid2}")
        return cluster2

        