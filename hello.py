from flask import Flask, request, redirect, url_for
app = Flask(__name__)

tasks = []

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/', methods = ['GET', 'POST'])
def task1():
    # POST
    if request.method == 'POST':
      category = request.form['category']
      tasks.append({'category':category})
      return redirect('/')    # 
      #return redirect(url_for('task1'))  # name of method instead of aboe

    # GET
    resp = """
    <form action="" method=post>
      <p>Category: <input type=text name=category></p>
      <p><input type=submit value=Add></p>
    </form>"""

    # Show the Table
    resp = resp + """
    <table border="1" cellpadding="3">
      <tbody>
        <tr>
          <th>Category</th>
        <tr/>
      """
    for task in tasks:
      resp = resp + "<tr><td>%s<td/></tr>" % (task['category'])
    resp = resp + '</tbody></table>'
    return resp

@app.route('/second/<name>')
def hello_2(name = "bla"):
    return 'Hello, %s!' % name

if __name__ == '__main__':
  app.debug = True
  app.run()