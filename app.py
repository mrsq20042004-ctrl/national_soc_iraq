import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

st.set_page_config(page_title="National SOC - IRAQ", layout="wide")
st.title("🛡️ National SOC - IRAQ")
st.markdown("**غرفة عمليات الأمن السيبراني | وزارة الاتصالات - العراق** | الحالة: 🟢 ACTIVE")
st.markdown("---")

if st.button("🔍 افحص الشبكة الآن", type="primary"):
    normal = np.random.normal(loc=[20, 5000, 2], scale=[5, 1000, 1], size=(200, 3))
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(normal)

    tests = [
        ("وزارة النفط", 22, 5200, 2, "192.168.1.10"),
        ("وزارة الصحة", 18, 4800, 1, "192.168.1.11"),
        ("وزارة الداخلية", 1500, 8000, 3, "45.12.88.9"),
        ("وزارة الدفاع", 25, 5000000, 2, "103.45.22.7"),
        ("وزارة المالية", 20, 5000, 80, "91.33.77.5"),
    ]

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 نتائج الفحص")
        for name, req, byt, port, ip in tests:
            pred = model.predict([[req, byt, port]])[0]
            if pred == -1:
                st.error(f"🚨 {name} | هجوم! | IP: {ip} | تم الحظر ⛔")
            else:
                st.success(f"🟢 {name} | آمنة | IP: {ip}")
    with col2:
        st.subheader("📈 هجمات اليوم")
        df = pd.DataFrame({"النوع": ["DDoS","Brute Force","Port Scan","Data Leak","Phishing"], "العدد": [42,28,35,12,30]})
        st.bar_chart(df.set_index("النوع"))
        st.metric("مجموع الهجمات اليوم", "147")
        st.metric("تم حظر", "3 مهاجمين")

st.info("نسخة تجريبية للعرض - National SOC Iraq v1.0 | تطوير: حسين البياتي")
