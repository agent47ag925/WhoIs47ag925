# streamlit_resume.py

import streamlit as st
from streamlit.components.v1 import html

# Streamlit 페이지 설정
st.set_page_config(
    page_title="John Anderson - Resume",
    page_icon="👨‍💻",
    layout="wide",
)

# HTML 코드 (CSS 포함)
HTML_CONTENT = """
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<div class="resume-wrapper">
    <section class="profile section-padding">
        <div class="container">
            <div class="picture-resume-wrapper">
        <div class="picture-resume">
        <span><img src="https://s3.amazonaws.com/uifaces/faces/twitter/jsa/128.jpg" alt="" /></span>
        <svg version="1.1" viewBox="0 0 350 350">
  
  <defs>
    <filter id="goo">
      <feGaussianBlur in="SourceGraphic" stdDeviation="8" result="blur" />
      <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 21 -9" result="cm" />
    </filter>
  </defs>
  
<g filter="url(#goo)">  
  <circle id="main_circle" class="st0" cx="171.5" cy="175.6" r="130"/>
  <circle id="circle" class="bubble0 st1" cx="171.5" cy="175.6" r="122.7"/>
  <circle id="circle" class="bubble1 st1" cx="171.5" cy="175.6" r="122.7"/>
  <circle id="circle" class="bubble2 st1" cx="171.5" cy="175.6" r="122.7"/>
  <circle id="circle" class="bubble3 st1" cx="171.5" cy="175.6" r="122.7"/>
  <circle id="circle" class="bubble4 st1" cx="171.5" cy="175.6" r="122.7"/>
  <circle id="circle" class="bubble5 st1" cx="171.5" cy="175.6" r="122.7"/>
  <circle id="circle" class="bubble6 st1" cx="171.5" cy="175.6" r="122.7"/>
  <circle id="circle" class="bubble7 st1" cx="171.5" cy="175.6" r="122.7"/>
  <circle id="circle" class="bubble8 st1" cx="171.5" cy="175.6" r="122.7"/>
  <circle id="circle" class="bubble9 st1" cx="171.5" cy="175.6" r="122.7"/>
  <circle id="circle" class="bubble10 st1" cx="171.5" cy="175.6" r="122.7"/>
</g>  
</svg>
      </div>
         <div class="clearfix"></div>
 </div>
      <div class="name-wrapper">
        <h1>John <br/>Anderson</h1>
      </div>
      <div class="clearfix"></div>
      <div class="contact-info clearfix">
        <ul class="list-titles">
            <li>Call</li>
            <li>Mail</li>
            <li>Web</li>
            <li>Home</li>
        </ul>
        <ul class="list-content">
            <li>+34 123 456 789</li>
            <li>j.anderson@gmail.com</li>
            <li><a href="#">janderson.com</a></li>
            <li>Los Angeles, CA</li>
        </ul>
      </div>
      <div class="contact-presentation">
        <p><span class="bold">Lorem</span> ipsum dolor sit amet, consectetur adipiscing elit.</p>
      </div>
        </div>
    </section>
  
  <section class="experience section-padding">
    <div class="container">
        <h3 class="experience-title">Experience</h3>
      <div class="experience-wrapper">
        <div class="company-wrapper clearfix">
            <div class="experience-title">Company name</div>
          <div class="time">Nov 2012 - Present</div>
        </div>
        <div class="job-wrapper clearfix">
            <div class="experience-title">Front End Developer </div>
          <div class="company-description">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>
"""

# HTML/CSS 콘텐츠를 Streamlit 앱에 렌더링
st.markdown(
    """
    <style>
    /* 사용자 정의 CSS 스타일 */
    .resume-wrapper {
        font-family: Arial, sans-serif;
        color: #333;
        margin: 0 auto;
        padding: 20px;
    }
    .section-padding {
        padding: 20px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# HTML 콘텐츠 삽입
html(HTML_CONTENT, height=800)

# 끝
