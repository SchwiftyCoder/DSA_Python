import unittest
import stackExceptions
import stack_implementation


class TestArrayStack(unittest.TestCase):
    def test_stack(self):
        stack = stack_implementation.ArrayStack()
        self.assertTrue(stack.isEmpty())  # Expect true, stack should be empty

        # Test push and len
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(len(stack), 3)  # Expect 3

        # Test top method
        self.assertEqual(stack.top(), 3)  # Expect 3 as the top element

        # Test pop method
        self.assertEqual(stack.pop(), 3)  # Expect 3 to be popped
        self.assertEqual(stack.pop(), 2)  # Expect 2 to be popped
        self.assertEqual(len(stack), 1)  # Expect the length to be 1

        # Test pop on last element
        self.assertEqual(stack.pop(), 1)  # Expect 1 to be popped
        self.assertTrue(stack.isEmpty())  # Expect true, stack should be empty again

        # Test pop method to raise Empty exception
        with self.assertRaises(stackExceptions.Empty("Stack is empty")):
            stack.pop()

        # Test top method to raise Empty exception
        with self.assertRaises(stackExceptions.Empty("Stack is empty")):
            stack.top()

        # Test pushing different types of elements
        stack.push("test")
        stack.push(10.5)
        stack.push([1, 2, 3])
        self.assertEqual(
            stack.top(), [1, 2, 3]
        )  # Expect the list [1, 2, 3] as the top element


if __name__ == "__main__":
    unittest.main()


