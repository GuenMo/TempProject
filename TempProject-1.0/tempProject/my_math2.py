# coding:utf-8

'''
이 클래스는 Math 클래스 입니다.
'''

class Math(object):
    """두 개의 int 값을 입력받아 다양한 연한을 할 수 있도록 하는 클래스.
    
    :param int a: a값
    :param int b: b값
    """
    
    def __inti__(self, a, b):
        self._a = a
        self._b = b
        
    def sum(self):
        """
        2개의 파라미터(argA, argB) 를 받아서, argA 에서 argB 를 뺀 결과를 반환하는 함수입니다.
    
        :param argA: argumentA 입니다.
        :param argB: argumentB 입니다.
        :return: argA-argB. 결과를 반환합니다.
        
        예제:
            >>> Math(1, 2).add()
            3
        """
        return self._a + self._b
    
    def subtract(self):
        """
        2개의 파라미터(argA, argB) 를 받아서, argA 에서 argB 를 뺀 결과를 반환하는 함수입니다.
    
        :param argA: argumentA 입니다.
        :param argB: argumentB 입니다.
        :return: argA-argB. 결과를 반환합니다.
        """
        return self._a - self._b
    