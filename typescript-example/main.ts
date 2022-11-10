import { MongoClient } from "mongodb";

const uri = "mongodb://localhost:27017/";
const client = new MongoClient(uri);

const main = async () => {
  try {
    // get the collection
    const db = client.db("mongodb-aggregate-example");
    const col = db.collection("students");

    // create the pipeline
    const pipeline: any = [
      // get the fields we want
      {
        $project: {
          section: 1,
          "midterm 1": 1,
          "midterm 2": 1,
        },
      },
      // group each section and average the sum of the midterm grades
      {
        $group: {
          _id: "$section",
          average: {
            $avg: {
              $avg: ["$midterm 1", "$midterm 2"],
            },
          },
        },
      },
      // sort by the average
      {
        $sort: {
          average: -1,
        },
      },
    ];

    // run the pipeline
    const result = await col.aggregate(pipeline).toArray();

    // print the result
    console.log(result);
  } finally {
    await client.close();
  }
};

main().catch(console.error);
