#!/usr/bin/node
let args = process.argv.slice(2);
if (args.length < 2) {
  console.log('0');
} else {
  let largest = args[0];
  let nextLargest = 0;
  for (let j = 1; j < args.length; j++) {
    if (args[j] > largest) {
      nextLargest = largest;
      largest = args[j];
    }
  }
  console.log(nextLargest);
}
