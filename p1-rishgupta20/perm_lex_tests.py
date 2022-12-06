import unittest
import perm_lex


# Starter test cases - write more!

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_lex.perm_gen_lex('ab'), ['ab', 'ba'])
        self.assertEqual(perm_lex.perm_gen_lex(''), [])
        self.assertEqual(perm_lex.perm_gen_lex('a'), ['a'])
        self.assertEqual(perm_lex.perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(perm_lex.perm_gen_lex('z'), ['z'])
        self.assertEqual(perm_lex.perm_gen_lex('efgh'), ['efgh', 'efhg', 'egfh', 'eghf', 'ehfg', 'ehgf', 'fegh', 'fehg',
                                                         'fgeh', 'fghe', 'fheg', 'fhge', 'gefh', 'gehf', 'gfeh', 'gfhe',
                                                         'ghef', 'ghfe', 'hefg', 'hegf', 'hfeg', 'hfge', 'hgef', 'hgfe']
                         )


if __name__ == "__main__":
    unittest.main()
