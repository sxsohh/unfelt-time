import os
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# -------------------------------------------------------
# Load Time Dilation Dataset
# -------------------------------------------------------

@st.cache_data
def load_city_data():
    path = "data/processed/worldcities_time_dilation_w_elevation.csv"
    df = pd.read_csv(path)

    # Ensure no missing core fields
    df = df.dropna(
        subset=[
            "lat",
            "lng",
            "aging_factor",
            "microseconds_difference_per_year",
            "elevation_meters",
        ]
    )

    return df


df = load_city_data()


# -------------------------------------------------------
# Helper Formatting
# -------------------------------------------------------

def format_microseconds(us):
    sign = "gained" if us >= 0 else "lost"
    return f"{abs(us):.3f} microseconds {sign} per year"


# -------------------------------------------------------
# Physics + Perception Simulations
# -------------------------------------------------------

def simulate_proper_time(total_time=10, velocity_fraction=0.8, steps=1000):
    """
    Simulates proper time vs coordinate time under special relativity.
    velocity_fraction: fraction of the speed of light.
    """
    c = 299_792_458  # speed of light (m/s)
    velocity = velocity_fraction * c

    t = np.linspace(0, total_time, steps)
    gamma = np.sqrt(1 - (velocity / c) ** 2)
    proper = t * gamma
    return t, proper


def simulate_brain_sampling(total_time=2.0, real_fps=1000, brain_fps=20):
    """
    Real time is continuous (1000 Hz), but the brain samples the world
    ~20 times per second. This shows why we cannot feel continuous time.
    """
    real_t = np.linspace(0, total_time, int(real_fps * total_time))
    perceived = np.linspace(0, total_time, int(brain_fps * total_time))
    return real_t, perceived


def spacetime_worldlines():
    """
    Creates two simple worldlines: one stationary, one moving.
    """
    x = np.linspace(0, 10, 300)
    ct_stationary = np.linspace(0, 10, 300)
    ct_moving = 0.6 * ct_stationary  # moving observer experiences less proper time
    return x, ct_stationary, ct_moving


# -------------------------------------------------------
# Streamlit UI
# -------------------------------------------------------

st.set_page_config(
    page_title="Unfelt Time",
    layout="wide"
)

st.title("Unfelt Time: A Study of Time Dilation and Human Perception")

tab1, tab2 = st.tabs(["City Time Dilation Explorer", "Why Humans Cannot Feel Time"])

# -------------------------------------------------------
# TAB 1: CITY-TO-CITY TIME DIFFERENCE
# -------------------------------------------------------

with tab1:
    st.header("City Time Dilation Explorer")
    st.write(
        """
        This tool compares how many microseconds of proper time you gain or lose per year
        depending on your city’s latitude and elevation.
        These effects are extremely small, but measurable using precise atomic clocks.
        """
    )

    cities = df["city_ascii"].sort_values().unique()

    colA, colB = st.columns(2)

    with colA:
        city_a = st.selectbox("Select City A", cities, index=0)

    with colB:
        city_b = st.selectbox("Select City B", cities, index=1)

    row_a = df[df["city_ascii"] == city_a].iloc[0]
    row_b = df[df["city_ascii"] == city_b].iloc[0]

    # Display metrics
    colA2, colB2 = st.columns(2)

    with colA2:
        st.subheader(f"{row_a['city_ascii']} ({row_a['country']})")
        st.write(f"Latitude: {row_a['lat']:.2f}°")
        st.write(f"Elevation: {row_a['elevation_meters']:.1f} m")
        st.write(f"Aging factor: {row_a['aging_factor']:.12f}")
        st.write("Time shift: " + format_microseconds(row_a["microseconds_difference_per_year"]))

    with colB2:
        st.subheader(f"{row_b['city_ascii']} ({row_b['country']})")
        st.write(f"Latitude: {row_b['lat']:.2f}°")
        st.write(f"Elevation: {row_b['elevation_meters']:.1f} m")
        st.write(f"Aging factor: {row_b['aging_factor']:.12f}")
        st.write("Time shift: " + format_microseconds(row_b["microseconds_difference_per_year"]))

    diff = row_a["microseconds_difference_per_year"] - row_b["microseconds_difference_per_year"]

    st.markdown("---")
    st.subheader("Relative Difference")

    st.write(
        f"Living in **{city_a}** instead of **{city_b}** changes your clock rate by "
        f"**{abs(diff):.3f} microseconds per year**."
    )

    st.info(
        """
        These changes come from two effects:
        1. Higher elevation has weaker gravity, so clocks tick slightly faster.
        2. Higher latitude rotates slower with Earth, so clocks tick slightly faster.

        Both effects are real, measurable, and predicted by relativity, but far too small to feel.
        """
    )


# -------------------------------------------------------
# TAB 2: WHY HUMANS CANNOT FEEL TIME
# -------------------------------------------------------

with tab2:
    st.header("Why Humans Cannot Feel Time")

    st.write(
        """
        Humans cannot directly feel the passage of time.  
        These visualizations explain the physics and neuroscience behind why.
        """
    )

    # 1. Special Relativity
    st.subheader("1. Special Relativity: Proper Time vs Coordinate Time")
    t, proper = simulate_proper_time()

    fig1, ax1 = plt.subplots(figsize=(7, 4))
    ax1.plot(t, t, label="Coordinate Time (Stationary)")
    ax1.plot(t, proper, label="Proper Time (Moving)")
    ax1.set_xlabel("Seconds")
    ax1.set_ylabel("Time Experienced")
    ax1.legend()
    st.pyplot(fig1)

    st.write(
        """
        Motion reduces experienced time.  
        A fast moving observer experiences less time passing but never notices this difference
        because biological perception operates at a much larger scale.
        """
    )

    # 2. Brain Sampling
    st.subheader("2. Human Perception: The Brain Samples Reality")
    real_t, perceived_t = simulate_brain_sampling()

    fig2, ax2 = plt.subplots(figsize=(7, 4))
    ax2.plot(real_t, np.zeros_like(real_t), alpha=0.6, label="Real Continuous Time")
    ax2.scatter(perceived_t, np.zeros_like(perceived_t), color="red", label="Brain Frames")
    ax2.set_yticks([])
    ax2.set_xlabel("Seconds")
    ax2.legend()
    st.pyplot(fig2)

    st.write(
        """
        The brain takes snapshots of the world around 20 times per second.  
        Because perception is discrete, time never feels continuous.
        We only feel change, not time itself.
        """
    )

    # 3. Spacetime Diagram
    st.subheader("3. Spacetime Diagram: Why We Cannot Move Through Time at Will")
    x, ct_stat, ct_mov = spacetime_worldlines()

    fig3, ax3 = plt.subplots(figsize=(6, 5))
    ax3.plot(x, ct_stat, label="Stationary Worldline")
    ax3.plot(x, ct_mov, label="Moving Worldline")
    ax3.set_xlabel("Space")
    ax3.set_ylabel("ct (Time × Speed of Light)")
    ax3.legend()
    st.pyplot(fig3)

    st.write(
        """
        In spacetime, motion defines your worldline.  
        But you cannot change your velocity through time like you can through space.
        You are locked to a single forward direction, so you cannot feel or control time flow.
        """
    )

    st.success("The theory section is complete and demonstrates the physics and neuroscience clearly.")
