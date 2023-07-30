<!DOCTYPE html>
<html>
<head>
<style>
  body {
    font-size: 18px;
    line-height: 1.6;
  }
  pre {
    font-size: 20px;
    background-color: #f5f5f5;
    padding: 10px;
    border-radius: 5px;
    overflow-x: auto;
  }
  h1, h2 {
    color: #007bff;
    margin-bottom: 5px;
  }
  h2 {
    color: #28a745;
    font-size: 24px;
  }
  h1::after, h2::after {
    content: " ⭐";
  }
</style>
</head>
<body>
  <h1>🌟 Connect to MongoDB Shell</h1>
  <pre>
    <!-- 🚀 Connect to the default MongoDB instance -->
    🚀 mongo
    
    <!-- 🚀 Connect to a specific host and port with credentials -->
    🚀 mongo --host &lt;host&gt; --port &lt;port&gt; -u &lt;user&gt; -p &lt;pwd&gt;
    
    <!-- 🚀 Connect to a remote MongoDB server -->
    🚀 mongo "mongodb://192.168.1.1:27017"
    
    <!-- 🚀 Connect to MongoDB Atlas -->
    🚀 mongo "mongodb+srv://cluster-name.abcde.mongodb.net/&lt;dbname&gt;" --username &lt;username&gt;
  </pre>

  <h1>📚 Show Databases</h1>
  <pre>
    <!-- 🎯 Show all available databases -->
    🎯 show dbs
    
    <!-- 🎯 Print the current database -->
    🎯 db
  </pre>

  <h1>🔄 Switch Database</h1>
  <pre>
    <!-- 🔄 Change to a specific database -->
    🔄 use &lt;database_name&gt;
  </pre>

  <h1>🗃️ Show Collections</h1>
  <pre>
    <!-- 📋 Show all collections in the current database -->
    📋 show collections
  </pre>

  <h1>🚀 Run JavaScript File</h1>
  <pre>
    <!-- 📜 Load and execute a JavaScript file -->
    📜 load("myScript.js")
  </pre>

  <h1>📝 CRUD Operations</h1>

  <h2>🌱 Create</h2>
  <pre>
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
  </pre>

  <h2>📖 Read</h2>
  <pre>
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
