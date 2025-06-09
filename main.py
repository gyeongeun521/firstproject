import streamlit as st

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 영화 추천기 🎥", page_icon="🎬")

# 🎯 타이틀
st.title("당신의 MBTI로 추천받는 🎬 과학&수학 명작 영화!")
st.subheader("성격대로 골라보는 명작 영화 🍿")

# ✍️ 사용자 입력 받기
mbti = st.text_input("당신의 MBTI를 입력해주세요 (예: INTP, ESFJ 등)", max_chars=4).upper()

# 🎥 MBTI별 추천 영화 DB
mbti_movies = {
    "INTP": [
        "📐 *A Beautiful Mind* (2001) – 천재 수학자의 삶을 깊이 있게 🎓",
        "🧠 *The Imitation Game* (2014) – 천재 코딩 천재 앨런 튜링 이야기 💻",
        "🌌 *Interstellar* (2014) – 논리와 과학이 뒤엉킨 감성 대서사시 🚀"
    ],
    "INFJ": [
        "🌠 *Contact* (1997) – 내면의 목소리와 우주를 잇는 이야기 ☄️",
        "💡 *Arrival* (2016) – 언어와 시간의 경계에 서다 ⏳",
        "🧬 *Gattaca* (1997) – 이상과 현실, 유전자 사회의 딜레마 🧬"
    ],
    "ENTP": [
        "🤯 *Tenet* (2020) – 시간의 퍼즐을 풀어라 🔄",
        "💬 *The Man from Earth* (2007) – 말로만 우주급 과학 토론 🗣️",
        "🔬 *Limitless* (2011) – 두뇌 풀가동 영화 ⚡"
    ],
    "ISTJ": [
        "📊 *The Theory of Everything* (2014) – 스티븐 호킹의 이야기 🪐",
        "🔍 *Hidden Figures* (2016) – 책임감 있는 계산과 성과 🚀",
        "📘 *October Sky* (1999) – 꿈을 향한 확고한 열정 🚀"
    ],
    # ...원하면 더 추가 가능!
}

# 💡 유효한 MBTI인지 확인
valid_mbtis = mbti_movies.keys()

if mbti:
    if mbti in valid_mbtis:
        st.success(f"🎉 {mbti} 유형을 위한 추천 명작 3편! 🍿")
        for movie in mbti_movies[mbti]:
            st.markdown(f"- {movie}")
        st.balloons()  # 🎈 풍선 효과!
    else:
        st.error("😢 유효한 MBTI를 입력해주세요 (예: INTP, ENFP 등)")
