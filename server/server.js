const cookieParser = require('cookie-parser');
const express = require('express')
const bodyParser = require('body-parser');
const app = express()
const csv = require('csv-express')
const path = require('path')
const fs = require('fs')
app.use(cookieParser());
app.use(bodyParser.json()); // for parsing application/json
app.use(bodyParser.urlencoded({extended:false}))
app.use('/', express.static(path.join(__dirname, '../html_prototype/')))
app.post('/data', function(req, res) {
  // console.log(req.body['typing_task_seconds'])
  data_str = '"' + req.body['user_id'] + '"' + ',' + '"' + req.body['input_field'] + '"' + ',' + '"' + req.body['time'] + '"' + ',' + '"' + req.body['input_text'] + '"' + '\n'
  fs.appendFileSync('file.csv', data_str);
  // fs.writeFile('file.csv', data_str, function (err) {
  //   console.log(req.body);
  // });
  res.json({'status': true})
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})
