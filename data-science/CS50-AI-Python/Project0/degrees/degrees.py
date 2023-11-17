import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }
            
    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass
"""
    print(names) after load_data(small) is complete:
    
    {'bill paxton': {'200'},
     'cary elwes': {'144'},
     'chris sarandon': {'1697'},
     'demi moore': {'193'},
     'dustin hoffman': {'163'},
     'emma watson': {'914612'},
     'gary sinise': {'641'},
     'gerald r. molen': {'596520'},
     'jack nicholson': {'197'},
     'kevin bacon': {'102'},
     'mandy patinkin': {'1597'},
     'robin wright': {'705'},
     'sally field': {'398'},
     'tom cruise': {'129'},
     'tom hanks': {'158'},
     'valeria golino': {'420'}}


    print(people) after load_data(small) is complete:
    
    {'102': {'birth': '1958', 'movies': {'104257', '112384'}, 'name': 'Kevin Bacon'},
    '129': {'birth': '1962', 'movies': {'104257', '95953'}, 'name': 'Tom Cruise'},
    '144': {'birth': '1962', 'movies': {'93779'}, 'name': 'Cary Elwes'},
    '158': {'birth': '1956', 'movies': {'109830', '112384'}, 'name': 'Tom Hanks'},
    '1597': {'birth': '1952', 'movies': {'93779'}, 'name': 'Mandy Patinkin'},
    '163': {'birth': '1937', 'movies': {'95953'}, 'name': 'Dustin Hoffman'},
    '1697': {'birth': '1942', 'movies': {'93779'}, 'name': 'Chris Sarandon'},
    '193': {'birth': '1962', 'movies': {'104257'}, 'name': 'Demi Moore'},
    '197': {'birth': '1937', 'movies': {'104257'}, 'name': 'Jack Nicholson'},
    '200': {'birth': '1955', 'movies': {'112384'}, 'name': 'Bill Paxton'},
    '398': {'birth': '1946', 'movies': {'109830'}, 'name': 'Sally Field'},
    '420': {'birth': '1965', 'movies': {'95953'}, 'name': 'Valeria Golino'},
    '596520': {'birth': '1935', 'movies': {'95953'}, 'name': 'Gerald R. Molen'},
    '641': {'birth': '1955', 'movies': {'109830', '112384'}, 'name': 'Gary Sinise'},
    '705': {'birth': '1966', 'movies': {'93779', '109830'}, 'name': 'Robin Wright'},
    '914612': {'birth': '1990', 'movies': set(), 'name': 'Emma Watson'}}

    
    print(movies) after load_data(small) is complete:
    
    {'104257': {'stars': {'102', '129', '193', '197'},
                'title': 'A Few Good Men',
                'year': '1992'},
     '109830': {'stars': {'158', '398', '641', '705'},
                'title': 'Forrest Gump',
                'year': '1994'},
     '112384': {'stars': {'102', '200', '158', '641'},
                'title': 'Apollo 13',
                'year': '1995'},
     '93779': {'stars': {'1597', '705', '1697', '144'},
               'title': 'The Princess Bride',
               'year': '1987'},
     '95953': {'stars': {'596520', '129', '163', '420'},
               'title': 'Rain Man',
               'year': '1988'}}
"""
    



def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # TODO
    raise NotImplementedError


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
