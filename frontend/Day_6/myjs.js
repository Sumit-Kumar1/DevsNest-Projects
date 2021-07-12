// Q:1Write a JavaScript function to check whether an `input` is an array or not
// Test Data :
// console.log(is_array('w3resource'));
// console.log(is_array([1, 2, 4, 0]));
// false
// True
function check_array(arr){
    let type = typeof arr;
    if( type != 'object')
        return false;
    else
        return true;
}

let arr = 'w3Resources';
console.log('"w3Resource" is arr ?: '+check_array(arr));
arr = [1,2,3,4];
console.log('[1,2,3,4] is an array?: '+ check_array(arr));
//Write a JavaScript function to get the first element of an array. Passing a parameter 'n' will return the first 'n' elements of the array.
function first(arr, n){
    let count = 0;
    for (const key in arr) {
        if(count >= n){
            console.log(" ");
        }else{
            console.log(arr[key]+' ');
        }
    }
}
console.log("First 3 numbers of [1,2,3,4]: ");
first(arr, 3);
console.log("First 5 numbers of [1,2,3,4,]: ");
first(arr ,5);

//Write a JavaScript program to find the most frequent item of an array
