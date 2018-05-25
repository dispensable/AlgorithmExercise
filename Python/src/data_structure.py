# -*- coding:utf-8 -*-


# 堆栈
def check_parenthese_match(parenthese_str, parenthese_left=('<', '(', '[', '{'), parenthese_right=('>', ')', ']', '}')):
    """
    检查给定的相同类型的括号字符串是否能够互相匹配
    :param parenthese_str: 给定的括号字符串，例如 '((()())))'
    :param parenthese_left: 左括号字符集合
    :param parenthese_right: 右括号集合
    :return: 是否匹配，如果错误返回错误的字符索引（如果正确，索引为-1）
    """
    stack = []
    for index, parenthe in enumerate(parenthese_str):
        if parenthe in parenthese_left:
            stack.append(parenthe)
        elif parenthe in parenthese_right:
            if len(stack) == 0:
                return False, index
            else:
                stack.pop()
    if len(stack) > 0:
        return False, index
    else:
        return True, -1


# linked list
class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self, node):
        self.head = node

    def add_node(self, node):
        last_node = self.head
        while(last_node.next is not None):
            last_node = last_node.next
        node.next = None
        last_node.next = node        
        return self
    
    def remove_node(self, node):
        # if node is head node
        if node.item == self.head.item:
            self.head = self.head.next
            return self
        
        # find this node's previous node
        current_node = self.head
        pre_node = current_node
        while(current_node.next is not None and current_node.item != node.item):
            current_node = current_node.next
            pre_node = current_node

        # if previous node is last node and not equal
        if current_node.item != node.item and current_node.next is None:
            return "node not exits!"

        # if removed node is the last node
        if current_node.item == node.item and current_node.next is None:
            pre_node.next = None
            return self
        
        # if removed node is a normal node
        pre_node.next = current_node.next
        return self


    def search_node(self, item):
        last_node = self.head
        while(last_node.item != item and last_node.next is not None):
            last_node = last_node.next
        
        if last_node.next is None and last_node.item != item:
            return "node not found!"
        else:
            return last_node

    def modify_node(self, old_node, new_node):
        old_node = self.search_node(old_node.item)
        if isinstance(old_node, Node):
            old_node.item = new_node.item
        else:
            return "not not exist!"

    def reverse(self):
        pass 

    def turn_to_list(self):
        node_items = []
        last_node = self.head
        while(last_node.next is not None):
            node_items.append(last_node.item)
            last_node = last_node.next

        node_items.append(last_node.item)
        return node_items
