colors = {
    "green": "GREEN",
    "blue": "BLUE",
    "red": "RED",
    "yellow": "yellow",
}

## Tasks:
# 1. Print all the keys in the dictionary
# 2. Print all values in the dictionary
# 3. Set the value of "red" to "reddish"
# 4. Set all the values to the uppercase form of the corresponding key
# 5. Print a list of tuples in the form: (key, value)
# 6. Check if "brown" is present in the dictionary
# 7. Print the value of "brown", or "No such color" if "brown" is not present
# 8. Add a "black" key with a "BLACK" value
# 9. Modify the dictionary so that "red" is "ROSE" and "yellow" is "SUN".
# 10. Remove "green" from the dictionary
# 11. Remove and print the value of the "blue"


cold_colors = dict(
    green="GREEN",
    blue="BLUE",
)

warm_colors = {
    "red": "RED",
    "yellow": "YELLOW",
}

# Merge cold_colors and warm_colors

company = {
    "board-management": {
        "John Smith": {
            "position": "CEO",
            "salary": 1000,
            "languages": ["english", "french", "german"],
            "is_manager": True,
            "employee_id": 5,
        },
        "Jane Doe": {
            "position": "Director",
            "salary": 1000,
            "languages": ["english", "italian"],
            "is_manager": True,
            "employee_id": 2,
        },
        "Roger McDonald": {
            "position": "Owner",
            "salary": 1500,
            "languages": ["english", "spanish"],
            "is_manager": True,
            "employee_id": 1,
        },
    },
    "employees": {
        "ProjectCosmos": {
            "百姓": {
                "position": "project-manager",
                "is_manager": True,
                "salary": 800,
                "languages": ["english", "chinese"],
                "employee_id": 3,
            },
            "عبد العزيز": {
                "position": "developer",
                "is_manager": False,
                "salary": 750,
                "languages": ["english", "arabic"],
                "employee_id": 4,
            },
            "Jane Żołądź": {
                "position": "developer",
                "salary": 750,
                "languages": ["English", "polish", "russian"],
                "employee_id": 9,
            },
            "Gregory Foo": {
                "position": "QA",
                "salary": 680,
                "languages": ["english", "french"],
                "employee_id": 6,
            },
            "Mark Exemplar": {
                "position": "QA",
                "salary": 630,
                "languages": ["english"],
                "employee_id": 10,
            },
        },
        "ProjectUniversum": {
            "Maria Esperanta": {
                "position": "project-manager",
                "is_manager": True,
                "salary": 830,
                "languages": ["Spanish", "Portugese", "Esperanto"],
                "employee_id": 7,
            },
            "Miguel Hugo": {
                "position": "statistician",
                "salary": 870,
                "languages": ["spanish", "english", "German"],
                "employee_id": 8,
            },
        },
    }
}

## Tasks:
# 1. All the names of the people in the company sorted by name in ascending order
# 2. All the names of the people in the company sorted by last name in descending order
# 3. Print the minimum salary
# 4. Print the maximum salary
# 5. Print the average salary of people who are managers
# 6. Make a dictionary (and print) the occurences of languages, e.g.: { "french": 2, "polish": 1, ...}
# 7. Make a dictionary (and print) of the people grouped by language, e.g. {"polish": ["Jan Żołądź"], "french": ["John Smith", "Gregory Foo"], ...}
# 8. Add a "Victor McKinley" to ProjectUniversum who earns 900, is a mathematician and speaks english and italian
# 9. Remove Mark Exemplar from ProjectCosmos
# 10. Print all people in the company order by their employee_id
