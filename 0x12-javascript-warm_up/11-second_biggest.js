#!/usr/bin/node
let args = process.argv.slice(2);
if (args.length === 0) {
  console.log('0');
} else if (args.length === 1) {
  console.log('1');
} else {
  let largest = args[0];
  let nextLargest = 0;
  for (let j = 0; j < args.length; j++) {
    if (args[j] > largest) {
      nextLargest = largest;
      largest = args[j];
    }
  }
  console.log(nextLargest);
}
