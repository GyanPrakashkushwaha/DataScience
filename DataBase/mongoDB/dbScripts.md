<!DOCTYPE html>
<html>
<head>
  <title>MongoDB Shell Commands</title>
</head>
<body>
  <h1>Connect MongoDB Shell</h1>
  <pre>
    mongo # connects to mongodb://127.0.0.1:27017 by default
    mongo --host &lt;host&gt; --port &lt;port&gt; -u &lt;user&gt; -p &lt;pwd&gt; # omit the password if you want a prompt
    mongo "mongodb://192.168.1.1:27017"
    mongo "mongodb+srv://cluster-name.abcde.mongodb.net/&lt;dbname&gt;" --username &lt;username&gt; # MongoDB Atlas
  </pre>

  <h1>Show Databases</h1>
  <pre>
    show dbs
    db // prints the current database
  </pre>

  <h1>Switch Database</h1>
  <pre>
    use &lt;database_name&gt;
  </pre>

  <h1>Show Collections</h1>
  <pre>
    show collections
  </pre>

  <h1>Run JavaScript File</h1>
  <pre>
    load("myScript.js")
  </pre>

  <h1>CRUD</h1>

  <h2>Create</h2>
  <pre>
    db.coll.insertOne({name: "Max"})
    db.coll.insert([{name: "Max"}, {name:"Alex"}]) // ordered bulk insert
    db.coll.insert([{name: "Max"}, {name:"Alex"}], {ordered: false}) // unordered bulk insert
    db.coll.insert({date: ISODate()})
    db.coll.insert({name: "Max"}, {"writeConcern": {"w": "majority", "wtimeout": 5000}})
  </pre>

  <h2>Read</h2>
  <pre>
    db.coll.findOne() // returns a single document
    db.coll.find()    // returns a cursor - show 20 results - "it" to display more
    db.coll.find().pretty()
    db.coll.find({name: "Max", age: 32}) // implicit logical "AND".
    db.coll.find({date: ISODate("2020-09-25T13:57:17.180Z")})
    db.coll.find({name: "Max", age: 32}).explain("executionStats") // or "queryPlanner" or "allPlansExecution"
    db.coll.distinct("name")
    // Count
    db.coll.count({age: 32})          // estimation based on collection metadata
    db.coll.estimatedDocumentCount()  // estimation based on collection metadata
    db.coll.countDocuments({age: 32}) // alias for an aggregation pipeline - accurate count
    // Comparison
    db.coll.find({"year": {$gt: 1970}})
    db.coll.find({"year": {$gte: 1970}})
    db.coll.find({"year": {$lt: 1970}})
    db.coll.find({"year": {$lte: 1970}})
    db.coll.find({"year": {$ne: 1970}})
    db.coll.find({"year": {$in: [1958, 1959]}})
    db.coll.find({"year": {$nin: [1958, 1959]}})
    // Logical
    db.coll.find({name:{$not: {$eq: "Max"}}})
    db.coll.find({$or: [{"year" : 1958}, {"year" : 1959}]})
    db.coll.find({$nor: [{price: 1.99}, {sale: true}]})
    db.coll.find({
      $and: [
        {$or: [{qty: {$lt :10}}, {qty :{$gt: 50}}]},
        {$or: [{sale: true}, {price: {$lt: 5 }}]}
      ]
    })
    // Element
    db.coll.find({name: {$exists: true}})
    db.coll.find({"zipCode": {$type: 2 }})
    db.coll.find({"zipCode": {$type: "string"}})
    // Aggregation Pipeline
    db.coll.aggregate([
      {$match: {status: "A"}},
      {$group: {_id: "$cust_id", total: {$sum: "$amount"}}},
      {$sort: {total: -1}}
    ])
    // Text search with a "text" index
    db.coll.find({$text: {$search: "cake"}}, {score: {$meta: "textScore"}}).sort({score: {$meta: "textScore"}})
    // Regex
    db.coll.find({name: /^Max/})   // regex: starts by letter "M"
    db.coll.find({name: /^Max$/i}) // regex case insensitive
    // Array
    db.coll.find({tags: {$all: ["Realm", "Charts"]}})
    db.coll.find({field: {$size: 2}}) // impossible to index - prefer storing the size of the array & update it
    db.coll.find({results: {$elemMatch: {product: "xyz", score: {$gte: 8}}}})
    // Projections
    db.coll.find({"x": 1}, {"actors": 1})               // actors + _id
    db.coll.find({"x": 1}, {"actors": 1, "_id": 0})     // actors
    db.coll.find({"x": 1}, {"actors": 0, "summary": 0}) // all but "actors" and "summary"
    // Sort, skip, limit
    db.coll.find({}).sort({"year": 1, "rating": -1}).skip(10).limit(3)
    // Read Concern
    db.coll.find().readConcern("majority")
  </pre>

  <h2>Update</h2>
  <pre>
    db.coll.update({"_id": 1}, {"year": 2016}) // WARNING! Replaces the entire document
    db.coll.update({"_id": 1}, {$set: {"year": 2016, name: "Max"}})
    // Add more update operations here
  </pre>

  <h2>Delete</h2>
  <pre>
    db.coll.remove({name: "Max"})
    // Add more delete operations here
  </pre>

  <h2>Databases and Collections</h2>
  <pre>
    db.coll.drop()    // removes the collection and its index definitions
    db.dropDatabase() // double check that you are *NOT* on the PROD cluster... :-)
    // Add more database and collection operations here
  </pre>
</body>
</html>
