#include <stdio.h>
#include <stdlib.h>
//malloc = memory allocation

int main(){
  int j;
  int i = 0;
  int input,len_tmp;
  // make a pointer and allocate memory
  int *arr, *tmp;
  int len = 10;

  // allocate enough memory for an array of length 10 for int types
  arr = (int*)malloc(len*sizeof(int));

  // checks at the end (do it only after we get input from user)
  do{
    scanf("%d",&input);
    arr[i++] = input;

    if (i ==len){
    // Check if we're near our len limit
    // If so, make temp array and save
      len_tmp = len;
      tmp = (int*)malloc(len_tmp*sizeof(int));
      for(j=0; j < len_tmp; j++){
        tmp[j] = arr[j];

    }

    // Reallocate memory in main array
    // And copy temp back into main
    len*=2;
    arr = (int*)realloc(arr,len*sizeof(int));

    for(j=0; j < len_tmp; j++){
      arr[j] = tmp[j];
    }
    free(tmp);

    //Free temp array

  }



  } while(input != -1);
  len = i -1;


  printf("\nArray: ");
  for(i=0; i < len -1; i++){
    printf("%d, ", arr[i]);
  }
  printf("%d\n\n", arr[i]);

  //Free memory
  free(arr);


  //scanf reads userinput
  // scanf("%d",&input);
  // printf("\n\nYou entered: %d \n \n",input);

  return 0;
}
/*
// int *arr;
int i;
int arr2[5];
arr2[0] = 3;
arr2[1] = 33;
arr2[2] = 1;
arr2[3] = 73;
arr2[4] = 4;

printf("\nArray: ");
for (i = 0; i <4; i++){
  printf("%d, ",arr2[i]);
}

printf("%d\n",arr2[i]);

*/
