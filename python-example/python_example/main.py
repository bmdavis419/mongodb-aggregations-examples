import pymongo
import pandas as pd
import numpy as np


def main():
    print("Connecting to MongoDB...")

    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = my_client["mongodb-aggregate-example"]
    my_col = my_db["students"]

    print("Connected to MongoDB!")

    print("Aggregating...")

    # create the pipeline
    pipeline = [
        # project the fields we want (name, section, and final 2)
        {
            "$project": {
                "name": 1,
                "section": 1,
                "final 2": 1
            }
        },
        # sort by section and final 2
        {
            "$sort": {
                "section": 1,
                "final 2": -1
            }
        },
        # group by section
        {
            "$group": {
                "_id": "$section",
                "students": {
                    "$push": {
                        "name": "$name",
                        "final 2": "$final 2"
                    }
                }
            }
        },
        # slice the first 3 students in each group
        {
            "$project": {
                "students": {
                    "$slice": ["$students", 3]
                }
            }
        }
    ]

    results = my_col.aggregate(pipeline)

    print("Aggregate Complete!")

    print("Results:")
    for section in results:
        print(section)


if __name__ == "__main__":
    main()
