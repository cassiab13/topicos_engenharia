from services.csv_reader import CSVReader
from services.initial_centroid import initial_centroid
from services.cluster import Cluster
from services.calculate import Calculate

def main():
    csv_file = 'alunos1.csv'
    students = CSVReader.readCsv(csv_file)
    centroid = initial_centroid(students)
    cluster1 = Cluster(centroid[0])
    cluster2 = Cluster(centroid[1])
    
    for student in students:
        cluster = Calculate.define_cluster(student, cluster1, cluster2)
        cluster.calculate_centroid()
        print(f"New centroid {cluster.centroid}")
    print(f"Cluster1: {cluster1.students}")
    print(f"Cluster2: {cluster2.students}")
    return cluster1.centroid, cluster2.centroid

    

    
    
if __name__ == "__main__":
    main()