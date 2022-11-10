package main

import (
	"context"
	"fmt"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

func main() {
	col, err := get_db_col()
	if err != nil {
		panic(err)
	}

	// get the fields we want
	project_stage := bson.D{
		{Key: "$project", Value: bson.D{
			{Key: "name", Value: 1},
			{Key: "average", Value: bson.D{
				{Key: "$avg", Value: bson.A{"$midterm 1", "$midterm 2", "$final 1", "$final 2"}},
			}},
		}},
	}

	// sort by average
	sort_stage := bson.D{
		{Key: "$sort", Value: bson.D{
			{Key: "average", Value: -1},
		}},
	}

	// limit to 3
	limit_stage := bson.D{
		{Key: "$limit", Value: 3},
	}

	// get the top 3 students
	cursor, err := col.Aggregate(context.Background(), mongo.Pipeline{project_stage, sort_stage, limit_stage})
	if err != nil {
		panic(err)
	}

	// print the results
	for cursor.Next(context.Background()) {
		var result bson.M
		err := cursor.Decode(&result)
		if err != nil {
			panic(err)
		}
		fmt.Println(result)
	}
}

// connect to students collection
func get_db_col() (*mongo.Collection, error) {
	var col *mongo.Collection

	uri := "mongodb://localhost:27017/"

	client, err := mongo.NewClient(options.Client().ApplyURI(uri))
	if err != nil {
		return col, err
	}

	err = client.Connect(context.Background())
	if err != nil {
		return col, err
	}

	db := client.Database("mongodb-aggregate-example")
	col = db.Collection("students")

	return col, nil
}
