from graphviz import Digraph

# Создание графа
state_graph = Digraph("StateGraph", format="png")

# Определение узлов
state_graph.node("OPENED", shape="circle", style="filled", color="lightblue", label="OPENED")
state_graph.node("IN PROGRESS", shape="circle", style="filled", color="lightblue", label="IN PROGRESS")
state_graph.node("READY TO TEST", shape="circle", style="filled", color="lightblue", label="READY TO TEST")
state_graph.node("NOT ACCEPTED", shape="circle", style="filled", color="lightblue", label="NOT ACCEPTED")
state_graph.node("ACCEPTED", shape="doublecircle", style="filled", color="lightgreen", label="ACCEPTED")

# Определение связей
state_graph.edge("OPENED", "IN PROGRESS")
state_graph.edge("IN PROGRESS", "READY TO TEST")
state_graph.edge("READY TO TEST", "ACCEPTED")
state_graph.edge("READY TO TEST", "NOT ACCEPTED")
state_graph.edge("NOT ACCEPTED", "IN PROGRESS")

# Сохранение графа в файл
state_graph.render("state_graph")
