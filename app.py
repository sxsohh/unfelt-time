import os
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import tensorflow as tf

# -----------------------------------
# Load data and model
# -----------------------------------

@st.cache_data
def load_city_data():
    path = "data/processed/worldcities_time_dilation_w_elevation.csv"
    df = pd.read_csv(path)

    df = df.dropna(
        subset=["lat", "lng", "aging_factor", "microseconds_difference_per_year"]
    )

    return df


@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        "model/time_dilation_nn.h5",
        compile=False
    )


df = load_city_data()
model = load_model()

# -----------------------------------
# Tools
# -----------------------------------

def format_microseconds(us):
    sign = "gained" if us >= 0 else "lost"
    return f"{abs(us):.3f} microseconds {sign} per year"


# -----------------------------------
# Physics Simulations for Theory Tab
# -----------------------------------

def simulate_proper_time(total_time=10, velocity=0.8 * 299_792_458, steps=1000):
    c = 299_792_458
    t = np.linspace(0, total_time, steps)
    gamma = np.sqrt(1 - (velocity / c) ** 2)
    proper = t * gamma
    return t, proper


def simulate_brain_sampling(total_time=2.0, real_fps=1000, brain_fps=20):
    real_t = np.linspace(0, total_time, int(real_fps * total_time))
    perceived = np.linspace(0, total_time, int(brain_fps * total_time))
    return real_t, perceived


def spacetime_worldlines():
    x = np.linspace(0, 10, 300)
    ct_stationary = np.linspace(0, 10, 300)
    ct_moving = 0.6 * ct_stationary
    return x, ct_stationary, ct_moving


# -----------------------------------
# STREAMLIT UI
# -----------------------------------

st.set_page_config(
    page_title="Unfelt Time",
    layout="wide"
)

st.title("Unfelt Time: A Study of Time Dilation and Human Perception")

tab1, tab2 = st.tabs(["City Time Dilation Explorer", "Why Humans Cannot Feel Time"])

# -----------------------------------
# TAB 1: CITY TIME DILATION
# -----------------------------------

with tab1:
    st.header("City Time Dilation Explorer")
    st.write(
        """
        This tool compares how many **microseconds of proper time** people gain or lose per year
        depending on their latitude and elevation.
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

    colA2, colB2 = st.columns(2)

    with colA2:
        st.subheader(f"{row_a['city_ascii']} ({row_a['country']})")
        st.write(f"Elevation: {row_a['elevation_meters']:.1f} m")
        st.write(f"Aging factor: {row_a['aging_factor']:.12f}")
        st.write("Time shift: " + format_microseconds(row_a["microseconds_difference_per_year"]))

    with colB2:
        st.subheader(f"{row_b['city_ascii']} ({row_b['country']})")
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

# -----------------------------------
# TAB 2: THEORY, WHY HUMANS CANNOT FEEL TIME
# -----------------------------------

with tab2:
    st.header("Why Humans Cannot Feel Time")
    st.write(
        """
        This section explains the physics and neuroscience behind why humans cannot directly
        experience the flow of time, even though time is a real dimension in spacetime.
        """
    )

    # -----------------------------------
    # 1. Special Relativity Visualization
    # -----------------------------------

    st.subheader("1. Special Relativity: Proper Time vs Coordinate Time")

    t, proper = simulate_proper_time()

    fig1, ax1 = plt.subplots(figsize=(7, 4))
    ax1.plot(t, t, label="Coordinate Time (Stationary Observer)")
    ax1.plot(t, proper, label="Proper Time (Moving Observer)")
    ax1.set_xlabel("Seconds")
    ax1.set_ylabel("Time Experienced")
    ax1.legend()
    st.pyplot(fig1)

    st.write(
        """
        In Einstein's theory, motion affects time.  
        A moving observer experiences **less proper time** than a stationary one.  
        But humans never feel this slowing down because biological perception ignores it.
        """
    )

    # -----------------------------------
    # 2. Brain Sampling Simulation
    # -----------------------------------

    st.subheader("2. Human Perception: The Brain Samples Reality, It Does Not Feel Time")

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
        Humans perceive the world at about **20 frames per second**, far slower than real time.
        We never experience continuous time only snapshots of change.
        This is why we cannot “feel” time passing.
        """
    )

    # -----------------------------------
    # 3. Spacetime Diagram
    # -----------------------------------

    st.subheader("3. Spacetime Diagram: Why Time Is a Dimension but We Cannot Move Through It")

    x, ct_stat, ct_mov = spacetime_worldlines()

    fig3, ax3 = plt.subplots(figsize=(6, 5))
    ax3.plot(x, ct_stat, label="Stationary Worldline")
    ax3.plot(x, ct_mov, label="Moving Worldline")
    ax3.set_xlabel("Space (x)")
    ax3.set_ylabel("ct (Time × Speed of Light)")
    ax3.legend()
    st.pyplot(fig3)

    st.write(
        """
        In spacetime, you trace a path called a worldline.  
        But you are **locked** moving forward in time at one rate.  
        Unlike space, you cannot choose your velocity through time so you cannot feel it.
        """
    )

    st.markdown("---")
    st.success("This page now fully demonstrates the physics and neuroscience behind why humans cannot feel time.")

