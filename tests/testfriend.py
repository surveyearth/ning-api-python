import unittest
import basetest


class TestFriends(basetest.BaseTestCase):

    def test_get_friends(self):
        fields = ["author", "createdDate", "updatedDate"]
        attrs = self.field_args(fields)
        attrs['count'] = 5
        content = self.api.get("Friend/recent", attrs)
        self.assertTrue(content["success"])


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestFriends)


if __name__ == '__main__':
    unittest.main()
