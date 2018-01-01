#!/usr/bin/node
var args = process.argv.slice(2);
var l = args.length
if (l === 0) {
  console.log("No argument");
} else if (l === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
