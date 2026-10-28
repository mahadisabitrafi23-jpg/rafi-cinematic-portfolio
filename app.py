from importlib import import_module
from pathlib import Path

try:
  st = import_module("streamlit")
except ModuleNotFoundError as exc:
  if exc.name != "streamlit":
    raise
  raise SystemExit(
    "Streamlit is not installed. Install it with `python -m pip install streamlit`."
  ) from exc

# ------------------------------------------------------------
# RAFI — CINEMATIC EDITORIAL PORTFOLIO
# Built with Python + Streamlit
# Run locally: python -m streamlit run app.py
# ------------------------------------------------------------

st.set_page_config(
    page_title="Mahadi Sabit Rafi — Selected Work",
    page_icon="◒",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Edit these details to personalize your site.
NAME = "Mahadi Sabit Rafi"
ROLE = "INDEPENDENT ARTIST & INNOVATOR"
CURRENTLY = "STUDENT · DEVELOPER IN PROGRESS · LYRIC WRITER"
EMAIL = "hello@example.com"  # Replace with your real email.
LOCATION = "Dhaka, Bangladesh"
INTRO = "An unfinished story. An uncommon mind."

# Add your portrait at assets/profile.jpg (inside this project folder).
PROFILE_IMAGE = Path(__file__).parent / "assets" / "profile.jpg"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap');

:root {
  --bg: #10100f;
  --panel: #171715;
  --paper: #e9e4d9;
  --muted: #a6a196;
  --line: #383730;
  --olive: #a4aa88;
}
.stApp { background: var(--bg); color: var(--paper); }
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.block-container { max-width: 1180px; padding-top: 1.7rem; padding-bottom: 4rem; }
h1,h2,h3 { color: var(--paper) !important; }
a { color: var(--olive) !important; }
p { line-height: 1.8; }
div[data-testid="stToolbar"], #MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }
div[data-testid="stVerticalBlock"] > div { gap: .75rem; }

.mono { font-family:'DM Mono', monospace; text-transform:uppercase; letter-spacing:.13em; font-size:.68rem; color:var(--muted); }
.topbar { display:flex; align-items:center; justify-content:space-between; padding:10px 0 22px; border-bottom:1px solid var(--line); }
.wordmark { font-family:'Playfair Display',serif; font-size:1.5rem; letter-spacing:-.04em; color:var(--paper); }
.wordmark span { color:var(--olive); }
.topright { font-family:'DM Mono',monospace; font-size:.68rem; letter-spacing:.1em; color:var(--muted); }
.kicker { font-family:'DM Mono',monospace; color:var(--olive); font-size:.72rem; letter-spacing:.16em; text-transform:uppercase; }
.hero { padding:80px 0 58px; }
.hero h1 { font-family:'Playfair Display',serif !important; font-weight:400 !important; font-size:clamp(3.6rem,9vw,8rem) !important; letter-spacing:-.065em !important; line-height:.91 !important; margin:20px 0 26px !important; }
.hero h1 em { color:var(--olive); font-weight:400; }
.hero-copy { color:#c2bdb2; font-size:1.05rem; max-width:680px; }
.hero-subtitle { font-family:'Playfair Display',serif; color:var(--olive); font-size:clamp(1.25rem,2.4vw,2rem); margin:0 0 18px; }
.about-quote { font-family:'Playfair Display',serif; color:var(--paper); font-size:1.25rem; font-style:italic; margin-top:20px; }
.hero-meta { border-left:1px solid var(--line); padding:15px 0 15px 22px; margin-top:25px; }
.hero-meta strong { color:var(--paper); font-weight:500; }
.rule { border:0; border-top:1px solid var(--line); margin:26px 0; }
.section-head { display:flex; justify-content:space-between; align-items:baseline; gap:20px; padding:32px 0 20px; border-top:1px solid var(--line); }
.section-head h2 { font-family:'Playfair Display',serif !important; font-size:2.6rem !important; font-weight:400 !important; letter-spacing:-.045em; margin:0; }
.section-number { font-family:'DM Mono',monospace; font-size:.72rem; color:var(--olive); letter-spacing:.12em; }
.project-card { border:1px solid var(--line); background:linear-gradient(145deg,#1b1b18,#131311); padding:25px; min-height:255px; border-radius:2px; }
.project-card .num { font-family:'DM Mono',monospace; color:var(--olive); font-size:.68rem; letter-spacing:.15em; }
.project-card h3 { font-family:'Playfair Display',serif !important; font-size:1.7rem !important; font-weight:400 !important; margin:25px 0 12px; }
.project-card p { color:var(--muted); font-size:.93rem; }
.tag { display:inline-block; border:1px solid #49483e; color:#c6c1b5; padding:6px 9px; margin:8px 5px 0 0; font-family:'DM Mono',monospace; font-size:.62rem; letter-spacing:.05em; }
.statement { font-family:'Playfair Display',serif; font-size:clamp(1.7rem,3.6vw,3rem); line-height:1.32; letter-spacing:-.035em; color:var(--paper); }
.statement em { color:var(--olive); font-weight:400; }
.about-copy { color:#b9b3a8; max-width:620px; }
.about-photo-note { color:var(--muted); font-family:'DM Mono',monospace; font-size:.68rem; letter-spacing:.08em; text-transform:uppercase; text-align:center; padding-top:10px; }
div[data-testid="stImage"] img { border-radius:2px; filter:grayscale(12%); }
.about-photo-placeholder { min-height:390px; height:100%; display:flex; flex-direction:column; justify-content:space-between; padding:22px; border:1px solid var(--line); background:linear-gradient(145deg,#24241f,#151512); color:var(--muted); font-family:'DM Mono',monospace; font-size:.7rem; letter-spacing:.1em; }
.about-photo-placeholder .placeholder-mark { font-family:'Playfair Display',serif; font-size:5rem; color:var(--olive); line-height:1; align-self:center; margin:auto 0; }
.skill-row { padding:14px 0; border-bottom:1px solid var(--line); display:flex; justify-content:space-between; gap:20px; }
.skill-row span:first-child { color:var(--paper); }
.skill-row span:last-child { font-family:'DM Mono',monospace; color:var(--muted); font-size:.7rem; text-align:right; }
.contact { border:1px solid var(--line); background:#dcd5c6; color:#171713; padding:clamp(25px,5vw,55px); margin-top:10px; }
.contact h2 { color:#171713 !important; font-family:'Playfair Display',serif !important; font-size:clamp(2.6rem,6vw,5rem) !important; font-weight:400 !important; letter-spacing:-.06em; line-height:1; }
.contact p { color:#555247; max-width:520px; }
.contact a { color:#171713 !important; text-decoration:none; border-bottom:1px solid #777363; padding-bottom:4px; }
.footer { display:flex; justify-content:space-between; gap:15px; padding-top:22px; color:#777469; font-family:'DM Mono',monospace; font-size:.65rem; letter-spacing:.06em; }
.stButton button, .stLinkButton a { border-radius:0 !important; border:1px solid var(--olive) !important; background:var(--olive) !important; color:#151510 !important; font-family:'DM Mono',monospace !important; text-transform:uppercase; letter-spacing:.08em; font-size:.72rem !important; padding: .8rem 1.1rem !important; }
.stLinkButton a:hover { background:transparent !important; color:var(--paper) !important; }
@media(max-width:700px) {
 .block-container { padding-left:1.1rem; padding-right:1.1rem; }
 .hero { padding:55px 0 35px; }
 .topright { display:none; }
 .section-head h2 { font-size:2.1rem !important; }
 .footer { flex-direction:column; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
  <div class="wordmark">Mahadi Sabit Rafi<span>.</span></div>
  <div class="topright">INDEPENDENT MIND · DHAKA, BD</div>
</div>
""", unsafe_allow_html=True)

# HERO — portrait appears at the top of the homepage, beside the main introduction
hero_photo, hero_intro = st.columns([0.72, 1.28], gap="large", vertical_alignment="center")
with hero_photo:
    if PROFILE_IMAGE.is_file():
        st.image(str(PROFILE_IMAGE), use_container_width=True)
        st.markdown('<div class="about-photo-note">MAHADI SABIT RAFI · PORTRAIT</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="about-photo-placeholder" style="min-height:420px;">
          <span>PORTRAIT / 01</span>
          <span class="placeholder-mark">r.</span>
          <span>ADD YOUR PHOTO TO<br>assets/profile.jpg</span>
        </div>
        """, unsafe_allow_html=True)
with hero_intro:
    st.markdown(f"""
    <div class="hero" style="padding:35px 0 25px;">
      <div class="kicker">Independent Mind · Dhaka, BD</div>
      <h1>Mahadi Sabit<br><em>Rafi.</em></h1>
      <p class="hero-subtitle">An unfinished story. An uncommon mind.</p>
      <p class="hero-copy">Drawn to the obscure, driven by the impossible.</p>
    </div>
    """, unsafe_allow_html=True)

hero_left, hero_right = st.columns([1.3, .7], gap="large")
with hero_left:
    st.link_button("LET'S CONNECT ↗", f"mailto:{EMAIL}")
with hero_right:
    st.markdown(f"""
    <div class="hero-meta">
      <div class="mono">IDENTITY</div>
      <p><strong>{ROLE}</strong></p>
      <div class="mono">CURRENTLY</div>
      <p><strong>{CURRENTLY}</strong></p>
      <div class="mono">BASED IN</div>
      <p><strong>{LOCATION}</strong></p>
    </div>
    """, unsafe_allow_html=True)

# ABOUT
st.markdown("""
<div class="section-head">
  <h2>Not just a job title.</h2>
  <div class="section-number">01 — ABOUT</div>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="statement">An unfinished story.<br><em>An uncommon mind.</em></div>
<div style="height:18px;"></div>
<p class="about-copy">Drawn to the obscure, driven by the impossible.</p>
<p class="about-copy">I exist somewhere between art and innovation, where unconventional ideas meet quiet ambition. Music, technology, and the beauty of things that don't need to be understood by everyone — that's my world.</p>
<p class="about-copy">I don't chase attention. I build things worth noticing.</p>
<p class="about-copy">Still evolving. Always observing. Never revealing the whole picture.</p>
<p class="about-quote">Some things are better left unexplained.</p>
""", unsafe_allow_html=True)

# SELECTED WORK
st.markdown("""
<div class="section-head">
  <h2>Selected explorations.</h2>
  <div class="section-number">02 — WORK</div>
</div>
""", unsafe_allow_html=True)
st.caption("Starter examples — replace these with real projects and links before presenting the site professionally.")
c1, c2 = st.columns(2, gap="medium")
with c1:
    st.markdown("""
    <div class="project-card">
      <div class="num">01 / CODE &amp; LEARNING</div>
      <h3>Small tools, real lessons.</h3>
      <p>A collection of Python exercises and beginner projects built to turn concepts into practical skills.</p>
      <span class="tag">PYTHON</span><span class="tag">PROBLEM SOLVING</span>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="project-card">
      <div class="num">02 / SOUND &amp; CULTURE</div>
      <h3>Nocturn Sessions.</h3>
      <p>A creative outlet exploring music, mood, society, and the visual language around sound.</p>
      <span class="tag">MUSIC</span><span class="tag">ART DIRECTION</span>
    </div>
    """, unsafe_allow_html=True)
c3, c4 = st.columns(2, gap="medium")
with c3:
    st.markdown("""
    <div class="project-card">
      <div class="num">03 / VISUAL EXPERIMENTS</div>
      <h3>Design in progress.</h3>
      <p>Posters, visual concepts, and experiments with atmosphere, typography, and storytelling.</p>
      <span class="tag">DESIGN</span><span class="tag">VISUAL STORYTELLING</span>
    </div>
    """, unsafe_allow_html=True)
with c4:
    st.markdown("""
    <div class="project-card">
      <div class="num">04 / NEXT CHAPTER</div>
      <h3>Something new is forming.</h3>
      <p>A space reserved for the next project — built with intention, documented with honesty.</p>
      <span class="tag">EXPERIMENT</span><span class="tag">COMING SOON</span>
    </div>
    """, unsafe_allow_html=True)

# SKILLS
st.markdown("""
<div class="section-head">
  <h2>Tools &amp; interests.</h2>
  <div class="section-number">03 — PRACTICE</div>
</div>
""", unsafe_allow_html=True)
skills_left, skills_right = st.columns(2, gap="large")
with skills_left:
    st.markdown("""
    <div class="skill-row"><span>Python &amp; creative coding</span><span>LEARNING</span></div>
    <div class="skill-row"><span>Visual design &amp; art direction</span><span>EXPLORING</span></div>
    <div class="skill-row"><span>Digital storytelling</span><span>EXPLORING</span></div>
    """, unsafe_allow_html=True)
with skills_right:
    st.markdown("""
    <div class="skill-row"><span>Lyrics &amp; songwriting</span><span>IN PROGRESS</span></div>
    <div class="skill-row"><span>Car enthusiast</span><span>PASSION</span></div>
    <div class="skill-row"><span>Learning about perfumes</span><span>EXPLORING</span></div>
    """, unsafe_allow_html=True)

# CONTACT
st.markdown("""
<div class="section-head">
  <h2>Open to good ideas.</h2>
  <div class="section-number">04 — CONTACT</div>
</div>
""", unsafe_allow_html=True)
st.markdown(f"""
<div class="contact">
  <div class="mono" style="color:#686456;">HAVE SOMETHING IN MIND?</div>
  <h2>Let's make<br>it meaningful.</h2>
  <p>For collaborations, creative conversations, or a project worth exploring, send me a message.</p>
  <p><a href="mailto:{EMAIL}">WRITE AN EMAIL ↗</a></p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="footer">
  <div>© 2026 {NAME.upper()}</div>
  <div>BUILT WITH PYTHON · STILL BECOMING</div>
  <div>{LOCATION.upper()}</div>
</div>
""", unsafe_allow_html=True)
