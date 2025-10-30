class Solution {
    public List<String> summaryRanges(int[] nums) {
        if (nums == null){
            return null;
        }
        if (nums.length == 0){
            ArrayList<String> strList = new ArrayList<>();
            return strList;
        }

        ArrayList<String> strList = new ArrayList<>();
        int start = 0;
        int end = 1;
        for (;end < nums.length; end++){
            if (nums[end] - nums[end-1] == 1){
                continue;
            }
            else if (end - start > 1){
                String str = "" + nums[start] + "->" + nums[end-1];
                strList.add(str);
                start = end;
            }
            else{
                String str = "" + nums[start];
                strList.add(str);
                start = end;
            }
        }
    
        if (end - start > 1){
            String str = "" + nums[start] + "->" + nums[end-1];
            strList.add(str);
            
        }
        else{
            String str = "" + nums[start];
            strList.add(str);
            
        }
        return strList;
    }
}
