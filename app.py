import streamlit as st

# 1. 리스트(list)를 활용한 선택 항목 정의
study_methods = ["히브라타교육", "백지공부", "멘토멘티"]
subjects = ["국어", "영어", "수학"]


# 2. def를 활용한 공부 방법 및 과목 분석 함수
def analyze_study_method(method, subject):
  # if-elif-else를 활용한 공부 방법별 정의, 효과, 소요자원 및 과목별 점수 계산
  if method == "히브라타교육":
    definition = (
        "짝을 지어 서로 질문하고 토론하며 개념을 깊이 이해하는 유대인식 토론"
        " 학습법(하브루타)입니다."
    )
    effects = [
        "질문을 만들고 답하는 과정에서 비판적 사고력과 논리력이 향상됩니다.",
        "친구에게 설명하면서 자신이 정확히 아는 것과 모르는 것을 구분할 수 있습니다.",
        "수동적인 암기보다 기억이 훨씬 오래 지속됩니다.",
    ]
    resources = [
        [
            "시간소비도",
            "상",
            "서로 질문하고 토론하며 생각을 정리하는 데 많은 시간이 걸립니다.",
        ],
        [
            "비용소비",
            "하",
            "별도의 교재나 강의 없이 대화할 상대와 노트만 있으면 됩니다.",
        ],
    ]

    if subject == "국어":
      score = 85
    elif subject == "영어":
      score = 80
    else:  # 수학
      score = 65

  elif method == "백지공부":
    definition = (
        "교재나 노트를 덮고 배운 내용을 아무것도 없는 백지에 스스로 떠올리며"
        " 적어보는 인출 학습법입니다."
    )
    effects = [
        "머릿속 지식을 직접 꺼내어 적으면서 메타인지(자기 객관화) 능력이 극대화됩니다.",
        "시험 직전 자신이 취약한 개념을 빠르게 찾아내어 보완할 수 있습니다.",
        "단순 반복 읽기보다 실전 기억 인출 속도가 빨라집니다.",
    ]
    resources = [
        [
            "시간소비도",
            "상",
            "배운 내용을 처음부터 끝까지 직접 떠올리며 적는 데 시간이 오래 걸립니다.",
        ],
        [
            "비용소비",
            "하",
            "빈 종이(A4용지, 연습장)와 펜만 있으면 추가 비용이 들지 않습니다.",
        ],
    ]

    if subject == "국어":
      score = 75
    elif subject == "영어":
      score = 85
    else:  # 수학
      score = 90

  else:  # 멘토멘티
    definition = (
        "잘 아는 사람(멘토)과 배우는 사람(멘티)이 짝을 이루어 질문하고"
        " 가르쳐주며 함께 성장하는 학습법입니다."
    )
    effects = [
        "모르는 문제를 즉시 질문하고 해결할 수 있어 학습 막힘이 줄어듭니다.",
        "멘토의 공부 습관과 문제 접근 노하우를 자연스럽게 배울 수 있습니다.",
        "서로 격려하며 학습 동기와 책임감을 꾸준히 유지할 수 있습니다.",
    ]
    resources = [
        [
            "시간소비도",
            "하",
            "막히는 부분을 멘토에게 바로 질문해 혼자 고민하는 시간을 크게 줄여줍니다.",
        ],
        [
            "비용소비",
            "상",
            "전문 멘토링이나 과외 형태로 진행할 경우 수업료나 모임 비용이 발생할 수 있습니다.",
        ],
    ]

    if subject == "국어":
      score = 68
    elif subject == "영어":
      score = 78
    else:  # 수학
      score = 92

  return definition, effects, resources, score


# 웹앱 화면 구성
st.title("📚 맞춤형 공부 방법 추천")

# (1) 공부방법 선택
selected_method = st.selectbox("1. 공부방법 선택", study_methods)

# (2) 과목입력 선택
selected_subject = st.selectbox("2. 과목입력 선택", subjects)

# 분석하기 버튼
if st.button("분석하기"):
  # 함수 호출하여 결과 받아오기
  definition, effects, resources, score = analyze_study_method(
      selected_method, selected_subject
  )

  st.divider()
  st.header(f"🔍 [{selected_method}] 분석 결과")

  # 정의 출력
  st.subheader("1) 정의")
  st.write(definition)

  # 효과 출력 (for 반복문 활용)
  st.subheader("2) 효과")
  for effect in effects:
    st.write(f"- {effect}")

  # 소요자원 테이블표 출력 (for 반복문으로 테이블 데이터 구성)
  st.subheader("3) 소요자원")
  table_data = []
  for item in resources:
    table_data.append({
        "자원 구분": item[0],
        "소비도": item[1],
        "이유": item[2],
    })
  st.table(table_data)

  # 마지막 추천점수 및 70점 이상 추천 문구 출력
  st.divider()
  st.subheader(f"{selected_subject}의 추천점수:{score}")

  if score >= 70:
    st.success("추천합니다")
  else:
    st.info("다른 공부 방법과 함께 활용하는 것을 권장합니다.")
