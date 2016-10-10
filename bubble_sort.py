from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def randList():
  import random, datetime

  startTime = datetime.datetime.now()
  sample_list = []
  for count in range (0, 101):
    sample_list.append(random.randrange(0, 10001))

  sample_list.sort()
  endTime = datetime.datetime.now()
  speed = endTime - startTime
  speed = speed.microseconds
  return render_template("index.html", sample_list = sample_list, startTime = startTime, endTime = endTime, speed = speed)

app.run(debug=True) # run our server