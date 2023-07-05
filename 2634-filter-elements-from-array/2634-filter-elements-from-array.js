/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let n = arr.length;
    let temp = 0;
    let nums = [];
    for(var i = 0; i < n; i++){
        if(fn(arr[i], i)){
            nums[temp++] = arr[i];
        }
    }
    return nums;
};