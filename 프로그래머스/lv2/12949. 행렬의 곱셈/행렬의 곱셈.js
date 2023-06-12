function solution(arr1, arr2){
  var answer = []
  var sum = 0
  var temp = []
  for(var i=0; i<arr1.length; i++){
    for(var k=0; k<arr2[0].length; k++){
      for(var j=0; j<arr2.length; j++){
        sum = sum + arr1[i][j] * arr2[j][k]
      }
      temp.push(sum)
      sum = 0
    }
    answer.push(temp)
    temp = []
  }
  return answer
}