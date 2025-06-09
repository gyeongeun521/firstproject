import streamlit as st

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 모둠 & 탐구 주제 추천", page_icon="🤝")

st.title("🔬 경은쌤과 함께하는 MBTI 기반 모둠 & 자유 탐구 주제 추천")
st.subheader("나에게 딱 맞는 모둠과 탐구 주제를 찾아보자! 🧠✨")

# MBTI → 모둠 매핑 (16개 전부 포함)
group_info = {
    # 🧠 논리파 과학 덕후 모둠
    "INTP": ("논리파 과학 덕후 모둠 🧠", ["INTP", "INTJ", "ENTP", "ENTJ"], "💡 'AI는 사고할 수 있을까? 인공지능과 인간의 사고 비교'"),
    "INTJ": ("논리파 과학 덕후 모둠 🧠", ["INTP", "INTJ", "ENTP", "ENTJ"], "🧠 '우주 여행을 위한 최적 궤도 계산법'"),
    "ENTP": ("논리파 과학 덕후 모둠 🧠", ["INTP", "INTJ", "ENTP", "ENTJ"], "🔁 '시간여행 이론의 과학적 가능성 분석'"),
    "ENTJ": ("논리파 과학 덕후 모둠 🧠", ["INTP", "INTJ", "ENTP", "ENTJ"], "📊 '미래 사회 예측을 위한 알고리즘 설계'"),

    # 🌌 이상주의자 상상 모둠
    "INFJ": ("이상주의자 상상 모둠 🌌", ["INFJ", "INFP", "ENFP", "ENFJ"], "🌱 '지속가능한 미래 도시에 대한 상상과 설계'"),
    "INFP": ("이상주의자 상상 모둠 🌌", ["INFJ", "INFP", "ENFP", "ENFJ"], "🧬 '감정과 유전자: 성격은 DNA로 결정되는가?'"),
    "ENFP": ("이상주의자 상상 모둠 🌌", ["INFJ", "INFP", "ENFP", "ENFJ"], "🌈 'SF 영화 속 과학 개념 분석하기'"),
    "ENFJ": ("이상주의자 상상 모둠 🌌", ["INFJ", "INFP", "ENFP", "ENFJ"], "🔮 'AI는 윤리적 결정을 내릴 수 있을까?'"),

    # 📐 현실 기반 꼼꼼이 모둠
    "ISTJ": ("현실 기반 꼼꼼이 모둠 📐", ["ISTJ", "ISFJ", "ESTJ", "ESFJ"], "📏 '엘리베이터 속 알고리즘 찾기: 최적 동선 설계'"),
    "ISFJ": ("현실 기반 꼼꼼이 모둠 📐", ["ISTJ", "ISFJ", "ESTJ", "ESFJ"], "🧪 '약물 보관 온도와 화학 변화 관찰 실험'"),
    "ESTJ": ("현실 기반 꼼꼼이 모둠 📐", ["ISTJ", "ISFJ", "ESTJ", "ESFJ"], "🏙️ '스마트시티의 구조와 데이터 흐름 분석'"),
    "ESFJ": ("현실 기반 꼼꼼이 모둠 📐", ["ISTJ", "ISFJ", "ESTJ", "ESFJ"], "🔎 '생활 속 안전장치의 과학 원리 조사'"),

    # ⚙️ 감각형 실험파 모둠
    "ISTP": ("감각형 실험파 모둠 ⚙️", ["ISTP", "ISFP", "ESTP", "ESFP"], "💥 '생활 속 물리 실험 리메이크 & 영상 제작'"),
    "ISFP": ("감각형 실험파 모둠 ⚙️", ["ISTP", "ISFP", "ESTP", "ESFP"], "🎨 '빛과 색의 조화: 과학과 예술의 만남'"),
    "ESTP": ("감각형 실험파 모둠 ⚙️", ["ISTP", "ISFP", "ESTP", "ESFP"], "🎮 'VR 게임 속 과학 원리 분석'"),
    "ESFP": ("감각형 실험파 모둠 ⚙️", ["ISTP", "ISFP", "ESTP", "ESFP"], "📹 '나만의 과학실험 브이로그 제작하기'"),
}

# 🎯 드롭다운으로 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 🔽", ["선택하세요"] + list(group_info.keys()))

# 💥 결과 출력
if selected_mbti != "선택하세요":
    group_name, members, topic = group_info[selected_mbti]
    st.success(f"🎉 당신은 **{group_name}** 에 속해요!")
    st.markdown(f"👥 **같은 모둠원**: {', '.join(members)}")
    st.markdown(f"🧪 **추천 자유 탐구 주제**: {topic}")
    st.balloons()
