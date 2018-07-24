import os
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from schema import schema

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir,
                                                   "my_graph_ql.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',
                                                           schema=schema,
                                                           graphiql=True,))


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


if __name__=='__main__':
    app.run()

