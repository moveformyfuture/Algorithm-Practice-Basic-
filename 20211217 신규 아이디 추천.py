
import re #정규식 표현을 사용

def solution(new_id):
    st = new_id #st를 new_id로 선언
    st = st.lower() #대분자를 소문자로 치환
    st = re.sub('[^a-z0-9\-_.]', '', st) #
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st