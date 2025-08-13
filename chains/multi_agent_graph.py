# chains/multi_agent_graph.py
# from langchain.llms import Ollama
from langchain_community.llms import Ollama
from langgraph.graph import END, StateGraph
from langchain_core.messages import HumanMessage

def planner_node(state):
    return {"step": "write a function to solve this"}

def coder_node(state):
    return {"code": f"def solve():\n    return 42"}

def build_graph():
    builder = StateGraph()
    builder.add_node("planner", planner_node)
    builder.add_node("coder", coder_node)

    builder.set_entry_point("planner")
    builder.add_edge("planner", "coder")
    builder.add_edge("coder", END)

    return builder.compile()

def run_graph(user_input):
    graph = build_graph()
    state = {"input": user_input}
    result = graph.invoke(state)
    return str(result)
