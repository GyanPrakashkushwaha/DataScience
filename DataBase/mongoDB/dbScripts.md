<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <h1>🌟 Connect to MongoDB Shell</h1>
  <pre><h2>
    <!-- 🚀 Connect to the default MongoDB instance -->
    🚀 mongo
    
    <!-- 🚀 Connect to a specific host and port with credentials -->
    🚀 mongo --host &lt;host&gt; --port &lt;port&gt; -u &lt;user&gt; -p &lt;pwd&gt;
    
    <!-- 🚀 Connect to a remote MongoDB server -->
    🚀 mongo "mongodb://192.168.1.1:27017"
    
    <!-- 🚀 Connect to MongoDB Atlas -->
    🚀 mongo "mongodb+srv://cluster-name.abcde.mongodb.net/&lt;dbname&gt;" --username &lt;username&gt;
  <h2></pre>

  <h1>📚 Show Databases</h1>
  <pre><h2>
    <!-- 🎯 Show all available databases -->
    🎯 show dbs
    
    <!-- 🎯 Print the current database -->
    🎯 db
  <h2></pre>

  <h1>🔄 Switch Database</h1>
  <pre><h2>
    <!-- 🔄 Change to a specific database -->
    🔄 use &lt;database_name&gt;
  <h2></pre>

  <h1>🗃️ Show Collections</h1>
  <pre><h2>
    <!-- 📋 Show all collections in the current database -->
    📋 show collections
  <h2></pre>

  <h1>🚀 Run JavaScript File</h1>
  <pre><h2>
    <!-- 📜 Load and execute a JavaScript file -->
    📜 load("myScript.js")
  <h2></pre>

  <h1>📝 CRUD Operations</h1>

  <h2>🌱 Create</h2>
  <pre><h2>
    <!-- 🌱 Insert a single document into the collection -->
    🌱 db.coll.insertOne({name: "Max"})
    
    <!-- 🌱 Insert multiple documents into the collection (ordered) -->
    🌱 db.coll.insert([{name: "Max"}, {name:"Alex"}])
    
    <!-- 🌱 Insert multiple documents into the collection (unordered) -->
    🌱 db.coll.insert([{name: "Max"}, {name:"Alex"}], {ordered: false})
    
    <!-- 🌱 Insert a document with a date field -->
    🌱 db.coll.insert({date: ISODate()})
    
    <!-- 🌱 Insert with a custom write concern -->
    🌱 db.coll.insert({name: "Max"}, {"writeConcern": {"w": "majority", "wtimeout": 5000}})
  <h2></pre>

  <h2>📖 Read</h2>
  <pre><h2>
    📖 db.coll.find().pretty() <!-- Find documents and pretty-print the results -->
    📖 db.coll.find({name: "Max", age: 32}) <!-- Find documents with multiple conditions (implicit logical "AND") -->
    📖 db.coll.find({date: ISODate("2020-09-25T13:57:17.180Z")}) <!-- Find documents with a specific date -->
    📖 db.coll.find({name: "Max", age: 32}).explain("executionStats") <!-- Explain query execution statistics -->
    📖 db.coll.distinct("name") <!-- Get distinct values for a field -->
    📖 db.coll.count({age: 32}) <!-- Count documents matching a condition (estimation) -->
    📖 db.coll.countDocuments({age: 32}) <!-- Count documents using aggregation pipeline (accurate count) -->
    
    <!-- 📖 Comparison operators -->
    📖 db.coll.find({"year": {$gt: 1970}}) <!-- Greater than -->
    📖 db.coll.find({"year": {$gte: 1970}}) <!-- Greater than or equal to -->
    📖 db.coll.find({"year": {$lt: 1970}}) <!-- Less than -->
    📖 db.coll.find({"year": {$lte: 1970}}) <!-- Less than or equal to -->
    📖 db.coll.find({"year": {$ne: 1970}}) <!-- Not equal to -->
    📖 db.coll.find({"year": {$in: [1958, 1959]}}) <!-- In an array of values -->
    📖 db.coll.find({"year": {$nin: [1958, 1959]}}) <!-- Not in an array of values -->
    
    <!-- 📖 Logical operators -->
    📖 db.coll.find({name:{$not: {$eq: "Max"}}}) <!-- Negation -->
    📖 db.coll.find({$or: [{"year" : 1958}, {"year" : 1959}]}) <!-- Logical OR -->
    📖 db.coll.find({$nor: [{price: 1.99}, {sale: true}]}) <!-- Logical NOR -->
    📖 db.coll.find({
      $and: [
        {$or: [{qty: {$lt :10}}, {qty :{$gt: 50}}]},
        {$or: [{sale: true}, {price: {$lt: 5 }}]}
      ]
    }) <!-- Logical AND -->
    
    <!-- 📖 Element operators -->
    📖 db.coll.find({name: {$exists: true}}) <!-- Field exists -->
    📖 db.coll.find({"zipCode": {$type: 2 }}) <!-- Field type -->
    📖 db.coll.find({"zipCode": {$type: "string"}}) <!-- Field type with string value -->
    
    <!-- 📖 Aggregation Pipeline -->
    📖 db.coll.aggregate([
      {$match: {status: "A"}},
      {$group: {_id: "$cust_id", total: {$sum: "$amount"}}},
      {$sort: {total: -1}}
    ])
    
    <!-- 📖 Text search with a "text" index -->
    📖 db.coll.find({$text: {$search: "cake"}}, {score: {$meta: "textScore"}}).sort({score: {$meta: "textScore"}})
    
    <!-- 📖 Regular expressions -->
    📖 db.coll.find({name: /^Max/})   <!-- regex: starts by letter "M" -->
    📖 db.coll.find({name: /^Max$/i}) <!-- regex case insensitive -->
    
    <!-- 📖 Array operators -->
    📖 db.coll.find({tags: {$all: ["Realm", "Charts"]}}) <!-- All elements match an array -->
    📖 db.coll.find({field: {$size: 2}}) <!-- Field is an array with size 2 -->
    📖 db.coll.find({results: {$elemMatch: {product: "xyz", score: {$gte: 8}}}}) <!-- Match elements in an array with conditions -->
    
    <!-- 📖 Projections -->
    📖 db.coll.find({"x": 1}, {"actors": 1})               <!-- Include "actors" and "_id" -->
    📖 db.coll.find({"x": 1}, {"actors": 1, "_id": 0})     <!-- Include "actors" only -->
    📖 db.coll.find({"x": 1}, {"actors": 0, "summary": 0}) <!-- Exclude "actors" and "summary" -->
    
    <!-- 📖 Sort, skip, limit -->
    📖 db.coll.find({}).sort({"year": 1, "rating": -1}).skip(10).limit(3)
    
    <!-- 📖 Read Concern -->
    📖 db.coll.find().readConcern("majority")
  <h2></pre>

  <h2>🔄 Update</h2>
  <pre><h2>
    <!-- 🔄 WARNING! Replaces the entire document -->
    🔄 db.coll.update({"_id": 1}, {"year": 2016})
    
    <!-- 🔄 Update specific fields using $set -->
    🔄 db.coll.update({"_id": 1}, {$set: {"year": 2016, name: "Max"}})
    
    <!-- 🔄 Remove a field using $unset -->
    🔄 db.coll.update({"_id": 1}, {$unset: {"year": 1}})
    
    <!-- 🔄 Rename a field using $rename -->
    🔄 db.coll.update({"_id": 1}, {$rename: {"year": "date"}})
    
    <!-- 🔄 Increment a numeric field using $inc -->
    🔄 db.coll.update({"_id": 1}, {$inc: {"year": 5}})
    
    <!-- 🔄 Multiply numeric fields using $mul -->
    🔄 db.coll.update({"_id": 1}, {$mul: {price: NumberDecimal("1.25"), qty: 2}})
    
    <!-- 🔄 Set a minimum value for a field using $min -->
    🔄 db.coll.update({"_id": 1}, {$min: {"imdb": 5}})
    
    <!-- 🔄 Set a maximum value for a field using $max -->
    🔄 db.coll.update({"_id": 1}, {$max: {"imdb": 8}})
    
    <!-- 🔄 Set a field to the current date using $currentDate -->
    🔄 db.coll.update({"_id": 1}, {$currentDate: {"lastModified": true}})
    
    <!-- 🔄 Set a field to the current date with a specific type using $currentDate -->
    🔄 db.coll.update({"_id": 1}, {$currentDate: {"lastModified": {$type: "timestamp"}}})
    
    <!-- 🔄 Update an array field using $push -->
    🔄 db.coll.update({"_id": 1}, {$push :{"array": 1}})
    
    <!-- 🔄 Remove an element from an array using $pull -->
    🔄 db.coll.update({"_id": 1}, {$pull :{"array": 1}})
    
    <!-- 🔄 Add an element to an array using $addToSet -->
    🔄 db.coll.update({"_id": 1}, {$addToSet :{"array": 2}})
    
    <!-- 🔄 Remove the first or last element from an array using $pop -->
    🔄 db.coll.update({"_id": 1}, {$pop: {"array": 1}})  <!-- last element -->
    🔄 db.coll.update({"_id": 1}, {$pop: {"array": -1}}) <!-- first element -->
    
    <!-- 🔄 Remove multiple elements from an array using $pullAll -->
    🔄 db.coll.update({"_id": 1}, {$pullAll: {"array" :[3, 4, 5]}})
    
    <!-- 🔄 Add multiple elements to an array using $push with $each -->
    🔄 db.coll.update({"_id": 1}, {$push: {scores: {$each: [90, 92, 85]}}})
    
    <!-- 🔄 Update specific element in an array using the positional operator $ -->
    🔄 db.coll.updateOne({"_id": 1, "grades": 80}, {$set: {"grades.$": 82}})
    
    <!-- 🔄 Update all elements in an array using the $[] operator -->
    🔄 db.coll.updateMany({}, {$inc: {"grades.$[]": 10}})
    
    <!-- 🔄 Update specific elements in an array using arrayFilters -->
    🔄 db.coll.update({}, {$set: {"grades.$[element]": 100}}, {multi: true, arrayFilters: [{"element": {$gte: 100}}]})
    
    <!-- 🔄 Update multiple documents matching a condition -->
    🔄 db.coll.update({"year": 1999}, {$set: {"decade": "90's"}}, {"multi":true})
    
    <!-- 🔄 Update multiple documents using updateMany -->
    🔄 db.coll.updateMany({"year": 1999}, {$set: {"decade": "90's"}})
    
    <!-- 🔄 FindOneAndUpdate with returnNewDocument -->
    🔄 db.coll.findOneAndUpdate({"name": "Max"}, {$inc: {"points": 5}}, {returnNewDocument: true})
    
    <!-- 🔄 Upsert - Insert or update if document exists -->
    🔄 db.coll.update({"_id": 1}, {$set: {item: "apple"}, $setOnInsert: {defaultQty: 100}}, {upsert: true})
    
    <!-- 🔄 Replace a document completely -->
    🔄 db.coll.replaceOne({"name": "Max"}, {"firstname": "Maxime", "surname": "Beugnet"})
    
    <!-- 🔄 Save a document - insert or update if _id exists -->
    🔄 db.coll.save({"item": "book", "qty": 40})
    
    <!-- 🔄 Write concern for update operations -->
    🔄 db.coll.update({}, {$set: {"x": 1}}, {"writeConcern": {"w": "majority", "wtimeout": 5000}})
  <h2></pre>

  <h2>🗑️ Delete</h2>
  <pre><h2>
    <!-- 🗑️ Remove documents matching a condition -->
    🗑️ db.coll.remove({name: "Max"})
    
    <!-- 🗑️ WARNING! Deletes all documents in the collection -->
    🗑️ db.coll.remove({})
    
    <!-- 🗑️ Remove documents with write concern -->
    🗑️ db.coll.remove({name: "Max"}, {"writeConcern": {"w": "majority", "wtimeout": 5000}})
    
    <!-- 🗑️ FindOneAndDelete - Find and delete a single document -->
    🗑️ db.coll.findOneAndDelete({"name": "Max"})
  <h2></pre>

  <h2>🧹 Databases and Collections</h2>
  <pre><h2>
    <!-- 🧹 Remove the collection and its index definitions -->
    🧹 db.coll.drop()
    
    <!-- 🧹 WARNING! Remove the entire database -->
    🧹 db.dropDatabase()
  <h2></pre>
</body>
</html>
