class Solution {
    public int numberOfSpecialChars(String word) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == Character.toUpperCase(word.charAt(i)) && map.containsKey(word.charAt(i))) continue;
            map.put(word.charAt(i), i);
        }
        int res = 0;
        HashSet<Character> seen = new HashSet<Character>();
        for (int i = 0; i < word.length(); i++) {
            char upper = Character.toUpperCase(word.charAt(i));
            char lower = Character.toLowerCase(word.charAt(i));

            if (map.containsKey(lower) && map.containsKey(upper) && map.get(lower) < map.get(upper)) {
                seen.add(lower);
            }
        }
        return seen.size();

    }
}