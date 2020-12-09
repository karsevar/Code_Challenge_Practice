var removeNthFromEnd = function (head, n) {
  // create two pointers both initialized to the head node
  // first loop through the linked list to the nth node using
  fast_node = head;
  slow_node = head;
  past_node = null;

  for (let i = 0; n > i; i++) {
    fast_node = fast_node.next;
  }

  while (fast_node !== null) {
    past_node = slow_node;
    slow_node = slow_node.next;
    fast_node = fast_node.next;
  }

  if (past_node === null && slow_node === null) {
    return null;
  } else if (past_node === null && slow_node !== null) {
    return slow_node.next;
  }
  if (slow_node.next !== null) {
    past_node.next = slow_node.next;
  } else {
    past_node.next = null;
  }

  return head;
};
