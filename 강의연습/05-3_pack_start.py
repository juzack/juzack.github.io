# import sys
# sys.path.append("./game")

import game.sound.echo
game.sound.echo.echo_test()

from game.sound import echo
echo.echo_test()

from game.sound.echo import echo_test
echo_test()

'''__init__.py의 용도
    폴더 안에 해당 __init__.py가 있으면 그 폴더는 파이썬패키지로 취급
    패키지와 관련된 설정이나 초기ㅗ하 코드를 포하할 수 있음
        패키지 공통 상수, 함수, 클래스 정의
        하위 모듈 import
    파이썬 3.3 이후 없어도 패키지로 인식될 수 있음. 하지만 일반 프로젝트에서는 여전히 __init__.py를 넣는 것이 표준
    from 패키지 import * 에서 노출할 심볼 제어 (__all__)
        from myexam import add 처럼 구체적으로 이름을 적어 import하는 경우에는 __all__와 상관없이 동작, __all__는 오직 from ... import * 에만 영햐을 줌
    예) 패키지 변수 및 함수 정의
        VERSION = 3.
        def print_version_info():
        print(f"The version of this game is {VERSION}.")'''
        
import game
print(game.VERSION)

game.print_version_info()
game.render_test()

from game.graphic.render import render_test