#include <stdio.h>
#include <malloc.h>

void print_array(int *nums, int len){
    int i = 0;

    printf("\nPrinting Array: ");
    for(; i < len - 1; i++){
        printf("%d, ", nums[i]);
    }
    printf("%d\n", nums[i]);
}


int main(){
    // Declare variables
    int *nums, *held;
    int i, len, input;

    // Define our variables
    len = 10;

    // Allocate memory for our array
    nums = (int*)malloc(sizeof(int) * len);

    // Get user input until -1
    do{
        scanf("%d", &input);
        nums[i++] = input;
    } while(input != -1);
    len = i - 1;
    nums[len] = '\0';

    // Print the array
    print_array(nums, len);

    // Free memory
    free(nums);

    return 0;
}
