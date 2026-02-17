from email import charset
from flask import Flask, render_template

app = Flask(__name__)


# Creating a simple flowchart diagram
from python_mermaid.diagram import (
    MermaidDiagram,
    Node,
    Link
)


# Family members
meg = Node("Meg")
jo = Node("Jo")
beth = Node("Beth", "", "cylindrical")
amy = Node("Amy")
robert = Node("Robert")

the_march_family = [meg, jo, beth, amy, robert]

# Create links
family_links = [
    Link(robert, meg),
    Link(robert, jo),
    Link(robert, beth),
    Link(robert, amy),
    Link(meg, beth, "dotted", "left-arrow", "arrow", "new relation")
]

chart = MermaidDiagram(
        title="Little Women",
        nodes=the_march_family,
        links=family_links
    )
print(chart)

chart2 = MermaidDiagram(
        title="New Diag",
        nodes=the_march_family,
        links=family_links
    )



@app.route('/')
def index():
    mermaid_code = chart
    return render_template('index.html', mermaid_code=mermaid_code)


@app.route('/new')
def index2():
    mermaid_code = chart2
    return render_template('index.html', mermaid_code=mermaid_code)


from python_mermaid.diagram import StateDiagram
from python_mermaid.node import StateNode
from python_mermaid.link import StateLink

sleep = StateNode("Sleep")
breakfast = StateNode("Eat breakfast")
work = StateNode("Go to work")
fun = StateNode("Have fun")
lunch = StateNode("Eat lunch")
work_again = StateNode("Work again")
visit_parents = StateNode("Visit parents")
dinner = StateNode("Eat dinner")

m = StateDiagram(
    type="statechart",
    nodes=[sleep, breakfast, work, fun, lunch, work_again, visit_parents, dinner],
    links=[
        StateLink(sleep, breakfast),
        StateLink(breakfast, work, "Working day"),
        StateLink(work, lunch, "Have time for lunch"),
        StateLink(work, work_again, "No time for lunch"),
        StateLink(work_again, dinner),
        StateLink(dinner, sleep),
        StateLink(breakfast, fun, "Weekend"),
        StateLink(fun, lunch),
        StateLink(lunch, visit_parents),
        StateLink(visit_parents, dinner),
    ],
)

m.add_start_and_end_nodes(breakfast, None)
print(m)

@app.route('/state')
def state():
    mermaid_code = m
    return render_template('index.html', mermaid_code=mermaid_code)



if __name__ == '__main__':
    app.run(debug=True)

    

