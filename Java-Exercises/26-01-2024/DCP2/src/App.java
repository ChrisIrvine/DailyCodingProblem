import java.util.Arrays;

/** Exercise:
 *
 * Given an array of integers, return a new array such that each element
 * at index i of the new array is the product of all the numbers in the original
 * array except the one at i. 
 * 
 * For example, if our input was [1, 2, 3, 4, 5], the expected output 
 * would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected
 * output would be [2, 3, 6].
 * 
 * Going straight to refined answer after figuring it out during python exercise.
 */

public class App {
    public static void main(String[] args) throws Exception {
        int[] inputArray = {1, 2, 3, 4, 5};
        int[] outputArray = new int[inputArray.length];
        int prefix = 1;
        int suffix = 1;

        for (int i = 0; i < inputArray.length; i++) {
            outputArray[i] = prefix;
            prefix = prefix * inputArray[i];
        }

        for (int i = inputArray.length-1; i >= 0; i--){
            outputArray[i] = suffix * outputArray[i];
            suffix = suffix * inputArray[i];
        }

        System.out.println(Arrays.toString(outputArray));
    }
}
