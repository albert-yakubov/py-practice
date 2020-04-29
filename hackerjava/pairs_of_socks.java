static int sockMerchant(int n, int[] ar) {
    // hashset int for colors
    Set<Integer> colors = new HashSet<>();
    // pairs
    int pairs = 0;
    for (int i = 0; i < n; i++) {
        // if there is nothing in our hashset, add the looped numbers
        if (!colors.contains(ar[i])) {
            colors.add(ar[i]);
        } else {
            // then remove the sets and append the pairs 
            pairs++;
            colors.remove(ar[i]);
        }
    }  
    return pairs;  
    }