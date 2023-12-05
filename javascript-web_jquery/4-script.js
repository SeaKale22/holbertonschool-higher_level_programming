#!/usr/bin/node

const header = $('header');
const toggleDiv = $('#toggle_header');

toggleDiv.click(function () {
  if (header.hasClass('green')) {
    header.attr('class', 'red');
  } else {
    header.attr('class', 'green');
  }
});
