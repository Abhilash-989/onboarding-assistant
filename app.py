import streamlit as st

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Onboarding Assistant",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ───────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

.main { background-color: #F0F2F8; }

.tile {
    background: white;
    border-radius: 14px;
    padding: 20px;
    border: 1px solid #E2E6F0;
    margin-bottom: 14px;
    transition: all 0.2s;
    cursor: pointer;
}
.tile:hover { border-color: #4B5FFA; box-shadow: 0 8px 24px rgba(0,0,0,0.08); }
.tile-done { border-color: #00C48C !important; background: #E6FAF5 !important; }
.tile-inprog { border-color: #FF9500 !important; background: #FFF4E0 !important; }

.badge-todo    { background:#F7F8FC; color:#9AA0BC; padding:3px 10px; border-radius:20px; font-size:12px; border:1px solid #E2E6F0; }
.badge-inprog  { background:#FFF4E0; color:#FF9500; padding:3px 10px; border-radius:20px; font-size:12px; }
.badge-done    { background:#E6FAF5; color:#00C48C; padding:3px 10px; border-radius:20px; font-size:12px; }

.metric-card {
    background: white;
    border-radius: 12px;
    padding: 16px 20px;
    border: 1px solid #E2E6F0;
    text-align: center;
}
.metric-val { font-size: 28px; font-weight: 600; }
.metric-lbl { font-size: 12px; color: #5A6080; margin-top: 2px; }

.section-header {
    font-size: 11px; font-weight: 600;
    color: #9AA0BC; letter-spacing: 0.06em;
    text-transform: uppercase; margin: 20px 0 12px;
}
.detail-box {
    background: white; border-radius: 14px;
    padding: 24px; border: 1px solid #E2E6F0;
    margin-bottom: 16px;
}
.step-num {
    background: #EEF0FF; color: #4B5FFA;
    border-radius: 50%; width: 24px; height: 24px;
    display: inline-flex; align-items: center;
    justify-content: center; font-size: 11px;
    font-weight: 600; margin-right: 8px;
}
</style>
""", unsafe_allow_html=True)

# ── Data ─────────────────────────────────────────────────────
TILES = [
    {
        "id": "security",
        "icon": "🛡️",
        "title": "Security Guidelines",
        "desc": "BHP & Accenture security rules",
        "time": "10 min read",
        "priority": "Mandatory",
        "steps": [
            "**DO NOT** forward any BHP emails or files to Accenture systems",
            "**NEVER** click suspicious links — report phishing via Cofense Report button in BHP mailbox",
            "Complete ALL BHP Cybersecurity Trainings within the stipulated timeframe",
            "**DO NOT** use GenAI tools (Gemini, Perplexity, DeepSeek) in BHP environment",
            "Before every action ask yourself: *'Is this needed to perform my job?'* If No — don't do it",
            "**DO NOT** transfer BHP data outside BHP environment without BHP Line Manager approval",
        ]
    },
    {
        "id": "avd",
        "icon": "💻",
        "title": "AVD Setup",
        "desc": "3 ways to access Azure Virtual Desktop",
        "time": "15 min setup",
        "priority": "Mandatory",
        "steps": [
            "**Method 1 (Recommended) — Windows App:** Download from Microsoft Store → Sign out of Accenture account → Sign in with BHP credentials → Double-click AVD icon",
            "**Method 2 — Web Browser:** Go to [windows.cloud.microsoft](https://windows.cloud.microsoft) → Sign in with BHP credentials → Access AVD directly",
            "**Method 3 — Windows Desktop Client:** Same steps as Windows App",
            "⚠️ First launch often times out — click Refresh and retry after 1 hour",
            "**Password reset / account unlock:** Go to [sspr.bhp.com](https://sspr.bhp.com) in Incognito window",
        ]
    },
    {
        "id": "troubleshoot",
        "icon": "🔧",
        "title": "AVD Troubleshooting",
        "desc": "Fixes for 5 common AVD issues",
        "time": "Reference",
        "priority": "Reference",
        "steps": [
            "**Black screen after login:** Press Ctrl+Shift+Esc → Task Manager → File → Run new task → type `explorer.exe`",
            "**Remote Desktop error:** Open Remote Desktop → 3 dots → About → Reset → Continue → Subscribe with BHP credentials",
            "**Can't click icons:** Restart your machine",
            "**Password expired:** Open sspr.bhp.com in Incognito → Registration for self-service password reset → Change password",
            "**Random pop-up errors:** Restart machine and click Refresh",
            "**Still stuck?** Raise an incident via BHP ServiceNow portal",
        ]
    },
    {
        "id": "access",
        "icon": "🔑",
        "title": "Access Requests",
        "desc": "Raise system access via ServiceNow",
        "time": "30 min task",
        "priority": "Mandatory",
        "steps": [
            "Open the reference tracker to see which requests to raise — check the **Generic Tab** in the Excel sheet shared by your lead",
            "Go to [bhp.service-now.com](https://bhp.service-now.com/sp?id=bhp_home)",
            "Search the **Request Name** from the tracker in the ServiceNow search bar",
            "Open the sample request to understand the format, then raise the **same request for yourself**",
            "Raise all requests as soon as you have your BHP_ID and ServiceNow access",
            "For help contact **Ravi Saravanan** (saravanan.f.ravi@accenture.com) or **D.B. Venkateswarlu** (d.b.venkateswarlu@accenture.com)",
        ]
    },
    {
        "id": "dbt",
        "icon": "📊",
        "title": "DBT Learning",
        "desc": "Learn Analytics Engineering with dbt",
        "time": "Self-paced",
        "priority": "Required",
        "steps": [
            "Go to [courses.getdbt.com](https://courses.getdbt.com/collections) — the course is free",
            "Complete **Analytics Engineering with dbt** — this is essential for the Data Engineering team",
            "Take notes as you go — you'll use these concepts from day one",
            "Mark this tile complete once you've finished the core modules",
        ]
    },
    {
        "id": "tools",
        "icon": "🛠️",
        "title": "Tools & Laptop",
        "desc": "Webex setup, laptop replacement guide",
        "time": "As needed",
        "priority": "Reference",
        "steps": [
            "**Webex (for client calls):** Install on your Accenture laptop directly — NOT inside AVD. Download from [webex.com](https://www.webex.com) or raise a Technology Support ticket if no admin rights",
            "**Laptop replacement Step 1:** Raise Technology Support incident → get ticket number → raise Asset Decommission Request",
            "**Laptop replacement Step 2:** Go to Accenture India Info Survey → select 'System replacement – Accenture Shared laptop' → complete all steps",
            "⚠️ Enable a temp password for your Accenture account before the swap — otherwise you won't be able to log into the new laptop",
        ]
    },
]

# ── Session state ─────────────────────────────────────────────
if "completed" not in st.session_state:
    st.session_state.completed = set()
if "inprog" not in st.session_state:
    st.session_state.inprog = set()
if "current_tile" not in st.session_state:
    st.session_state.current_tile = None

def get_status(tile_id):
    if tile_id in st.session_state.completed:
        return "done"
    if tile_id in st.session_state.inprog:
        return "inprog"
    return "todo"

def get_badge(status):
    if status == "done":   return '<span class="badge-done">✓ Done</span>'
    if status == "inprog": return '<span class="badge-inprog">● In Progress</span>'
    return '<span class="badge-todo">○ Not Started</span>'

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🚀 Onboarding Assistant")
    st.markdown("**DataEng Team** · BHP")
    st.divider()

    total = len(TILES)
    done_count = len(st.session_state.completed)
    pct = int((done_count / total) * 100)

    st.markdown(f"**Your progress**")
    st.progress(pct / 100)
    st.markdown(f"**{pct}%** complete · {done_count}/{total} topics done")
    st.divider()

    page = st.radio("Navigate", ["🏠 Home", "📋 My Journey", "👥 Admin View"], label_visibility="collapsed")

    st.divider()
    st.markdown('<p style="font-size:11px;color:#9AA0BC">Need help? Ask your buddy or raise a ServiceNow ticket</p>', unsafe_allow_html=True)

# ── HOME VIEW ─────────────────────────────────────────────────
if page == "🏠 Home":

    # If a tile is open show detail view
    if st.session_state.current_tile:
        tile = next(t for t in TILES if t["id"] == st.session_state.current_tile)
        status = get_status(tile["id"])

        if st.button("← Back to home"):
            st.session_state.current_tile = None
            st.rerun()

        st.markdown(f"## {tile['icon']} {tile['title']}")
        col1, col2, col3 = st.columns([2,1,1])
        with col1:
            st.markdown(f"*{tile['desc']}*")
        with col2:
            st.markdown(f"⏱️ {tile['time']}")
        with col3:
            priority_color = "#FF4D6A" if tile["priority"] == "Mandatory" else "#4B5FFA"
            st.markdown(f'<span style="color:{priority_color};font-weight:600">{tile["priority"]}</span>', unsafe_allow_html=True)

        st.divider()

        st.markdown('<div class="section-header">Steps to complete</div>', unsafe_allow_html=True)
        for i, step in enumerate(tile["steps"], 1):
            st.markdown(f'<span class="step-num">{i}</span> {step}', unsafe_allow_html=True)
            if i < len(tile["steps"]):
                st.markdown('<hr style="border:none;border-top:1px solid #F0F2F8;margin:8px 0">', unsafe_allow_html=True)

        st.divider()

        col_a, col_b, col_c = st.columns([1,1,2])
        with col_a:
            if status != "done":
                if st.button("✅ Mark as Complete", type="primary", use_container_width=True):
                    st.session_state.completed.add(tile["id"])
                    st.session_state.inprog.discard(tile["id"])
                    st.success("Great job! Tile marked as complete 🎉")
                    st.rerun()
            else:
                st.success("✓ Completed!")
        with col_b:
            if status == "todo":
                if st.button("▶ Mark In Progress", use_container_width=True):
                    st.session_state.inprog.add(tile["id"])
                    st.rerun()

    else:
        # Home screen
        st.markdown("## 👋 Welcome to your Onboarding Journey")
        st.markdown("Complete all tiles to finish your onboarding. Click any tile to get started.")
        st.divider()

        # Metrics row
        done_count = len(st.session_state.completed)
        inprog_count = len(st.session_state.inprog)
        todo_count = total - done_count - inprog_count
        pct = int((done_count / total) * 100)

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f'<div class="metric-card"><div class="metric-val" style="color:#4B5FFA">{pct}%</div><div class="metric-lbl">Overall progress</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="metric-card"><div class="metric-val" style="color:#00C48C">{done_count}</div><div class="metric-lbl">Completed</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<div class="metric-card"><div class="metric-val" style="color:#FF9500">{inprog_count}</div><div class="metric-lbl">In Progress</div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown(f'<div class="metric-card"><div class="metric-val" style="color:#9AA0BC">{todo_count}</div><div class="metric-lbl">Not Started</div></div>', unsafe_allow_html=True)

        st.markdown('<div class="section-header" style="margin-top:24px">YOUR ONBOARDING TILES</div>', unsafe_allow_html=True)

        # Tiles grid — 3 per row
        for row in range(0, len(TILES), 3):
            cols = st.columns(3)
            for col_idx, col in enumerate(cols):
                tile_idx = row + col_idx
                if tile_idx < len(TILES):
                    tile = TILES[tile_idx]
                    status = get_status(tile["id"])
                    tile_class = "tile-done" if status == "done" else ("tile-inprog" if status == "inprog" else "")
                    with col:
                        st.markdown(f"""
                        <div class="tile {tile_class}">
                            <div style="font-size:28px;margin-bottom:8px">{tile['icon']}</div>
                            <div style="font-size:14px;font-weight:600;margin-bottom:4px">{tile['title']}</div>
                            <div style="font-size:12px;color:#5A6080;margin-bottom:12px">{tile['desc']}</div>
                            <div style="display:flex;justify-content:space-between;align-items:center">
                                {get_badge(status)}
                                <span style="color:#9AA0BC;font-size:12px">{tile['time']}</span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        if st.button(f"Open →", key=f"open_{tile['id']}"):
                            st.session_state.current_tile = tile["id"]
                            st.rerun()

# ── JOURNEY VIEW ──────────────────────────────────────────────
elif page == "📋 My Journey":
    st.markdown("## 📋 My Onboarding Journey")
    st.markdown("Your full checklist — track everything in one place.")
    st.divider()

    for tile in TILES:
        status = get_status(tile["id"])
        icon_map = {"done": "✅", "inprog": "🔄", "todo": "⬜"}
        col1, col2, col3, col4 = st.columns([0.5, 3, 1.5, 1])
        with col1:
            st.markdown(f"### {icon_map[status]}")
        with col2:
            st.markdown(f"**{tile['icon']} {tile['title']}**")
            st.caption(tile["desc"])
        with col3:
            st.markdown(f'<div style="padding-top:8px">{get_badge(status)}</div>', unsafe_allow_html=True)
        with col4:
            if st.button("Open", key=f"journey_{tile['id']}"):
                st.session_state.current_tile = tile["id"]
                page = "🏠 Home"
                st.rerun()
        st.divider()

# ── ADMIN VIEW ────────────────────────────────────────────────
elif page == "👥 Admin View":
    st.markdown("## 👥 New Joiner Tracker")
    st.markdown("Admin overview — track all joiners progress.")
    st.divider()

    import pandas as pd
    data = {
        "Name": ["Alex J.", "Priya M.", "Sam K.", "Ravi S.", "Neha T."],
        "Team": ["DataEng", "Finance", "DataEng", "Engineering", "DataEng"],
        "Day": [5, 8, 12, 3, 15],
        "Completed": [3, 1, 5, 0, 6],
        "Status": ["On Track", "Behind", "On Track", "Just Started", "Complete"]
    }
    df = pd.DataFrame(data)
    df["Progress"] = (df["Completed"] / 6 * 100).astype(int).astype(str) + "%"

    st.dataframe(df, use_container_width=True, hide_index=True)

    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Active Joiners", "5")
    with col2:
        st.metric("On Track", "3", delta="↑ good")
    with col3:
        st.metric("Behind Schedule", "1", delta="needs attention", delta_color="inverse")
