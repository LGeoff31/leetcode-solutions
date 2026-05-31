class Solution {
    public boolean asteroidsDestroyed(long mass, int[] asteroids) {
        Arrays.sort(asteroids);
        for (int i = 0; i < asteroids.length; i++) {
            if (asteroids[i] > mass) return false;
            mass = mass + asteroids[i];
        }
        return true;
    }
}