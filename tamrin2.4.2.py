from keyword import kwlist
import string
from random import randint
from time import perf_counter
pro = ',.?!'
li2 = ['ali', 1233, 0, "", [], {}, 'False', '0', 'None', None, -1, [1, 2, 3], {'key': 'value'}, True, ' ', '[]',
'[1, 2, 3]', '{}', '{"a": 1}', 'True', 'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}', '{"a": 1}',
'True', 'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}', '{"a": 1}', 'True', 'ali', '1234', 1, 0.1, -0.1]
key = kwlist
key[3] = 'False'
key[0] = "and"


def solve_puzzle(puzzles):
	answer = []
	for i in puzzles:
		if isinstance(i, int) or isinstance(i, float):
			if i == 0:
				answer.append("False")
			else:
				answer.append('True')
		elif i is True or i is None:
			if i:
				answer.append('True')
			elif i is None:
				answer.append("None")
		else:
			if len(i) == 0:
				answer.append("False")
			else:
				answer.append('True')
	return answer


def decrypt_clue(tx):
	key_list = []
	for i in kwlist:
		if i in tx:
			key_list.append(i)
	return key_list


text = "ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbreakclasscontinueexceptfinallyforfromglobalimportnonlocalpassraisereturntrywhilewithandorasassertbreakclasscontinuedefdelelifelseexceptexecfinallyforfromglobalifimportinislambdnonlocalnotorpassprintraisereprreturnsupertrywhilewithyieldTrueFalseNoneasyncawaitmatchcasenonelocaloverrideprivatesealedstaticmethodvolatileabstractenumintfloatdoublebyteboolcharstructvectorlistdictionaryqueuestackinterfacenulltrycatchfinallythrowthrowsimplementsextendspublicprotectedprivatefinalstaticvoidmainStringargsSystemoutprintlnnewMapSetGetAddRemoveClearIsEmptySizeContainsKeyContainsValueKeyValuePairsForEachDoWhileSwitchCaseDefaultbreakcontinueiteratoriterablecollectionsframeworksynchronizedtransientvolatilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencegenericswildcardstypeerasurereflectionproxydecoratorfactorysingletonprototypebuildercompositeadapterbridgechainofresponsibilitycommandstateobservermementointerpreteriteratorvisitorstrategytemplatemethodflyweightmediatorproxymultithreadingconcurrencyasynchronousprogrammingeventdrivenarchitecturefunctionalprogrammingimmutables..."
"quantumcomputingqubitsentanglementsuperpositionquantumalgorithmsShorsGroverquantumcryptographyquantumteleportationartificialintelligenceAIoptimizationalgorithmsgraphtheorytraversalsearchalgorithmsdepthfirstsearchbreadthfirstsearchAstaralgorithmgeneticalgorithmssimulatedannealingparticlewarmoptimizationantcolonyoptimizationmachinelearningdeeplearningunsupervisedlearningreinforcementlearningneuralnetworksconvolutionalneuralnetworksrecurrentneuralnetworkslongshorttermmemorynetworksgenerativeadversar..."
"blockchaintechnologydistributedledgerconsensusalgorithmsproofOfWorkproofOfStakeByzantineFaultTolerancepeer-to"
"-peerP2PnetworkscryptographyhashfunctionsasymmetricencryptionpublickeyinfrastructurePKIdigitalcertificatesdigital "
"signaturesmartcontractsdecentralizedapplicationsDAppsEthereumplatformSolidityprogramminglanguageWeb3technologyNFTsnon-fungibletokensDeFidecentralizedfinancedecentralizedexchangesDEXsstablecoinscryptocurrencyminingstakingyieldfarmingliquiditypoolsoraclesDAOsdecentralizedautonomousorganizati... "


def func3(word):
	for h in word:
		if h in pro:
			return True
	return False


def func2(word):
	d = False
	d1 = False
	for k in word:
		if k in string.ascii_lowercase:
			d = True
		if k in string.ascii_uppercase:
			d1 = True
		if d1 and d:
			return True
	return False


def func(password):
	if len(password) >= 8 and func3(password) and func2(password):
		return True
	else:
		return False


def win():
	li = []
	x = tuple(input().split(' '))
	for i in range(1, len(x), 2):
		if func(x[i]):
			li.append(x[i - 1])
	return li


def game():
	answer = []
	start = perf_counter()
	while 1:
		num = randint(0, 16)
		print(bin(num))
		guess = int(input(' enter guess : '))
		if guess == num:
			answer.append('True')
		else:
			answer.append('False')
		end = perf_counter()
		if end - start >= 20:
			break
	return answer


def unlock_code(li):
	s = ''
	for i in range(4):
		s = s + li[i][0][0]
	return s


clue = [decrypt_clue(text), solve_puzzle(li2), game(), win()]
print(unlock_code(clue))
