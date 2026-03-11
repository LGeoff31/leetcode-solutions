class Solution {
    double radius;
    double x_center;
    double y_center;

    bool valid(double x, double y) {
        return pow(x - x_center, 2) + pow(y - y_center, 2) <= pow(radius, 2);
    }

public:
    Solution(double radius, double x_center, double y_center) : radius(radius), x_center(x_center), y_center(y_center) {
        srand(time(0));
    }
    
    vector<double> randPoint() {
        double x=-1e9, y=-1e9;
        while (!valid(x, y)) {
            x = x_center + (((double)rand()) / RAND_MAX - 0.5) * 2 * radius;
            y = y_center + (((double)rand()) / RAND_MAX - 0.5) * 2 * radius;
        }
        return {x, y};
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj->randPoint();
 */