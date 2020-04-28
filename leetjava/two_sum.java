class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // should return indecies that add up to the target  
        // using HashMap
        // declare Hashmap
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        // declare the answer
        int[] result = new int[2];
        // then loop through the numbers and add them to the result
        for(int i = 0; i < numbers.length; i++){
            // map all the numbers in two sets of results
            if(map.containsKey(numbers[i])){
                int index = map.get(numbers[i]);
                result[0]= index + 1; 
                result[1]= i+1; 
                break;
            }else{
                map.put(target-numbers[i], i);
            }
        }
        return result;
    }
}