
const list = $('.my_list');
const addItem = $('#add_item');

addItem.click(function () {
  list.append('<li>Item</li>');
});
