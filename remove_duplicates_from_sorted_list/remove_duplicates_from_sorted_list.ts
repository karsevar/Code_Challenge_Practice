

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function deleteDuplicates(head: ListNode | null): ListNode | null {
    if (head === null) {
        return head
    }
    if (head.next === null) {
        return head
    }

    let currentNode: ListNode | null = head
    let nextNode: ListNode | null = head.next

    while (currentNode !== null && nextNode !== null) {
        if (currentNode.val === nextNode.val) {
            while (nextNode !== null && currentNode.val === nextNode.val) {
                nextNode = nextNode.next
            }
        }
        currentNode.next = nextNode
        if (nextNode !== null) {
            currentNode = currentNode.next
            nextNode = nextNode.next
        } else {
            break
        }
    }
    return head
};