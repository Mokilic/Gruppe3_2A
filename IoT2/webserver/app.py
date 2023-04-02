from flask import Flask, render_template
import sqlite3

import time
app = Flask(__name__)



def getData():
    conn = sqlite3.connect('../Gruppe3.db')
    curs = conn.cursor()

    for row in curs.execute("SELECT * FROM IoT2 ORDER BY id DESC LIMIT 1"):
        år_måned_dag = str(row[1])
        timer_minutter = str(row[2])
        percentage = row[3]
    conn.close()
    return år_måned_dag, timer_minutter, percentage

    
@app.route('/')
def index():
  år_måned_dag, timer_minutter, percentage = getData()
  templateData = {
    'år_måned_dag': år_måned_dag,
    'timer_minutter': timer_minutter,
    'percentage': percentage
  }
  return render_template('index.html', **templateData)

if __name__ == '__main__':
  app.run(debug=True)
