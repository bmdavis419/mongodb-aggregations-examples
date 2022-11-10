import pymongo
import random
import pandas as pd
import numpy as np


def main():
    print("Connecting to MongoDB...")

    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = my_client["mongodb-aggregate-example"]
    my_col = my_db["students"]

    print("Connected to MongoDB!")

    print("Seeding DB...")

    df = pd.DataFrame(np.random.randint(
        0, 100, size=(5000, 4)), columns=list('Test1 Test2 Test3 Test4'.split()))

    sections = ["morning", "evening", "online"]

    for index, row in df.iterrows():
        # create the student document
        student = {
            "name": "Student {}".format(index),
            "midterm 1": np.int16(row['Test1']).item(),
            "midterm 2": np.int16(row['Test2']).item(),
            "final 1": np.int16(row['Test3']).item(),
            "final 2": np.int16(row['Test4']).item(),
            "section": random.choice(sections)
        }

        my_col.insert_one(student)

    print("DB Seeded!")


if __name__ == "__main__":
    main()
