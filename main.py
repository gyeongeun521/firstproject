import streamlit as st

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 모둠 & 자유 탐구 주제 추천", page_icon="🔬")

st.title("🔬 MBTI 기반 모둠 & 자유 탐구 주제 추천")
st.subheader("MBTI와 이름을 입력하면, 어울리는 과학 모둠과 자유 탐구 주제를 추천해줄게요! 🧪✨")

# 사용자 이름 입력
name = st.text_input("이름을 입력하세요 ✍️")

# MBTI → 모둠 매핑 (중학교 과학에 맞춘 주제)
group_info = {
    # 🧠 논리파 과학 덕후 모둠
    "INTP": ("논리파 과학 덕후 모둠 🧠", ["INTP", "INTJ", "ENTP", "ENTJ"], "🔦 '빛의 반사와 굴절 실험 설계하기'"),
    "INTJ": ("논리파 과학 덕후 모둠 🧠", ["INTP", "INTJ", "ENTP", "ENTJ"], "🔋 '전기 회로의 직렬·병렬 연결 실험하기'"),
    "ENTP": ("논리파 과학 덕후 모둠 🧠", ["INTP", "INTJ", "ENTP", "ENTJ"], "🧲 '자석과 자기장 실험 키트 만들기'"),
    "ENTJ": ("논리파 과학 덕후 모둠 🧠", ["INTP", "INTJ", "ENTP", "ENTJ"], "⚡ '정전기와 도체의 관계 실험하기'"),

    # 🌌 이상주의자 상상 모둠
    "INFJ": ("이상주의자 상상 모둠 🌌", ["INFJ", "INFP", "ENFP", "ENFJ"], "🌍 '기후 변화가 생물 다양성에 미치는 영향 조사'"),
    "INFP": ("이상주의자 상상 모둠 🌌", ["INFJ", "INFP", "ENFP", "ENFJ"], "🌱 '식물의 광합성 속도에 영향을 주는 요인 실험'"),
    "ENFP": ("이상주의자 상상 모둠 🌌", ["INFJ", "INFP", "ENFP", "ENFJ"], "☀️ '태양의 고도 변화와 그림자의 길이 관계 실험'"),
    "ENFJ": ("이상주의자 상상 모둠 🌌", ["INFJ", "INFP", "ENFP", "ENFJ"], "🌊 '해수면 상승이 생태계에 미치는 영향 영상 제작'"),

    # 📐 현실 기반 꼼꼼이 모둠
    "ISTJ": ("현실 기반 꼼꼼이 모둠 📐", ["ISTJ", "ISFJ", "ESTJ", "ESFJ"], "💧 '물의 상태 변화 실험: 응결과 증발 관찰'"),
    "ISFJ": ("현실 기반 꼼꼼이 모둠 📐", ["ISTJ", "ISFJ", "ESTJ", "ESFJ"], "🧫 '세균 번식 조건 실험하기 (깨끗한 손의 중요성)'"),
    "ESTJ": ("현실 기반 꼼꼼이 모둠 📐", ["ISTJ", "ISFJ", "ESTJ", "ESFJ"], "🍽️ '화학 변화와 물리 변화 구분 실험'"),
    "ESFJ": ("현실 기반 꼼꼼이 모둠 📐", ["ISTJ", "ISFJ", "ESTJ", "ESFJ"], "🥶 '냉장고 속 기체의 응축 실험'"),

    # ⚙️ 감각형 실험파 모둠
    "ISTP": ("감각형 실험파 모둠 ⚙️", ["ISTP", "ISFP", "ESTP", "ESFP"], "✈️ '양력 실험: 종이비행기와 비행 원리'"),
    "ISFP": ("감각형 실험파 모둠 ⚙️", ["ISTP", "ISFP", "ESTP", "ESFP"], "🎨 '빛과 색의 혼합 실험 (RGB/CMY)'"),
    "ESTP": ("감각형 실험파 모둠 ⚙️", ["ISTP", "ISFP", "ESTP", "ESFP"], "🎢 '속력과 가속도 실험: 미끄럼틀 실험 장치 만들기'"),
    "ESFP": ("감각형 실험파 모둠 ⚙️", ["ISTP", "ISFP", "ESTP", "ESFP"], "🎥 '소리의 진동 실험: 스피커 위의 소금 영상 만들기'")
}

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 🔽", ["선택하세요"] + list(group_info.keys()))

# 출력
if name and selected_mbti != "선택하세요":
    group_name, members, topic = group_info[selected_mbti]
    st.success(f"🎉 {name}님은 **{group_name}** 에 속해요!")
    st.markdown(f"👥 **같은 모둠원 유형**: {', '.join(members)}")
    st.markdown(f"🧪 **추천 자유 탐구 주제**: {topic}")
    st.balloons()
elif not name:
    st.info("👤 이름을 입력해주세요!")
elif selected_mbti == "선택하세요":
    st.info("🔽 MBTI를 선택해주세요!")
