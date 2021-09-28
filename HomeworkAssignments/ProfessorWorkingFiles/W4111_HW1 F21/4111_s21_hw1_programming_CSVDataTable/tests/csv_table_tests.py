"""

csv_table_tests.py

"""
from src.CSVDataTable import CSVDataTable

import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
data_dir = os.path.abspath("../Data/Baseball")


def tests_people():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }
    people = CSVDataTable("People", connect_info, ["playerID"])
    try:

        print()
        print("find_by_primary_key(): Known Record")
        print(people.find_by_primary_key(["aardsda01"]))

        print()
        print("find_by_primary_key(): Unknown Record")
        print(people.find_by_primary_key((["cah2251"])))

        print()
        print("find_by_template(): Known Template")
        template = {"nameFirst": "David", "nameLast": "Aardsma", "nameGiven": "David Allan"}
        print(people.find_by_template(template))

        # Please complete code IN THE SAME FORMAT to test when the rest of methods pass or fail
        # HINT HINT: Don't forget about testing the primary key integrity constraints!!
        # For these tests, think to yourself: When should this fail? When should this pass?
        print()
        print("delete_by_key(): Known Record")
        # should output 1
        print(people.delete_by_key(["aardsda01"]))

        print()
        print("delete_by_key(): Unkown Record")
        print(people.delete_by_key(["cah2251"]))

        print()
        print("delete_by_template(): Known Template")
        template = {"nameFirst": "Hank", "nameLast": "Aaron", "nameGiven": "Henry Louis"}
        print(people.delete_by_template(template))

        # check if can find by key aardsda01 and find by template hank, aaron, henry louis, if not then success
        print()
        print("find_by_primary_key() after deletion: should return empty list")
        print(people.find_by_primary_key(["aardsda01"]))

        print()
        print("find_by_template() after deletion: should return empty list")
        template = {"nameFirst": "Hank", "nameLast": "Aaron", "nameGiven": "Henry Louis"}
        print(people.find_by_template(template))

        print()
        print("insert(): previously deleted player with playerID aardsda01")
        dict_to_insert1 = {'playerID': 'aardsda01', 'birthYear': '1981', 'birthMonth': '12', 'birthDay': '27',
                          'birthCountry': 'USA', 'birthState': 'CO', 'birthCity': 'Denver', 'deathYear': '',
                          'deathMonth': '', 'deathDay': '', 'deathCountry': '', 'deathState': '', 'deathCity': '',
                          'nameFirst': 'David', 'nameLast': 'Aardsma', 'nameGiven': 'David Allan', 'weight': '215',
                          'height': '75', 'bats': 'R', 'throws': 'R', 'debut': '2004-04-06', 'finalGame': '2015-08-23',
                          'retroID': 'aardd001', 'bbrefID': 'aardsda01'}
        people.insert(dict_to_insert1)
        print(people.find_by_primary_key(["aardsda01"]))

        print()
        print("insert(): new player with playerID abcd01")
        dict_to_insert2 = {'playerID': 'abcd01', 'birthYear': '1990', 'birthMonth': '10', 'birthDay': '24',
                          'birthCountry': 'USA', 'birthState': '', 'birthCity': '', 'deathYear': '',
                          'deathMonth': '', 'deathDay': '', 'deathCountry': '', 'deathState': '', 'deathCity': '',
                          'nameFirst': 'Kamado', 'nameLast': 'Tanjiro', 'nameGiven': 'Bob Tanjiro', 'weight': '200',
                          'height': '75', 'bats': 'R', 'throws': 'R', 'debut': '2000-01-01', 'finalGame': '2020-12-31',
                          'retroID': 'abcd01', 'bbrefID': 'abcd01'}
        people.insert(dict_to_insert2)
        print(people.find_by_primary_key(["abcd01"]))

        print()
        print("insert(): player that already exists, should print statement stating that player already exists")
        people.insert(dict_to_insert2)

        print()
        print("update_by_template(): known template, should return 1")
        template = {"nameFirst": "David", "nameLast": "Aardsma", "nameGiven": "David Allan"}
        new_values = {"birthCountry": "China", "birthState": "Guangdong", "birthCity": "Zhuhai"}

        print(people.update_by_template(template, new_values))
        print(people.find_by_primary_key(["aardsda01"]))

        print()
        print("update_by_template() unknown: should return 0 and print player doesn't exist")
        template = {"playerID": "cah2251", "nameLast": "Simpson", "nameGiven": "Bart Simpson"}
        print(people.update_by_template(template, new_values))

        print()
        print("update_by_key(): should return 1")
        print(people.update_by_key(["abcd01"], new_values))
        print(people.find_by_primary_key(["abcd01"]))

    except Exception as e:
        print("An error occurred:", e)


