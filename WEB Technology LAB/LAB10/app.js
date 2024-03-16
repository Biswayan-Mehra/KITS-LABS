const http = require("http");
const fs = require("fs");
const mongoose = require("mongoose");
mongoose.connect("mongodb://127.0.0.1:27017/DataBase_1").then(() => {
  console.log("db connected");
});

const schema = new mongoose.Schema({
  name: String,
  password: String,
  age: Number,
  number: String,
  email: String,
  gender: String,
  state: String,
});
const model = mongoose.model("Users", schema);
const server = http.createServer((req, res) => {
  if (req.url == "/") {
    res.writeHead(200, { "Content-Type": "text/html" });
    const htmlContent = fs.readFileSync("form.html", "utf8");
    res.end(htmlContent);
  } else if ((req.url == "/signup") & (req.method == "POST")) {
    let rawdata = "";
    req.on("data", (data) => {
      rawdata += data;
    });
    req.on("end", () => {
      let params = new URLSearchParams(rawdata);
      res.writeHead(200, { "Content-Type": "text/html" });
      res.write("Name: " + params.get("name") + "<br>");
      res.write("Password: " + params.get("password") + "<br>");
      res.write("age: " + params.get("age") + "<br>");
      res.write("number: " + params.get("number") + "<br>");
      res.write("email: " + params.get("email") + "<br>");
      res.write("gender: " + params.get("gender") + "<br>");
      res.write("state: " + params.get("state") + "<br>");
      model.create({
        name: params.get("name"),
        password: params.get("password"),
        age: params.get("age"),
        number: params.get("number"),
        email: params.get("email"),
        gender: params.get("gender"),
        state: params.get("state"),
      });
      res.write("Data saved");
      res.end();
    });
  } else if (req.url == "/view") {
    res.writeHead(200, { "Content-Type": "text/html" });
    model.find().then((users) => {
      res.write(
        "<table border='1' cellspacing='0' style='width: 100%; text-align: center; border-collapse:colapse;'><tr style 'background-color:#f2f2f2;'><<th>Name</th><th>Password</th><th>Age</th><th>Mobile Number</th><th>Email</th><th>Gender</th><th>State</th></tr>"
      );
      users.forEach((record) => {
        res.write("<tr>");
        res.write('<td style="padding: 10px;">' + record.name + "</td>");
        res.write('<td style="padding: 10px;">' + record.password + "</td>");
        res.write('<td style="padding: 10px;">' + record.age + "</td>");
        res.write('<td style="padding: 10px;">' + record.number + "</td>");
        res.write('<td style="padding: 10px;">' + record.email + "</td>");
        res.write('<td style="padding: 10px;">' + record.gender + "</td>");
        res.write('<td style="padding: 10px;">' + record.state + "</td></tr>");
      });
      res.write("</table>");
      res.end();
    });
  }
});
server.listen(8000, () => {
  console.log("Server is running");
});
