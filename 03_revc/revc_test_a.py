#Trying to put all of the files in one folder so I can run them one by one

""" Tests for revc.py """

from subprocess import getstatusoutput
import platform
import os
import re


#print(os.getcwd())
base_dir = os.getcwd()+'/my_tests/'
#print(base_dir)
#print(os.listdir(base_dir))
PRG=(os.listdir("my_tests/")) # Doesnt seem like much but I am working through making many solutions


for i in list(PRG):
    #RUN = f'python {i}' if platform.system() == 'Windows' else i
    #print(i)
    inputs1 = os.getcwd()+ '/tests/tests/inputs/' # Current working directory for tests
    #print(inputs1)
    inputs_for_tests=(os.listdir(inputs1)) #iterating over heerrre
    #print(inputs_for_tests)
    for j in inputs_for_tests:
        RUN = f'python {i} {j}' if platform.system() == 'Windows' else i
    

    #TEST1 = ('.tests/tests/inputs/input1.txt', '.tests/tests/inputs/output1.txt') # adding the inputs
    #TEST2 = ('.tests/tests/inputs/input2.txt', '.tests/tests/inputs/output2.txt')
    
    
    
        def test_exists() -> None:
            """ Program exists """
            assert os.path.isfile(RUN)
        


    # --------------------------------------------------
        def test_usage() -> None:
            """ Prints usage """

            for arg in ['-h', '--help']:
                rv, out = getstatusoutput(f'{RUN} {arg}')
                assert rv == 0
                assert out.lower().startswith('usage:')
                
        

        # --------------------------------------------------
        def test_no_args() -> None:
            """ Dies on no args """

            rv, out = getstatusoutput(RUN)
            assert rv != 0
            assert re.match("usage", out, re.IGNORECASE)
'''

        # --------------------------------------------------
        def test_uppercase() -> None:
            """ Runs on uppercase input """

            rv, out = getstatusoutput(f'{RUN} AAAACCCGGT')
            assert rv == 0
            assert out == 'ACCGGGTTTT'

'''
'''
        # --------------------------------------------------
        def test_lowercase() -> None:
            """ Runs on lowercase input """

            rv, out = getstatusoutput(f'{RUN} aaaaCCCGGT')
            assert rv == 0
            assert out == 'ACCGGGtttt'


        # --------------------------------------------------
        def test_input1() -> None:
            """ Runs on file input """

            file, expected = TEST1
            rv, out = getstatusoutput(f'{RUN} {file}')
            assert rv == 0
            assert out == open(expected).read().rstrip()


        # --------------------------------------------------
        def test_input2() -> None:
            """ Runs on file input """

            file, expected = TEST2
            rv, out = getstatusoutput(f'{RUN} {file}')
            assert rv == 0
            assert out == open(expected).read().rstrip()'''