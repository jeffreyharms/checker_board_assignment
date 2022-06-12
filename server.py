from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

# @app.route('/Home')
@app.route('/')
def checker_board():
    return render_template("index.html")
    
@app.route("/number/<int:num>")
def modular_board(num):
    return render_template("eightbyx.html", num=num)

if __name__ == "__main__":
    app.run(debug=True)
# @app.route("/number/<string:num>")
# def print_number(num):
#     print("Number sent from URL:", num)
#     return f"Your number is {num}"


#         GET - read and display
# URL of the route to display all: the name of the list or dictionary that we are about to display
# Example: "/todos"
# Example: "/users 

# Function: get_all_todos()

# URL of the route to display one: the name of the list in singular that we are about to display
# followed by the id
# Example: "/todo/<int:id>"
# Example: "/user/<int:id>"

# Function: get_todo_by_id( id )

# POST - create
# URL of the route to create something new: the name of the list in singular that we are about to create
# followed by the keyword /new
# Example: "/todo/new"
# Example: "/user/new

# Function: create_todo()

# PUT - update
# URL of the route to update something already existing: the name of the list in singular that we are about 
# to update, followed by the id, followed by the keyword /update /edit
# Example: "/todo/<int:id>/update"
# Example: "/user/<int:id>/update"

# Function: update_todo_by_id( id )

# DELETE - remove
# URL of the route to delete something already existing: the name of the list in singular that we are about 
# to delete, followed by the id, followed by the keyword /delete /remove
# Example: "/todo/<int:id>/delete"
# Example: "/user/<int:id>/remove"

# Function: delete_todo_by_id( id )