def tests_batting():
    connect_info = {
        "directory": data_dir,
        "file_name": "Batting.csv"
    }
    batting = CSVDataTable("Batting", connect_info, ["playerID", "yearID", "stint"])
    try:

        print()
        print("find_by_primary_key(): Known Record")
        print(batting.find_by_primary_key(["abercda01", "1871", "1"]))

        print()
        print("find_by_primary_key(): Unknown Record")
        print(batting.find_by_primary_key((["abcd01", "1999", "1"])))

        print()
        print("find_by_template(): Known Template")
        template = {"teamID": "TRO", "lgID": "NA", "G": "1"}
        print(batting.find_by_template(template))

        print()
        print("delete_by_key(): Known Record")
        # should output 1
        print(batting.delete_by_key(["abercda01", "1871", "1"]))

        print()
        print("delete_by_key(): Unkown Record")
        print(batting.delete_by_key(["abcd01", "1999", "1"]))

        print()
        print("delete_by_template(): Known Template")
        template = {"teamID": "RC1", "AB": "118", "R": "30"}
        print(batting.delete_by_template(template))

        # check if can find by key (abercda01, 1871, 1) and find by template RC1, 118, 30, if not then success
        print()
        print("find_by_primary_key() after deletion: should return empty list")
        print(batting.find_by_primary_key(["abercda01", "1871", "1"]))

        print()
        print("find_by_template() after deletion: should return empty list")
        template = {"teamID": "RC1", "AB": "118", "R": "30"}
        print(batting.find_by_template(template))

        print()
        print("insert(): previously deleted player with playerID abercda01")
        dict_to_insert1 = {'playerID': 'abercda01', 'yearID': '1871', 'stint': '1', 'teamID': 'TRO', 'lgID': 'NA',
                           'G': '1', 'AB': '4', 'R': '0', 'H': '0', '2B': '0', '3B': '0', 'HR': '0', 'RBI': '0',
                           'SB': '0', 'CS': '0', 'BB': '0', 'SO': '0', 'IBB': '', 'HBP': '', 'SH': '', 'SF': '',
                           'GIDP': '0'}

        batting.insert(dict_to_insert1)
        print(batting.find_by_primary_key(["abercda01", "1871", "1"]))

        print()
        print("insert(): new player with primary key (abcd01, 1999, 1)")
        dict_to_insert2 = {'playerID': 'abcd01', 'yearID': '1999', 'stint': '1', 'teamID': 'TRO', 'lgID': 'NA',
                           'G': '100', 'AB': '100', 'R': '100', 'H': '100', '2B': '100', '3B': '100', 'HR': '100',
                           'RBI': '100',
                           'SB': '100', 'CS': '100', 'BB': '100', 'SO': '100', 'IBB': '', 'HBP': '', 'SH': '', 'SF': '',
                           'GIDP': ''}
        batting.insert(dict_to_insert2)
        print(batting.find_by_primary_key(["abcd01", "1999", "1"]))

        print()
        print("insert(): player that already exists, should print statement stating that player already exists")
        batting.insert(dict_to_insert2)

        print()
        print("update_by_template(): known template, update all players with teamID TRO and HR = 0 should return 20")
        template = {"teamID": "TRO", "HR": "0"}
        new_values = {"SB": "100", "CS": "100"}

        print(batting.update_by_template(template, new_values))
        print(batting.find_by_template(template))

        print()
        print("update_by_template() unknown: should return 0 and print player doesn't exist")
        template = {"teamID": "ABC", "G": "100"}
        print(batting.update_by_template(template, new_values))

        print()
        print("update_by_key(): should return 1")
        new_values = {"teamID": "LAL", "CS": "100"}
        print(batting.update_by_key(["abcd01", "1999", "1"], new_values))
        print(batting.find_by_primary_key(["abcd01", "1999", "1"]))

    except Exception as e:
        print("An error occurred:", e)


tests_people()
tests_batting()
