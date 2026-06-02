class Solution {
    public int earliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < landStartTime.length; i++) {
            for (int j = 0; j < waterStartTime.length; j++) {
                if (landStartTime[i] + landDuration[i] >= waterStartTime[j]) {
                    res = Math.min(res, landStartTime[i] + landDuration[i] + waterDuration[j]);
                } else {
                    res = Math.min(res, waterStartTime[j] + waterDuration[j]);
                }
            }
        }

        for (int i = 0; i < waterStartTime.length; i++) {
            for (int j = 0; j < landStartTime.length; j++) {
                if (waterStartTime[i] + waterDuration[i] >= landStartTime[j]) {
                    res = Math.min(res, waterStartTime[i] + waterDuration[i] + landDuration[j]);
                } else {
                    res = Math.min(res, landStartTime[j] + landDuration[j]);
                }
            }
        }
        
        return res;
    }
}