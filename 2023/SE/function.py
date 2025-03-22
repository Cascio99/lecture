class Testrespone_priortyeop(unittest.TestCase):
    def testplus(self):
        input1 = '+'
        self.assertEqual(op_priority(input1),1)
    def testminus(self):
        input2 = '-'
        self.assertEqual(op_priority(input2),1)
    def testmultiply(self):
        input3 = '*'
        self.assertEqual(op_priority(input3),2)

class Testinfix_to_postfix(unittest.TestCase):
    def test1(self):
        expr_test1 = [2,'*',4,'+',6,'*',8]
        test_postfix1 = [2,4,'*',6,8,'*','+']
        postfix10 = []
        infix_to_postfix(expr_test1,postfix10)
        self.assertEqual(postfix10,test_postfix1)
    def test2(self):
        expr_test2 = [2,'*',2,'+',2,'*',2,'+',2,'*',2,'+',2,'*',2,'*',2,'*',2,'*',2,'*',2,'+',2,'*',2,'*',2,'*',2,'*',2,'*',2,'*',2,'*',2,'*',2,'*',2,'+',2]
        test_postfix2 = [2,2,'*',2,2,'*','+',2,2,'*','+',2,2,'*',2,'*',2,'*',2,'*',2,'*','+',2,2,'*',2,'*',2,'*',2,'*',2,'*',2,'*',2,'*',2,'*',2,'*','+',2,'+']
        postfix11 = []
        infix_to_postfix(expr_test2,postfix11)
        self.assertEqual(postfix11,test_postfix2)
            
class Testcalc_postfix(unittest.TestCase):
    def test1(self):
        test_postfix1 = [2,4,'*',6,8,'*','+']
        tmp_test = []
        self.assertEqual(calc_postfix(test_postfix1,tmp_test),56)
        
    def test2(self):
        test_postfix1 = [2,2,'*',2,2,'*','+',2,2,'*','+',2,2,'*',2,'*',2,'*',2,'*',2,'*','+',2,2,'*',2,'*',2,'*',2,'*',2,'*',2,'*',2,'*',2,'*',2,'*','+',2,'+']
        tmp_test = []
        self.assertEqual(calc_postfix(test_postfix1,tmp_test),1102)