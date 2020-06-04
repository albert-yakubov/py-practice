class TestFile {
	public static int[] solution(int[] inputArray) {
        if (inputArray == null || inputArray.length == 0) {
            return inputArray;
        }

        int r = 0;
        while (inputArray[r] < 0) {
            r++;
        }

        int l = r - 1;
​
        int[] arr = new int[inputArray.length];
​
        int i = 0;
        while (l >= 0 && r < arr.length) {
            int r2 = inputArray[r] * inputArray[r];
            int l2 = inputArray[l] * inputArray[l];
​
            if (r2 < l2) {
                arr[i] = r2;
                r++;
            }
            else {
                arr[i] = l2;
                l--;
            }
​
            i++;
        }
​
        while (l >= 0) {
            arr[i] = inputArray[l] * inputArray[l];
            i++;
            l--;
        }
​
        while (r < arr.length) {
            arr[i] = inputArray[r] * inputArray[r];
            i++;
            r++;
        }
​
        return arr;
    }
}