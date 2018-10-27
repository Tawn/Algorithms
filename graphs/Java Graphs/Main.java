package graphs;

public class Main {
	
	public static void main(String[] args) {
		Directed_Graph graph = new Directed_Graph();
		graph.addVertex("A");
		graph.addVertex("B");
		graph.addVertex("C");
		graph.addVertex("D");
		
		graph.addEdge("A", "B");
		graph.addEdge("A", "C");
		graph.addEdge("B", "D");
		
		graph.printAdj("A");
		graph.printAdj("B");

	}

}
