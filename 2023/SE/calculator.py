import random
import sys
import unittest

class TestProper(unittest.TestCase):
    def test(self):
        a = []
        a.append(1)
        self.assertEqual(factorial(a),1)
    def test2(self):
        a = []
        a.append(2)
        self.assertEqual(factorial(a),2)
    def test3(self):
        a = []
        a.append(10)
        self.assertEqual(factorial(a),3628800)

class TestBig(unittest.TestCase):
    def test_big(self):
        a = []
        a.append(1000)
        self.assertEqual(factorial(a),402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461062892187960223838971476088506276862967146674697562911234082439208160153780889893964518263243671616762179168909779911903754031274622289988005195444414282012187361745992642956581746628302955570299024324153181617210465832036786906117260158783520751516284225540265170483304226143974286933061690897968482590125458327168226458066526769958652682272807075781391858178889652208164348344825993266043367660176999612831860788386150279465955131156552036093988180612138558600301435694527224206344631797460594682573103790084024432438465657245014402821885252470935190620929023136493273497565513958720559654228749774011413346962715422845862377387538230483865688976461927383814900140767310446640259899490222221765904339901886018566526485061799702356193897017860040811889729918311021171229845901641921068884387121855646124960798722908519296819372388642614839657382291123125024186649353143970137428531926649875337218940694281434118520158014123344828015051399694290153483077644569099073152433278288269864602789864321139083506217095002597389863554277196742822248757586765752344220207573630569498825087968928162753848863396909959826280956121450994871701244516461260379029309120889086942028510640182154399457156805941872748998094254742173582401063677404595741785160829230135358081840096996372524230560855903700624271243416909004153690105933983835777939410970027753472000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
class TestZero(unittest.TestCase):
    def test(self):
        a = []
        a.append(0)
        self.assertEqual(factorial(a),1)
class TestNegative(unittest.TestCase):
    def test(self):
        a = []
        a.append(-1)
        self.assertEqual(factorial(a), "[ERROR] Out Of Range")
class TestImproper(unittest.TestCase):
    def test(self):
        a = []
        a.append(2)
        a.append(4)
        self.assertEqual(factorial(a),"[ERROR] Input Error")

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
        
random.seed(0,2)

def op_priority(op):       # 연산자의 우선순위를 결정하는 함수
    if op in ['+', '-']:
        return 1
    elif op == '*':        # '*' 연산자의 우선순위가 더 높으므로 1보다 더 큰 2를 리턴
        return 2

def infix_to_postfix(expr, postfix): # infix를 postfix로 바꾸는 함수
    stack = []          # stack으로 활용하기 위한 list 선언
    for token in expr:
        if token in ['+', '-', '*']: # 연산자인 경우
            while stack and op_priority(stack[-1]) >= op_priority(token):
                postfix.append(stack.pop()) # 스택의 맨위에 있는 연산자가 더 크거나 같은 연산자일 때까지 stack에서 pop()한 것을 postfix list에 저장하고
            stack.append(token) # stack에 현재 연산자를 넣어준다.
        else:   # 피연산자인 경우
            postfix.append(token)     # 피연산자인 경우 postfix list에 저장한다.

    while stack:
        postfix.append(stack.pop())     # stack에 남아있는 연산자들을 postfix list에 추가한다.

def calc_postfix(postfix, tmp):     # postfix를 계산하는 함수
    result = 0
    if len(postfix) == 1:   # 입력이 정수 하나인 경우 ex. 5 = ?
        tmp.append(int(postfix[0]))
        result = tmp[-1]
        return result
    
    for token in postfix:
        if token in ['+', '-', '*']:
            second = tmp.pop()
            first = tmp.pop()
            op = token[0]
            if op == '+':       # +인 경우 계산
                result = first + second
            elif op == '-':     # -인 경우 계산
                result = first - second
            elif op == '*':     # *인 경우 계산
                result = first * second
            tmp.append(result)
        else:
            tmp.append(int(token))  # 올바른 수식이라면 계산 결과값을 tmp 스택에도 저장
    return result

def print_error():
    print("[SYSTEM] ERROR!")
    sys.exit()

def clear(expr, postfix, dummy):
    postfix.clear()
    expr.clear()
    dummy.clear()

def factorial(expr):
    result = 1
    num = int(expr[-1])
    if num == 0 :
        return 1
    if num < 0:
        result = "[ERROR] Out Of Range"
        return result
    if len(expr) >= 2:
        result = "[ERROR] Input Error"
        return result
    for i in range(1, num + 1):
        result *= i
    return result

def testfunction(expr, postfix):

    dummy = []

    #test1
    print("error1", end = "") #error 메시지 출력, error가 발생하였을 때 어디서 오류가 발생하였는지 알아보기 위한 트릭
    clear(expr, postfix, dummy) #expr, postfix, dummy 리스트 초기화
    for i in range(1,10001): #1~10000까지의 수를 더하는 연산을 하여 큰 규모의 더하기 연산에 대하여 테스트 함
        expr.append(str(i))
        if i == 10000:
            break
        expr.append('+')
    
    infix_to_postfix(expr, postfix)
    assert 50005000 == calc_postfix(postfix, dummy), "sum plus error"
    print('\b''\b''\b''\b''\b''\b', end = "") #\b를 호출해서 cursor을 원위치로 돌린다
    
    #test2
    print("error2", end = "") # cursor위치가 되돌려졌고 그 위치에서부터 덮어써진다
    clear(expr, postfix, dummy)
    for i in range(1,10001): #-1~-10000까지의 수를 더하는 연산을 하여 큰 규모의 더하기 연산에 대하여 테스트 함
        expr.append(str(-i))
        if i == 10000:
              break
        expr.append('+')

    infix_to_postfix(expr, postfix)
    assert -50005000 == calc_postfix(postfix, dummy), "sum minus error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    #test3
    print("error3", end = "")
    clear(expr, postfix, dummy)
    for i in range(1,10001): #1~10000까지의 수를 빼는 연산을 하여 큰 규모의 빼기 연산에 대하여 테스트 함
        expr.append(str(i))
        if i == 10000:
            break
        expr.append('-')
    
    infix_to_postfix(expr, postfix)
    
    assert -50004998 == calc_postfix(postfix,dummy), "minus error"
    print('\b''\b''\b''\b''\b''\b', end = "")
    
    #test4
    print("error4", end = "")
    clear(expr, postfix, dummy)
    for i in range(1,10001): #-1~-10000까지의 수를 빼는 연산을 하여 큰 규모의 빼기 연산에 대하여 테스트 함
        expr.append(str(-i))
        if i == 10000:
            break
        expr.append('-')
    
    infix_to_postfix(expr, postfix)
    
    assert 50004998 == calc_postfix(postfix,dummy), "minus error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    #test5
    print("error5", end = "")
    clear(expr, postfix, dummy)
    for i in range(1,3073): #2^3072를 연산하여 큰 규모의 양의 정수 곱하기 연산에 대하여 테스트 함
        expr.append(str(2))
        if i == 3072:
            break
        expr.append('*')

    infix_to_postfix(expr, postfix)
    assert 5809605995369958062859502533304574370686975176362895236661486152287203730997110225737336044533118407251326157754980517443990529594540047121662885672187032401032111639706440498844049850989051627200244765807041812394729680540024104827976584369381522292361208779044769892743225751738076979568811309579125511333093243519553784816306381580161860200247492568448150242515304449577187604136428738580990172551573934146255830366405915000869643732053218566832545291107903722831634138599586406690325959725187447169059540805012310209639011750748760017095360734234945757416272994856013308616958529958304677637019181594088528345061285863898271763457294883546638879554311615446446330199254382340016292057090751175533888161918987295591531536698701292267685465517437915790823154844634780260102891718032495396075041899485513811126977307478969074857043710716150121315922024556759241239013152919710956468406379442914941614357107914462567329693696\
        == calc_postfix(postfix, dummy), "big integer error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    #test6
    print("error6", end = "")
    clear(expr, postfix, dummy)
    for i in range(1,3073): #(-2)^3072를 연산하여 큰 규모의 음의 정수 곱하기 연산에 대하여 테스트 함
        expr.append(str(-2))
        if i == 3072:
            break
        expr.append('*')
    
    infix_to_postfix(expr, postfix)
    assert 5809605995369958062859502533304574370686975176362895236661486152287203730997110225737336044533118407251326157754980517443990529594540047121662885672187032401032111639706440498844049850989051627200244765807041812394729680540024104827976584369381522292361208779044769892743225751738076979568811309579125511333093243519553784816306381580161860200247492568448150242515304449577187604136428738580990172551573934146255830366405915000869643732053218566832545291107903722831634138599586406690325959725187447169059540805012310209639011750748760017095360734234945757416272994856013308616958529958304677637019181594088528345061285863898271763457294883546638879554311615446446330199254382340016292057090751175533888161918987295591531536698701292267685465517437915790823154844634780260102891718032495396075041899485513811126977307478969074857043710716150121315922024556759241239013152919710956468406379442914941614357107914462567329693696\
        == calc_postfix(postfix, dummy), "big integer2 error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    #test7
    print("error7", end = "")
    clear(expr, postfix, dummy)

    for i in range(1,401) : #400!을 연산하여 큰 규모의 정수 곱하기 연산에 대하여 테스트 함
        expr.append(str(i))
        if i == 400:
            break
        expr.append('*')

    infix_to_postfix(expr, postfix)

    assert 64034522846623895262347970319503005850702583026002959458684445942802397169186831436278478647463264676294350575035856810848298162883517435228961988646802997937341654150838162426461942352307046244325015114448670890662773914918117331955996440709549671345290477020322434911210797593280795101545372667251627877890009349763765710326350331533965349868386831339352024373788157786791506311858702618270169819740062983025308591298346162272304558339520759611505302236086810433297255194852674432232438669948422404232599805551610635942376961399231917134063858996537970147827206606320217379472010321356624613809077942304597360699567595836096158715129913822286578579549361617654480453222007825818400848436415591229454275384803558374518022675900061399560145595206127211192918105032491008000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\
        == calc_postfix(postfix, dummy), "big integer factorial error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    #test8
    print("error8", end = "")
    clear(expr, postfix, dummy)

    for i in range(0,1000): #임의의 정수와 임의의 연산자들의 집합의 연산에 정삭적으로 작동하는지에 대하여 테스트 함
        expr.append(str(random.randint(0,256)))
        d = random.randint(0,256)
        if i == 999:
            continue
        if (d % 3 == 0): 
            expr.append('+')
        elif (d % 3 == 1):
            expr.append('-')
        elif (d % 3 == 2):
            expr.append('*')

    infix_to_postfix(expr, postfix)
    assert 176515113295 == calc_postfix(postfix, dummy), "big calculation error"
    print('\b''\b''\b''\b''\b''\b', end = "")


    print("test complete, No abnormality found")
    
    sys.exit(0)

if __name__ == "__main__":
    expr = []           # 식을 저장하기 위해 list 선언
    postfix = []        # infix를 postfix로 바꾼 표현을 저장하는 list 선언
    tmp = []            # calc_postfix()함수에서 사용할 stack 선언
    ans = 0             # 답 임시 저장 변수
    is_operator = False     # 333++같이 연속으로 숫자가 나오는 경우를 막기 위한 변수
    is_right = True
    operators = ['+', '-', '*', '!']

    #suite = unittest.TestSuite()
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Testinfix_to_postfix))
    #unittest.TextTestRunner().run(suite)
    #sys.exit(0)
    # unittest.main(exit=True)

    while True :
        try:
            #testfunction(expr,postfix)     # test가 필요할 경우만 사용
            temp = input()
            if temp in operators and not is_operator:   # 입력이 연산자이고 is_operator가 True가 아닌 경우
                is_right = False        # 비정상적인 입력으로 판정하고 is_right에 False를 대입
            if(is_operator):        # 입력을 받을 때마다 정상적인 입력인지 확인하기 위해 
                is_operator = False # 번갈아가며 False, True변경
            else:
                is_operator = True
            if temp == "!":
                if not expr:
                    print_error()
                result = str(factorial(expr))
                if not result.isdigit():
                    print(result)
                    break
                temp = input()
                if temp == "=":     #팩토리얼 이후에 '='이 입력되었을 때 결과 출력
                    print(result)
                    break
                else:               # 아닐 경우 표준 에러 출력
                    print_error()
            if temp == "7503":     # 이스터에그
                print('[EVENT] "안녕! 7503은 사용할 수 없는 숫자야"')
                break
            if temp == "1015":     # 개교기념일 이스터에그
                print("[EVENT] 전북대 개교기념일입니다.")
                break
            if temp == '=':        # '='가 입력된 경우 지금까지 입력된 expr을 함수에 전달해 계산
                if not expr:       # 아무것도 입력하지 않고 '='를 입력한 경우
                    print_error()
                if not is_right:
                    print_error()
                infix_to_postfix(expr, postfix)
                ans = calc_postfix(postfix, tmp)
                if len(tmp) > 1:        # tmp list가 1보다 클 경우 숫자가 비정상적으로 많다.
                    print_error()
                print(ans)
                break
            expr.append(temp)
        except Exception:
            print_error()