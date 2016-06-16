# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None


class DoubleLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if not self.head and self.tail:
            return
        _node = self.head
        while _node:
            print """
            {} | {} | {} | {}
            """.format(
                _node.prev, _node.key, _node.value, _node.next)
            _node = _node.next

    def isEmpty(self):
        return not self.tail

    def removeLast(self):
        self.remove(self.tail)

    def remove(self, node):
        if self.head == self.tail:
            self.head = self.tail = None
            return
        if node == self.head:
            node.next.prev = None
            self.head = node.next
            return
        if node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            return
        node.prev.next = node.next
        node.next.prev = node.prev

    def addFirst(self, node):
        if not self.head:
            self.head = self.tail = node
            node.prev = node.next = None
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
        node.prev = None

    def addLast(self, node):
        pass


class LRUCache(object):

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.hash_map=dict()  # OrderedDict
        self.cache = DoubleLinkedList()

    def get(self, key):
        if key in self.hash_map and self.hash_map[key]:
            self.cache.remove(self.key)
            self.cache.addFirst(self.hash_map[key])
            return self.hash_map[key].value

    def set(self, key, value):
        if key in self.hash_map:
            self.cache.remove(self.hash_map[key])
            self.cache.addFirst(self.hash_map[key])
            self.hash_map[key].value = value
        else:
            node = Node(key, value)
            self.hash_map[key] = node
            self.cache.addFirst(node)
            self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                del self.hash_map[self.cache.tail.key]
                self.cache.removeLast()
