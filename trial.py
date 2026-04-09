import streamlit as st
import random

# Page configuration
st.set_page_config(
    page_title="AI Environmental Decision Intelligence Platform",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern dark theme styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding: 1rem;
    }
    
    /* Card styling */
    .metric-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 15px;
        padding: 1.5rem;
        border: 1px solid #0f3460;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        margin-bottom: 1rem;
    }
    
    .card-header {
        color: #00d4ff;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .aqi-display {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .aqi-good { background: linear-gradient(135deg, #00c853, #69f0ae); color: #000; }
    .aqi-moderate { background: linear-gradient(135deg, #ffd600, #ffff00); color: #000; }
    .aqi-unhealthy { background: linear-gradient(135deg, #ff6d00, #ff9100); color: #000; }
    .aqi-hazardous { background: linear-gradient(135deg, #d50000, #ff1744); color: #fff; }
    
    .route-card {
        background: linear-gradient(135deg, #0d7377 0%, #14ffec 100%);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        color: #000;
    }
    
    .eco-route-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        color: #000;
    }
    
    .action-item {
        background: rgba(0, 212, 255, 0.1);
        border-left: 4px solid #00d4ff;
        padding: 0.75rem;
        margin: 0.5rem 0;
        border-radius: 0 8px 8px 0;
    }
    
    .exposure-meter {
        height: 20px;
        border-radius: 10px;
        background: linear-gradient(90deg, #00c853 0%, #ffd600 50%, #ff6d00 75%, #d50000 100%);
        position: relative;
        margin: 1rem 0;
    }
    
    .header-gradient {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    
    .stSlider > div > div {
        background-color: #00d4ff;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'optimized' not in st.session_state:
    st.session_state.optimized = False
if 'optimization_results' not in st.session_state:
    st.session_state.optimization_results = None

# Sidebar Inputs
with st.sidebar:
    st.markdown("## 🎛️ Control Panel")
    st.markdown("---")
    
    st.markdown("### 🚗 Traffic Parameters")
    traffic_level = st.slider(
        "Traffic Level",
        min_value=0,
        max_value=100,
        value=50,
        help="Current traffic congestion level"
    )
    
    st.markdown("### 🌳 Environmental Factors")
    green_cover = st.slider(
        "Green Cover %",
        min_value=0,
        max_value=100,
        value=30,
        help="Percentage of green coverage in the area"
    )
    
    st.markdown("### ⏱️ Exposure Duration")
    time_outside = st.slider(
        "Time Outside (hours)",
        min_value=0.0,
        max_value=24.0,
        value=2.0,
        step=0.5,
        help="Expected time spent outdoors"
    )
    
    st.markdown("---")
    st.markdown("### 📍 Route Planning")
    source = st.text_input("Source Location", placeholder="Enter starting point")
    destination = st.text_input("Destination", placeholder="Enter destination")
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.info("This platform uses AI to predict air quality and optimize environmental decisions for healthier mobility choices.")

# Helper Functions
def calculate_aqi(traffic, green):
    """Calculate AQI based on traffic and green cover"""
    base_aqi = 50
    traffic_impact = traffic * 1.5
    green_benefit = green * 0.8
    aqi = base_aqi + traffic_impact - green_benefit
    return max(0, min(500, int(aqi)))

def get_aqi_category(aqi):
    """Get AQI category and styling"""
    if aqi <= 50:
        return "Good", "aqi-good", "🟢"
    elif aqi <= 100:
        return "Moderate", "aqi-moderate", "🟡"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups", "aqi-unhealthy", "🟠"
    elif aqi <= 200:
        return "Unhealthy", "aqi-unhealthy", "🔴"
    else:
        return "Hazardous", "aqi-hazardous", "🟣"

def calculate_exposure_score(aqi, hours):
    """Calculate personal exposure score"""
    base_score = 100
    exposure = (aqi / 500) * hours * 10
    score = max(0, base_score - exposure)
    return round(score, 1)

def generate_route_data(source, destination):
    """Generate route information"""
    if source and destination:
        base_distance = random.randint(5, 25)
        return {
            "fastest": {
                "distance": base_distance,
                "time": int(base_distance * 2.5),
                "aqi_exposure": random.randint(80, 150)
            },
            "eco": {
                "distance": base_distance + random.randint(1, 5),
                "time": int(base_distance * 3.2),
                "aqi_exposure": random.randint(40, 80)
            }
        }
    return None

def generate_optimization_suggestions(traffic, green, aqi):
    """Generate optimization suggestions"""
    suggestions = []
    
    if traffic > 60:
        reduction_needed = traffic - 40
        suggestions.append({
            "icon": "🚗",
            "title": "Reduce Traffic Congestion",
            "description": f"Decrease traffic level by {reduction_needed}% through carpooling or public transit",
            "impact": f"Could reduce AQI by ~{int(reduction_needed * 1.2)} points"
        })
    
    if green < 40:
        increase_needed = 40 - green
        suggestions.append({
            "icon": "🌳",
            "title": "Increase Green Cover",
            "description": f"Plant more trees to increase green cover by {increase_needed}%",
            "impact": f"Could reduce AQI by ~{int(increase_needed * 0.6)} points"
        })
    
    if aqi > 100:
        suggestions.append({
            "icon": "😷",
            "title": "Personal Protection",
            "description": "Use N95 masks when outdoors during peak pollution hours",
            "impact": "Reduces personal exposure by up to 95%"
        })
    
    if aqi > 80:
        suggestions.append({
            "icon": "⏰",
            "title": "Time Optimization",
            "description": "Schedule outdoor activities during early morning (5-7 AM)",
            "impact": "Typically 30-40% lower pollution levels"
        })
    
    suggestions.append({
        "icon": "🚴",
        "title": "Active Transportation",
        "description": "Use cycling or walking for short distances on green routes",
        "impact": "Zero emissions + health benefits"
    })
    
    return suggestions

# Main Header
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem;">
        🌿 AI Environmental Decision Intelligence Platform
    </h1>
    <p style="font-size: 1.2rem; color: #888;">
        Green Mobility + AQI Optimization • Real-time Environmental Intelligence
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Calculate current AQI
current_aqi = calculate_aqi(traffic_level, green_cover)
aqi_category, aqi_class, aqi_emoji = get_aqi_category(current_aqi)
exposure_score = calculate_exposure_score(current_aqi, time_outside)

# Top Row - Key Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="🌡️ Current AQI",
        value=current_aqi,
        delta=f"{aqi_category}",
        delta_color="inverse" if current_aqi > 100 else "normal"
    )

with col2:
    st.metric(
        label="🚗 Traffic Level",
        value=f"{traffic_level}%",
        delta="High" if traffic_level > 70 else ("Moderate" if traffic_level > 40 else "Low"),
        delta_color="inverse" if traffic_level > 70 else "normal"
    )

with col3:
    st.metric(
        label="🌳 Green Cover",
        value=f"{green_cover}%",
        delta="Good" if green_cover > 40 else "Low",
        delta_color="normal" if green_cover > 40 else "inverse"
    )

with col4:
    st.metric(
        label="🛡️ Exposure Score",
        value=f"{exposure_score}/100",
        delta="Safe" if exposure_score > 70 else ("Moderate" if exposure_score > 40 else "At Risk"),
        delta_color="normal" if exposure_score > 70 else "inverse"
    )

st.markdown("---")

# Main Content - Two Column Layout
left_col, right_col = st.columns([1, 1])

with left_col:
    # AQI Prediction Card
    st.markdown("### 📊 AQI Prediction & Analysis")
    
    with st.container():
        aqi_col1, aqi_col2 = st.columns([1, 1])
        
        with aqi_col1:
            st.markdown(f"""
            <div class="aqi-display {aqi_class}">
                {aqi_emoji} {current_aqi}
            </div>
            """, unsafe_allow_html=True)
            st.caption(f"Category: **{aqi_category}**")
        
        with aqi_col2:
            st.markdown("**Health Recommendations:**")
            if current_aqi <= 50:
                st.success("✅ Air quality is satisfactory. Enjoy outdoor activities!")
            elif current_aqi <= 100:
                st.info("ℹ️ Acceptable quality. Sensitive individuals should limit prolonged outdoor exertion.")
            elif current_aqi <= 150:
                st.warning("⚠️ Sensitive groups may experience health effects. Limit outdoor activities.")
            else:
                st.error("🚨 Health alert! Everyone may experience serious health effects.")
    
    st.markdown("---")
    
    # Scenario Simulator
    st.markdown("### 🔬 Scenario Simulator")
    
    with st.expander("Explore What-If Scenarios", expanded=True):
        sim_col1, sim_col2 = st.columns(2)
        
        with sim_col1:
            sim_traffic = st.slider(
                "Simulated Traffic",
                0, 100, traffic_level,
                key="sim_traffic"
            )
        
        with sim_col2:
            sim_green = st.slider(
                "Simulated Green Cover",
                0, 100, green_cover,
                key="sim_green"
            )
        
        simulated_aqi = calculate_aqi(sim_traffic, sim_green)
        aqi_change = simulated_aqi - current_aqi
        
        sim_metric_col1, sim_metric_col2 = st.columns(2)
        
        with sim_metric_col1:
            st.metric(
                label="Simulated AQI",
                value=simulated_aqi,
                delta=f"{aqi_change:+d} from current",
                delta_color="inverse" if aqi_change > 0 else "normal"
            )
        
        with sim_metric_col2:
            sim_exposure = calculate_exposure_score(simulated_aqi, time_outside)
            exposure_change = sim_exposure - exposure_score
            st.metric(
                label="Simulated Exposure Score",
                value=f"{sim_exposure}/100",
                delta=f"{exposure_change:+.1f}",
                delta_color="normal" if exposure_change > 0 else "inverse"
            )
        
        if aqi_change < 0:
            st.success(f"🎉 This scenario would improve air quality by {abs(aqi_change)} AQI points!")
        elif aqi_change > 0:
            st.warning(f"⚠️ This scenario would worsen air quality by {aqi_change} AQI points.")
        else:
            st.info("ℹ️ No change in air quality predicted.")

with right_col:
    # Optimization Engine
    st.markdown("### ⚡ Optimization Engine")
    
    if st.button("🚀 Optimize Environment", use_container_width=True):
        st.session_state.optimized = True
        st.session_state.optimization_results = generate_optimization_suggestions(
            traffic_level, green_cover, current_aqi
        )
    
    if st.session_state.optimized and st.session_state.optimization_results:
        st.markdown("**Recommended Actions:**")
        
        for suggestion in st.session_state.optimization_results:
            with st.container():
                st.markdown(f"""
                <div class="action-item">
                    <strong>{suggestion['icon']} {suggestion['title']}</strong><br>
                    {suggestion['description']}<br>
                    <small style="color: #00d4ff;">Impact: {suggestion['impact']}</small>
                </div>
                """, unsafe_allow_html=True)
        
        # Calculate optimized metrics
        optimized_traffic = max(0, traffic_level - 20)
        optimized_green = min(100, green_cover + 15)
        optimized_aqi = calculate_aqi(optimized_traffic, optimized_green)
        
        st.markdown("---")
        st.markdown("**If all recommendations implemented:**")
        
        opt_col1, opt_col2 = st.columns(2)
        with opt_col1:
            st.metric(
                "Optimized AQI",
                optimized_aqi,
                delta=f"{optimized_aqi - current_aqi}",
                delta_color="inverse" if optimized_aqi > current_aqi else "normal"
            )
        with opt_col2:
            opt_exposure = calculate_exposure_score(optimized_aqi, time_outside)
            st.metric(
                "Optimized Exposure Score",
                f"{opt_exposure}/100",
                delta=f"{opt_exposure - exposure_score:+.1f}",
                delta_color="normal"
            )
    else:
        st.info("👆 Click 'Optimize Environment' to get personalized recommendations")
    
    st.markdown("---")
    
    # Green Route Navigator
    st.markdown("### 🗺️ Green Route Navigator")
    
    route_data = generate_route_data(source, destination)
    
    if route_data:
        st.markdown(f"**Route: {source} → {destination}**")
        
        route_col1, route_col2 = st.columns(2)
        
        with route_col1:
            st.markdown("""
            <div class="route-card">
                <strong>🚀 Fastest Route</strong>
            </div>
            """, unsafe_allow_html=True)
            st.write(f"📏 Distance: **{route_data['fastest']['distance']} km**")
            st.write(f"⏱️ Time: **{route_data['fastest']['time']} min**")
            st.write(f"🌫️ Avg AQI: **{route_data['fastest']['aqi_exposure']}**")
            if route_data['fastest']['aqi_exposure'] > 100:
                st.warning("Higher pollution exposure")
        
        with route_col2:
            st.markdown("""
            <div class="eco-route-card">
                <strong>🌿 Eco-Friendly Route</strong>
            </div>
            """, unsafe_allow_html=True)
            st.write(f"📏 Distance: **{route_data['eco']['distance']} km**")
            st.write(f"⏱️ Time: **{route_data['eco']['time']} min**")
            st.write(f"🌫️ Avg AQI: **{route_data['eco']['aqi_exposure']}**")
            st.success("✅ Recommended for health")
        
        # Route comparison
        time_diff = route_data['eco']['time'] - route_data['fastest']['time']
        aqi_diff = route_data['fastest']['aqi_exposure'] - route_data['eco']['aqi_exposure']
        
        st.info(f"💡 Taking the eco-friendly route adds **{time_diff} min** but reduces pollution exposure by **{aqi_diff} AQI points**")
    else:
        st.info("📍 Enter source and destination in the sidebar to see route options")

st.markdown("---")

# Personal Exposure Section
st.markdown("### 🛡️ Personal Exposure Analysis")

exp_col1, exp_col2, exp_col3 = st.columns([2, 1, 1])

with exp_col1:
    st.markdown("**Your Daily Exposure Profile**")
    
    # Visual exposure meter
    exposure_percentage = 100 - exposure_score
    st.progress(min(1.0, exposure_percentage / 100))
    
    st.caption(f"Exposure Level: {exposure_percentage:.1f}% of safe daily limit")
    
    if exposure_score >= 80:
        st.success("🟢 **Excellent** - Your exposure is well within safe limits")
    elif exposure_score >= 60:
        st.info("🟡 **Good** - Exposure is acceptable, minor precautions recommended")
    elif exposure_score >= 40:
        st.warning("🟠 **Moderate** - Consider reducing outdoor time or wearing a mask")
    else:
        st.error("🔴 **High Risk** - Strongly recommend staying indoors or using protection")

with exp_col2:
    st.metric(
        "Cumulative AQI Exposure",
        f"{int(current_aqi * time_outside)}",
        help="AQI × Hours of exposure"
    )
    
    st.metric(
        "Time Outside",
        f"{time_outside} hrs",
        help="Duration of outdoor exposure"
    )

with exp_col3:
    # Health impact indicators
    st.markdown("**Health Indicators**")
    
    if current_aqi <= 50:
        st.write("❤️ Cardiovascular: Low Risk")
        st.write("🫁 Respiratory: Low Risk")
    elif current_aqi <= 100:
        st.write("❤️ Cardiovascular: Low Risk")
        st.write("🫁 Respiratory: Mild Risk")
    elif current_aqi <= 150:
        st.write("💛 Cardiovascular: Moderate Risk")
        st.write("🫁 Respiratory: Moderate Risk")
    else:
        st.write("💔 Cardiovascular: High Risk")
        st.write("🫁 Respiratory: High Risk")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>🌿 AI Environmental Decision Intelligence Platform</p>
    <p style="font-size: 0.8rem;">Built with Streamlit • Data is simulated for demonstration purposes</p>
</div>
""", unsafe_allow_html=True)
