public class App {
    /* Problem:
     * Given a list of numbers and a number k, return whether any two of numbers
     * add from the list add up to k.
     * 
     * Example: given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17
     */

    public static void main(String[] args) throws Exception {        
        int k = Integer.parseInt(args[0]);
        int[] numbers = {10, 15, 3, 7};
        boolean additionFound = false;
        
        for (int i : numbers) {
            for (int j : numbers) {
                if (i + j == k) {
                    System.out.println(i + " and " + j + " equal " + k);
                    additionFound = true;
                    return;
                }
            }
        }

        // Added fail case handling in case no numbers add up
        if (!additionFound) {
            System.out.println(k + " cannot be made from the list of numbers");
        }
    }
}
