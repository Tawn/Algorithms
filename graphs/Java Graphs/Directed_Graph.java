package graphs;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;


public class Directed_Graph {
	
	private Map<String, LinkedList<String>> graph;
	
	public Directed_Graph() {
		graph = new HashMap<>();
	}
	
	public void addVertex(String label) {
		if (graph.containsKey(label)) 
			System.out.println("Vertex Exist");
		else
			graph.put(label, new LinkedList<String>());
		
	}
	
	public void addEdge(String v1, String v2) {
		if (graph.get(v1).contains(v2)) 
			System.out.println("Edge already exists from " + v1 + " to " + v1);
		else if (!(graph.containsKey(v1) && graph.containsKey(v2)))
				System.out.println("Vertices doesn't exist");
		else
			graph.get(v1).add(v2);
	}
	
	public void printAdj(String vertex) {
		System.out.println("Vertex " + vertex + " -> " + graph.get(vertex));
		
	}

}
