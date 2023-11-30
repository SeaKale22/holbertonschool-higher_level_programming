#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

function tasksCompleted (err, response, body) {
  if (err) {
    // do nothing
  }
  const completedTasks = {};
  const tasks = JSON.parse(body);
  for (const task of tasks) {
    if (task.completed) {
      if (!completedTasks[task.userId]) {
        completedTasks[task.userId] = 0;
      }
      completedTasks[task.userId] = completedTasks[task.userId] + 1;
    }
  }
  console.log(completedTasks);
}

request(apiUrl, tasksCompleted);
