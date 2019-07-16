package chapter06;

import java.util.*;

public class BreadthFirstSearch {
    public static void main(String[] args) {
        // init test data structure
        List<String> list_you = new LinkedList<>();
        list_you.add("claire");
        list_you.add("bob");
        list_you.add("alice");

        List<String> list_claire = new LinkedList<>();
        list_claire.add("jonny");
        list_claire.add("thom");

        List<String> list_alice = new LinkedList<>();
        list_alice.add("peggy");

        List<String> list_bob = new LinkedList<>();
        list_bob.add("peggy");
        list_bob.add("aunj");

        List<String> list_thom = new LinkedList<>();
        List<String> list_jonny = new LinkedList<>();
        List<String> list_peggy = new LinkedList<>();
        List<String> list_anuj = new LinkedList<>();

        Map<String, List<String>> graph = new HashMap<>();
        graph.put("you", list_you);
        graph.put("claire", list_claire);
        graph.put("bob", list_bob);
        graph.put("alice", list_alice);
        graph.put("jonny", list_jonny);
        graph.put("thom", list_thom);
        graph.put("peggy", list_peggy);
        graph.put("anuj", list_anuj);

        BFS(graph);
    }

    private static void BFS(Map<String, List<String>> graph) {
        Queue<String> queue = new LinkedList<>();
        queue.add("you");
        Set<String> searched = new HashSet<>();

        while (!queue.isEmpty()) {
            String person = queue.poll();
            if (!searched.contains(person)) {
                if (is_seller(person)) {
                    System.out.println("person " + person + " is a seller");
                    return;
                }

                for (String sub : graph.get(person)) {
                    queue.add(sub);
                }
                searched.add(person);
            }
        }
        System.out.println("No seller in friends list.");
    }

    private static boolean is_seller(String name) {
        return name.contains("m");
    }
}
