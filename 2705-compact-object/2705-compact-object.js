/**
 * @param {Object} obj
 * @return {Object}
 */
var compactObject = function(obj) {
  if(typeof obj !== 'object' || obj === null){
    return obj;
  }  
  if(Array.isArray(obj)){
    const compactArr = []
    for(let i = 0; i < obj.length; i++){
      let val = compactObject(obj[i]);
      if(val){
          compactArr.push(val);
      }
    }  
    return compactArr;
  }   
  const compactObj = {};  
  for(let key in obj){
    const val = compactObject(obj[key]);
    if(val){
        compactObj[key] = val;
    }
  }  
  return compactObj;
};