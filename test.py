import unittest
import roroaring64


class DeserializeTest(unittest.TestCase):

    def test_invalid_data_raises_exception(self):
        with self.assertRaisesRegex(RuntimeError, "failed alloc"):
            roroaring64.deserialize(b"fdasf")

    def test_deserializes_valid_set_correctly(self):
        result = roroaring64.deserialize(
            bytes.fromhex(
                "0100000000000000000000003a300000010000004700040010000000e64ee84ee94eea4eeb4e"))
        self.assertEqual(result, {4673254, 4673256, 4673257, 4673258, 4673259})


if __name__ == "__main__":
    unittest.main()
