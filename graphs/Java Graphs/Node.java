package graphs;

import java.util.LinkedList;

public class Node {
	
	// This node can be used for undirected or directed graphs
	// made by a graph class of HashMap <Vertex, List adjacent vertex's> 

	private String label;
	private LinkedList<Node> adjList;
	
	public Node(String label) {
		this.label = label;
		adjList = null;
	}

	public String getLabel() {
		return label;
	}

	public void setLabel(String label) {
		this.label = label;
	}

	public LinkedList<Node> getAdjList() {
		return adjList;
	}

	public void setAdjList(LinkedList<Node> adjList) {
		this.adjList = adjList;
	}

}
