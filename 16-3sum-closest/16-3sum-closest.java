class Solution {
    public int threeSumClosest(int[] nums, int target) 
    {
    int u,f,curr_sum=0,close_sum=Integer.MAX_VALUE;
    Arrays.sort(nums);  
    for(int i=0;i<nums.length;i++)
    {
    u=i+1; f=nums.length-1;
    while(u<f)
    {
    curr_sum=nums[i]+nums[u]+nums[f];
        
    if(Math.abs(target-curr_sum)<Math.abs(target-close_sum))        
      close_sum=curr_sum;                
    
    if(curr_sum>target) 
       f--;
    else
       u++;
    }
    }
    return(close_sum);
    }
        
}