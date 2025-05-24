from services.euclidean_distance import euclidian_distance
from services.csv_reader import CSVReader
from services.initial_centroid import initial_centroid

def main():
    csv_file = 'alunos1.csv'
    people = CSVReader.readCsv(csv_file)
    centroid = initial_centroid(people)
    print(centroid)
    distance = euclidian_distance(centroid)
    
    print(f"Distância {distance}")
    
if __name__ == "__main__":
    main()