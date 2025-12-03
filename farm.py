import streamlit as st
import time

st.title("🌾 Mini Farm Game")

# ----------------------------
# Initialize Default Game State
# ----------------------------
defaults = {
    "coins": 50,
    "wheat": 0,
    "crop_status": "empty",   # empty, growing, ready
    "planted_time": None
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

GROW_TIME = 5  # seconds needed to grow wheat

# ----------------------------
# Crop Logic
# ----------------------------
def plant_wheat():
    if st.session_state.crop_status == "empty":
        if st.session_state.coins >= 5:
            st.session_state.coins -= 5
            st.session_state.crop_status = "growing"
            st.session_state.planted_time = time.time()
        else:
            st.error("Not enough coins!")
    else:
        st.warning("The field is not empty!")


def update_crop_status():
    """Automatically updates crop to 'ready' when enough time has passed."""
    if st.session_state.crop_status == "growing":
        elapsed = time.time() - st.session_state.planted_time
        if elapsed >= GROW_TIME:
            st.session_state.crop_status = "ready"


def harvest_wheat():
    if st.session_state.crop_status == "ready":
        st.session_state.crop_status = "empty"
        st.session_state.wheat += 1
        st.session_state.planted_time = None
    else:
        st.warning("Nothing ready to harvest!")


# Update crop state every run
update_crop_status()

# ----------------------------
# Display Inventory
# ----------------------------
st.subheader("📦 Inventory")
st.write(f"💰 **Coins:** {st.session_state.coins}")
st.write(f"🌾 **Wheat:** {st.session_state.wheat}")

# ----------------------------
# Field Display
# ----------------------------
st.subheader("🌱 Field Status")

status = st.session_state.crop_status

if status == "empty":
    st.info("Field is empty. Plant something!")
elif status == "growing":
    st.warning("Crop is growing... ⏳")
elif status == "ready":
    st.success("Crop is ready to harvest! 🌾")  # <-- FIXED LINE


# ----------------------------
# Action Buttons
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("🌱 Plant Wheat (5 coins)"):
        plant_wheat()

with col2:
    if st.button("🌾 Harvest"):
        harvest_wheat()

# ----------------------------
# Market (Sell Wheat)
# ----------------------------
st.subheader("🏪 Market")

if st.button("Sell 1 Wheat for 10 Coins"):
    if st.session_state.wheat > 0:
        st.session_state.wheat -= 1
        st.session_state.coins += 10
        st.success("Sold 1 Wheat!")
    else:
        st.error("You have no wheat to sell!")
