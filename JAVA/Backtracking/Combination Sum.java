class Solution {

    List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        
        wrap(candidates, target, 0, new ArrayList<>());
        return result;
    }

    public List<List<Integer>> wrap(int[] candidates, int target, int start, List<Integer> path){
            if (target == 0){
                result.add(new ArrayList<>(path));
                return null;
            }
            
            for(int i = start; i < candidates.length; i++){
                int c = candidates[i];
                if (c > target) continue;
                path.add(c);
                wrap(candidates,target-c,i,path);
                path.remove(path.size() - 1);
                }
            return null;
            }
            
    }
